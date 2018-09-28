#!/usr/bin/env python
# Python version 3.7+

"""CSV Sort
Usage:
    csvsort.py [--input=PATH] [--output=PATH] [--delimiter=STRING]
    csvsort.py (-h | --help)
    csvsort.py (-v | --version)

Options:
    -h --help              Show this screen.
    -v --version           Show version.

    -i --input=PATH        Input file to read from.
    -o --output=PATH       Output file to write to.
    -d --delimiter=STRING  Delimiter between values. Defaults to comma.

Description:
    Sorts rows from an input CSV file.

    If no input file is specified stdin will be used.

Requirements:
    Python 3.7+, docopt
"""

# Import system modules.
import sys

# Command line parsing.
from docopt import docopt


def sort(data, delimiter=","):
    """
    Sorts an array of CSV data rows stored as strings and returns it as a list.

    Args:
        data (list): input list of string rows or row values as a list to sort.
        delimiter (str): delimiter of the CSV format to use for value splitting.

    Returns:
        list of sorted rows in string format.
    """
    data_sorted = []

    for row in data:
        # Convert our string row into a list of strings if it's not already one.
        values = row.split(delimiter) if type(row) is str else row

        # Store our identifier.
        id = values[0]

        # Sort our row and add the identifier back to the start.
        row_sorted = sorted(values[1:])
        row_sorted.insert(0, id)

        # Insert our sorted data back into list.
        data_sorted.append(row_sorted)

    return data_sorted


def cli():
    """ Script and command line interface entry point. """
    args = docopt(__doc__, version="CSV Sort 0.2")

    # Handle arguments.
    input_path = args["--input"]
    output_path = args["--output"]

    delimiter = args["--delimiter"] or ","

    # Create a field to store our sorted data in.
    data_sorted = []

    # Read the file if specified.
    if input_path:
        with open(input_path) as f:
            # Insert the lines into the array and strip whitespace.
            data_sorted = sort([s.strip() for s in f.readlines()], delimiter)
            print(data_sorted)

    # Otherwise read from stdin.
    else:
        data_sorted = sort([s.strip() for s in sys.stdin.readlines()], delimiter)

    # If an output path is defined write to it.
    if output_path:
        with open(output_path, "w") as f:
            for row in data_sorted:
                f.write("{}\n".format(delimiter.join(row)))

    # Otherwise just print out the data.
    else:
        for row in data_sorted:
            print(delimiter.join(row))


if __name__ == "__main__":
    cli()
