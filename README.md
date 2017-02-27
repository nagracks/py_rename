# Python Rename

> Python file rename script

Usage
-----

```
usage: py_rename.py [-h] [-v] [-A string] [-B string] [-r string] [-n]
                    [--lower] [--remove-space] [--camel-case] [-s]
                    filename

Python Rename

positional arguments:
  filename              filename

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -A string, --prefix string
                        prefix filename with prefix string
  -B string, --postfix string
                        postfix filename with postfix string
  -r string, --rename string
                        replace filename with string
  -n, --dryrun          perform a dry run (will not run any actions)
  --lower               lowercase the filename
  --remove-space        remove space with underscore
  --camel-case          convert to camel case
  -s, --silent          silence output
```

`$ py_rename.py -A vacation-photo- IMG*.jpg`

TODO
----

`Python Rename` is a work in progress, so any ideas and patches are 
appreciated.

* [x] Prefix filename with prefix string
* [x] Postfix filename with postfix string
* [x] Convert to lower case
* [x] Convert to naming conventions `CamelCase` `underscore_case` (need work, not perfect yet)
* [x] Make arguments work properly
* [ ] Implement regular expressions
* [ ] Recursively walk directories and bulk-rename files

Contributing
------------

Feel free to improve `Python Rename`. All kind of pull-requests are welcome.

Contributors
------------

* [kretusmaximus](https://github.com/kretusmaximus)
* [astonge](https://github.com/astonge)
* [prabhath6](https://github.com/prabhath6)
* [Luki138](https://github.com/Luki138)

LICENSE
-------

`Python Rename` is licensed under 
[MIT](https://github.com/nagracks/py_rename/blob/master/LICENSE)
