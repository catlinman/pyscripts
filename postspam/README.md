
# Postspam #

Makes POST requests to a given URL with randomized field selection data
from an input CSV file. CSV headers determine the fields to set.

## Setup & Usage ##

Install the dependencies of *docopt* and *requests* first using *pip*.

    $ pip install docopt requests

Once all requirements have been fulfilled you can execute the script from the
command line directly - if execution permissions have been set - or by using
a Python 3 interpreter.

    $ python postspam.py (-h | --help) (-v | --version)

    $ python postspam.py <url> <data>
        [--count=COUNT]
        [--sleep=SLEEP]
        [--random=RANDOM]

Before you can make any POST requests you will have to create a CSV file that
specifies which fields should receive which data sets. The formatting is rather
simple with the first column being the identifier of the form field on the page
you are posting to and the second being the content. Further content is comma
separated and converted into an array from which each additional column is
randomly picked for the next request.

If you an example, check the *postspam.csv* file. It also already contains
a good amount of data you can use for whatever you want.

To avoid spamming too much content there are flags that can be set to sleep
between requests with an additional flag for an extra random amount of time.

A limit for the amount of requests to be made can also be set.

For additional information on each argument and option please use the *help*
command as it describes each in detail.

## License ##

This script falls under the same license as the repository it stems from. For
more information please refer to
[LICENSE](https://github.com/catlinman/pyscripts/blob/master/LICENSE)
