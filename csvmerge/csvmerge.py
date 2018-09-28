#!/usr/bin/env python
# Python version 3.7+

"""CSV Merge
Usage:
    csvmerge.py [--input=PATH] [--output=PATH] [--delimiter=STRING]
    csvmerge.py (-h | --help)
    csvmerge.py (-v | --version)

Options:
    -h --help              Show this screen.
    -v --version           Show version.

    -i --input=PATH        Input file to read from.
    -o --output=PATH       Output file to write to.
    -d --delimiter=STRING  Delimiter between values. Defaults to comma.

Description:
    Merges rows from a CSV with equal first field identifiers.

    If no input file is specified stdin will be used.

Requirements:
    Python 3.7+, docopt
"""

# Import system modules.
import sys

# Command line parsing.
from docopt import docopt


def merge(data, delimiter):
    """
    Merge rows with an equal starting index from an array of CSV data rows.

    Args:
        data (list): Input list of string rows to sort.
        delimiter (str): Delimiter of the CSV format to use for value splitting.

    Returns:
        merged list of rows in string format.
    """
    data_merged = []
    row_merged = []

    # Register an empty field.
    id = None

    for row in data:
        # Split the line and get values using the delimiter.
        values = row.split(delimiter)

        # Assign a value if this is the first run.
        if not id:
            id = values[0]
            row_merged.append(id)

        # If our identifier does not match up with the last, append the row and reset.
        if values[0] != id:
            data_merged.append(row_merged)
            row_merged = []

            id = values[0]
            row_merged.append(id)

        # Begin iteration over values skipping our identifier.
        for value in values[1:]:
            row_merged.append(value)

        # If this is the last row append it.
        if row == data[-1]:
            data_merged.append(row_merged)

    return data_merged


def cli():
    """ Script and command line interface entry point. """
    args = docopt(__doc__, version="CSV Merge 0.2")

    # Handle arguments.
    input_path = args["--input"]
    output_path = args["--output"]

    delimiter = args["--delimiter"] or ","

    # Create a field to store our merged data in.
    merged = []

    # Read the file if specified.
    if input_path:
        with open(input_path) as f:
            # Insert the lines into the array and strip whitespace.
            merged = merge([s.strip() for s in f.readlines()], delimiter)

    # Otherwise read from stdin.
    else:
        merged = merge([s.strip() for s in sys.stdin.readlines()], delimiter)

    # If an output path is defined write to it.
    if output_path:
        with open(output_path, "w") as f:
            for row in merged:
                f.write("{}\n".format(delimiter.join(row)))

    # Otherwise just print out the data.
    else:
        for row in merged:
            print(delimiter.join(row))


if __name__ == "__main__":
    cli()
