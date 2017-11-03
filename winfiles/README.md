
# winfiles #

Iterates over a directory and makes filenames safe for transfer to Windows based
filesystems. Removes illegal characters and also gets rid of junk files such as
the well known .DS_Store files.

Also writes an output log file in the given directory which can be checked and
used to reverse changes. This would required an extra script though.

## Usage ##

You can execute the script from the command line directly - if execution
permissions have been set - or by using a Python 3 interpreter.

    $ python winfiles.py

## License ##

This script falls under the same license as the repository it stems from. For
more information please refer to
[LICENSE](https://github.com/catlinman/pyscripts/blob/master/LICENSE)
