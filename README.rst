===============
Name of Thrones
===============
.. image:: https://travis-ci.org/Matt-Deacalion/Name-of-Thrones.svg?branch=master
    :target: https://travis-ci.org/Matt-Deacalion/Name-of-Thrones
    :alt: Build Status
.. image:: https://coveralls.io/repos/Matt-Deacalion/Name-of-Thrones/badge.png?branch=master
    :target: https://coveralls.io/r/Matt-Deacalion/Name-of-Thrones?branch=master
    :alt: Test Coverage
.. image:: https://pypip.in/download/name-of-thrones/badge.png?period=week
    :target: https://pypi.python.org/pypi/name-of-thrones/
    :alt: Downloads
.. image:: https://pypip.in/version/name-of-thrones/badge.png
    :target: https://pypi.python.org/pypi/name-of-thrones/
    :alt: Latest Version
.. image:: https://pypip.in/wheel/name-of-thrones/badge.png?new
    :target: https://pypi.python.org/pypi/name-of-thrones/
    :alt: Wheel Status
.. image:: https://pypip.in/license/name-of-thrones/badge.png
    :target: https://pypi.python.org/pypi/name-of-thrones/
    :alt: License

Command line tool to generate words that sound like characters from Game of Thrones. Useful for
unique project names, host names and the occasional stray cat.

.. image:: https://raw.githubusercontent.com/Matt-Deacalion/Name-of-Thrones/screenshots/screenshot.jpg
    :alt: Name of Thrones screenshot

Installation
------------
You can install the *Name of Thrones* using pip:

.. code-block:: bash

    $ pip install name-of-thrones

Usage
-----
You can use the `name-of-thrones` command from the shell to run Name of Thrones::

    $ name-of-thrones --help

    Generate words that sound like characters from Game of Thrones.

    Usage:
      name-of-thrones [--quantity=<number>] [--min=<length>] [--max=<length>] [--json]
      name-of-thrones (-h | --help | --version)

    Options:
      --version                show program's version number and exit.
      -h, --help               show this help message and exit.
      -q, --quantity=<number>  the quantity of words to generate [default: 10].
      --min=<length>           the minimum length of each word [default: 4].
      --max=<length>           the maximum length of each word [default: 10].
      -j, --json               output the names in JSON format.

License
-------
Copyright © 2014 `Matt Deacalion Stevens`_, released under The `MIT License`_.

.. _Matt Deacalion Stevens: http://dirtymonkey.co.uk
.. _MIT License: http://deacalion.mit-license.org
