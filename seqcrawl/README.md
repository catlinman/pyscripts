
# Seqcrawl #

Crawls an entry point URL using generated fixed length sequences from an
input character set and saves responses as files in the execution directory.

## Setup & Usage ##

Install the dependencies of *docopt* and *requests* first using *pip*.

    $ pip install docopt requests

Once all requirements have been fulfilled you can execute the script from the
command line directly - if execution permissions have been set - or by using
a Python 3 interpreter.

    $ python seqcrawl.py (-h | --help) (-v | --version)

    $ python seqcrawl.py <url> <characters> <length>
        [--start <number>]
        [--end <number>]
        [--log <path>]
        [--sleep <number>]

For additional information on each argument and option please use the *help*
command as it describes each in detail.

## License ##

This script falls under the same license as the repository it stems from. For
more information please refer to
[LICENSE](https://github.com/catlinman/pyscripts/blob/master/LICENSE)
