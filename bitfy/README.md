
# Bitfy #

Takes in an input such as files, websites and URLs, filters out all links and
converts them to bit.ly links.

## Setup & Usage ##

Install the dependencies of *docopt* and *requests* first using *pip*.

    $ pip install docopt requests

Once all requirements have been fulfilled you can execute the script from the
command line directly - if execution permissions have been set - or by using
a Python 3 interpreter.

    $ python bitfy.py (-h | --help) (-v | --version)

    $ python bitfy.py
        --token=TOKEN [--title=NAME]
        --url=URL [--title=NAME]
        --request=URL [--title=NAME]
        --file=PATH [--title=NAME]

Before you can make any bitly links you will have to specifiy your OAuth
developer token from bitly. You can supply the token using the command line
option.

For additional information on each argument and option please use the *help*
command as it describes each in detail.

## License ##

This script falls under the same license as the repository it stems from. For
more information please refer to
[LICENSE](https://github.com/catlinman/pyscripts/blob/master/LICENSE)
