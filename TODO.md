`bin`
====

The idea is having an encripted version of the password, stored in a file only accesible by the user. When the `pymputator` is launched, it asks for those credentials, encrypts them and compare with the stored one.

With this:
* We avoid that whoever that doesn't know the password can't use it.
* Also it avoids storing the password in plain text, which obviously conflicts the previous point.

`pymputator`
----------
* Everything ...

`store_credentials`
-----------------
* Doctrings.
* It admits whitespace password.
* `write_credentials` apparently leaves an open descriptor to the file
* Change file to mode `500`.

`pymputator`
============

`__init__.py`
-------------
* Version, author, all, etc ...

`imputar.py`
------------
* `TEMPLATE` return to the Abyss, Flame of Udun
* Configure `logging` and `docstrings`
* Replace `bin/pymputator` with this?

`settings.py`
-------------
* Documentation

`workdays.py`
-------------
* Deprecated? (so early ... :()

`parameters.py`
--------------
* A total mess, it is intended to parse command line arguments to `imputar.py` or `pymputator`
* Not even wrong

`templates`
-----------
* Everything


