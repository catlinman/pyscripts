
# rangedownload #

Simple ranged download script. For those times when the other end just decides
to close the file stream and you end up with partial files. This fixes that.

## Setup & Usage ##

Install the dependency of *requests* using *pip*.

    $ pip install requests

You can execute the script from the command line directly - if execution
permissions have been set - or by using a Python 3 interpreter.

    $ python rangedownload.py

This download script is partially extracted from my Bandcamp downloader,
[campdown](https://github.com/catlinman/campdown).

The first argument is the URL to download the file from.

The second argument is the optional output folder the file should be written to.
If none is specified the folder this script is in will be used.

## License ##

This script falls under the same license as the repository it stems from. For
more information please refer to
[LICENSE](https://github.com/catlinman/pyscripts/blob/master/LICENSE)
