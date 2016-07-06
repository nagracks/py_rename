# Python Rename

> Python file rename script

Usage
-----

```
usage: py_rename.py [-h] [-v] [-A string] [-B string] [-n] [--lower]
                    [--remove-space] [--camel-case]
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
  -n, --dryrun          perform a dry run (will no run any actions)
  --lower               lowercase the filename
  --remove-space        remove space with underscore
  --camel-case          convert to camel case
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
* [ ] Implement regular expressions


Contributing
------------

Feel free to improve `Python Rename`. All kind of pull-requests are welcome. 

LICENSE
-------

`Python Rename` is licensed under 
[GPL3](https://github.com/nagracks/py_rename/blob/master/LICENSE)
