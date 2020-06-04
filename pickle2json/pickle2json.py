#!/usr/bin/env python
# Python version 3.7+

"""Pickle2JSON
Usage:
    pickle2json.py (<input> | --input=PATH) [--output=PATH]
    pickle2json.py (-h | --help)
    pickle2json.py (-v | --version)

Options:
    -h --help              Show this screen.
    -v --version           Show version.

    -i --input=PATH        Input pickled file to read from.
    -o --output=PATH       Output file to write to.

Description:
    Converts a Python Pickle object to a JSON formatted file and saves it in
    the working directory or a specified output directory.

Requirements:
    Python 3.7+, docopt, (Unpickled imports)
"""

import re
import sys
import os
import _pickle as pickle
import json

# Command line parsing.
from docopt import docopt


def regex_result_label_aws_node(result):
    """
        Regex search handler: Filter out AWS nodes into a clean format.

        Args:
            result (MatchObject): Match result from a previous regex match.
    """
    result = result.group(0) # Capture our entire matching result.

    # Filter out values by labels using regex capture groups.
    account = re.match(r"^.*(account).*x00(.*)q\\x02", result).group(2)
    region = re.match(r"^.*(region).*x00(.*)q\\x04", result).group(2)
    resource = re.match(r"^.*(resource).*x00(.*)q\\x06", result).group(2)

    # Build a unique resource identifier and group by accountid & region.
    return "\"{}-({})-{}\"".format(account, region, resource)

def regex_result_escape_recursive(result):
    """
        Regex search handler: De-construct objects that implement a JSON like
        structure in our present schema.

        Args:
            result (MatchObject): Match result from a previous regex match.
    """
    result = result.group(0).replace('"', "'").replace("'{", '"{').replace("}'", '}"')

    return result

def regex_result_escape_duplicate_quotes(result):
    """
        Regex search handler: Escape sections where we find duplicate empty
        quotes surrounding objects.

        Args:
            result (MatchObject): Match result from a previous regex match.
    """
    return "{}\"{}\"".format(result.group(1), result.group(3))

def regex_result_escape_descriptions(result):
    """
        Regex search handler: Take apart results which encapsulate descriptive
        and escaping content.

        Args:
            result (MatchObject): Match result from a previous regex match.
    """
    content = re.match(r"^(.*?)(?![\(\)\s\.])\W(\W*)$", result.group(1))

    baggage = content.group(2) # Get any additional symbols such as object markers.
    marker = result.group(2) # Get our value and or object separating symbol.

    # Put everything together and swap quotes on the content string.
    return "\"Description\": \"{}\"{}{}".format(content.group(1).replace("\"", "'"), baggage, marker)

def regex_result_escape_commands(result):
    """
        Regex search handler: Take apart results which encapsulate command
        escaping content.

        Args:
            result (MatchObject): Match result from a previous regex match.
    """
    return "\"command\": [\"{}\"]".format(result.group(1).replace("\"", "'"))


def filter_string(str, filters):
    """
    Progressive filtering of a string using search and replace or regex filters.

    Iterate over an array of array pairs using the first as a match and second
    as a replacement. If any additional value added to the pair, run as regex.

    Args:
        str (string): String to run filters against.
        filters (array): Two/Three value array with the first item being a string
            to look up or regex to execute. Second value is a string to replace
            matches with or a callback for regex handling. If a third entry as a
            boolean is supplied, the first entry is handled as a regex query.

    Returns:
        Filtered output of the original input string.
    """

    for filter_set in filters:
        if len(filter_set) > 2:
            str = re.compile(filter_set[0]).sub(filter_set[1], str)

        else:
            str = str.replace(filter_set[0], filter_set[1])
            
    return str

def dict_to_json(dict):
    """
    Converts a Python dictionary object to JSON notation.

    Various object notations are broken apart and filtered out depending on their
    use in the final JSON file.

    Args:
        dict (dictionary): Input dictionary to filter and convert.

    Returns:
        JSON encoded object.
    """

    # Convert our data dictionary into a cohesive string representation.
    stringified = filter_string(str(dict), [
        [r"b'\\.*?'", regex_result_label_aws_node, True],
        [", tzinfo=tzlocal())", "\""],
        ["datetime.datetime(", "\""],
        ["False", "false"],
        ["True", "true"],
        ["None", "\"None\""],
        ["()", "[]"],
        ["\'", "\""],
        ["\"", '"'],
        [r"\"{(\"[\s\S]+?)(?:}\")", regex_result_escape_recursive, True],
        [r"\s*(\"\w+\":)\s*(\"\")(?!,)(?!\s+})(?!})(.*?)(\"\")", regex_result_escape_duplicate_quotes, True],
        [r"\"Description\":\s\"(.*?)([\,\}\]])(?=\s\W)", regex_result_escape_descriptions, True],
        [r"\"command\":\s\[\"(.*?)\"\]", regex_result_escape_commands, True],
        [r"\\u\d\d\d\w", "", True], # Filter out Unicode.
        [r"\\", "", True] # Nuke these little shits because they're screwing up escape sequences when parsing.
    ])

    return json.loads(stringified)

def cli():
    """ Script and command line interface entry point. """
    args = docopt(__doc__, version="Unpickle2JSON 0.1")

    # Handle arguments.
    input_path = args["<input>"] or args["--input"]
    output_path = args["--output"] or os.path.join(os.path.dirname(os.path.realpath(__file__)), "")

    # Open our pickle file in byte mode for reading. Prepare a JSON output.
    with open(input_path, "rb") as pickle_file, open("{}{}.json".format(output_path, os.path.basename(input_path)), "w") as json_file:
        try:
            data = pickle.load(pickle_file) # Read in our data. Don't do anything with it.

        except ModuleNotFoundError as e:
            print((
                "{}\nIt appears that the pickled data requires a module you don't have installed."
                "\nMake sure to fetch it via your preferred package manager (i.e. pip)!"
            ).format(e))

            return

        json.dump(dict_to_json(data), json_file, ensure_ascii=False, sort_keys=True, indent=4)

if __name__ == "__main__":
    cli()
