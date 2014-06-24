=====================
Game of Thrones Namer
=====================
.. image:: https://travis-ci.org/Matt-Deacalion/Game-of-Thrones-Namer.svg?branch=master
    :target: https://travis-ci.org/Matt-Deacalion/Game-of-Thrones-Namer
    :alt: Build Status
.. image:: https://coveralls.io/repos/Matt-Deacalion/Game-of-Thrones-Namer/badge.png?branch=master
    :target: https://coveralls.io/r/Matt-Deacalion/Game-of-Thrones-Namer?branch=master
    :alt: Test Coverage
.. image:: https://pypip.in/download/game-of-thrones/badge.png?period=week&new
    :target: https://pypi.python.org/pypi/game-of-thrones/
    :alt: Downloads
.. image:: https://pypip.in/version/game-of-thrones/badge.png?new
    :target: https://pypi.python.org/pypi/game-of-thrones/
    :alt: Latest Version
.. image:: https://pypip.in/wheel/game-of-thrones/badge.png
    :target: https://pypi.python.org/pypi/game-of-thrones/
    :alt: Wheel Status
.. image:: https://pypip.in/license/game-of-thrones/badge.png
    :target: https://pypi.python.org/pypi/game-of-thrones/
    :alt: License

Command line tool to generate words that sound like characters from Game of Thrones. Useful for
unique project names, host names and the occasional stray cat.

.. image:: https://raw.githubusercontent.com/Matt-Deacalion/Game-of-Thrones-Namer/screenshots/screenshot.jpg
    :alt: Game of Thrones Namer screenshot

Installation
------------
You can install the *Game of Thrones Namer* using pip:

.. code-block:: bash

    $ pip install game-of-thrones

Usage
-----
You can use the `game-of-thrones` command from the shell to run the Game of Thrones Namer::

    $ game-of-thrones --help

    Generate words that sound like characters from Game of Thrones.

    Usage:
      game-of-thrones [--quantity=<number>] [--min=<length>] [--max=<length>] [--json]
      game-of-thrones (-h | --help | --version)

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
