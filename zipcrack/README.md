
# Zipcrack #

Generates character sequences to brute force crack a zip archive

## Setup & Usage ##

Install the dependency of *docopt* first using *pip*.

    $ pip install docopt

Once all requirements have been fulfilled you can execute the script from the
command line directly - if execution permissions have been set - or by using
a Python 3 interpreter.

    $ python zipcrack.py (-h | --help) (-v | --version)

    $ python zipcrack.py <file> (--sequence=STRING --length=NUMBER | --dictionary=PATH)
        [--iteration-start=NUMBER]
        [--iteration-end=NUMBER]
        [--sleep=NUMBER]
        [--output=PATH]

For additional information on each argument and option please use the *help*
command as it describes each in detail.

## License ##

This script falls under the same license as the repository it stems from. For
more information please refer to
[LICENSE](https://github.com/catlinman/pyscripts/blob/master/LICENSE)
