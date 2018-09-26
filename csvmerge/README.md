
# CSV Merge #

Merges rows from a CSV with equal first field identifiers.

If no input file is specified *stdin* will be used.

## Setup & Usage ##

Install the dependency of *docopt* first using *pip*.

    $ pip install docopt

Once all requirements have been fulfilled you can execute the script from the
command line directly - if execution permissions have been set - or by using
a Python 3 interpreter.

    $ python csvmerge.py (-h | --help) (-v | --version)

    $ csvmerge.py [--input=PATH] [--output=PATH] [--delimiter=STRING]

For additional information on each argument and option please use the *help*
command as it describes each in detail.

## License ##

This script falls under the same license as the repository it stems from. For
more information please refer to
[LICENSE](https://github.com/catlinman/pyscripts/blob/master/LICENSE)
