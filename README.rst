=====================
Game of Thrones Namer
=====================

Command line tool to generate words that sound like characters from Game of Thrones. Useful for
unique project names, host names and the occasional stray cat.

Installation
------------
You can install the *Game of Thrones Namer* using pip::

    $ pip install game-of-thrones

Usage
-----
You can use the `game-of-thrones` command from the shell to run the Game of Thrones Namer::

    $ game-of-thrones --help

    Generate words that sound like characters from Game of Thrones.

    Usage:
      game-of-thrones [--quantity=<number>] [--min=<length>] [--max=<length>]
      game-of-thrones (-h | --help | --version)

    Options:
      --version                show program's version number and exit.
      -h, --help               show this help message and exit.
      -q, --quantity=<number>  the quantity of words to generate [default: 10].
      --min=<length>           the minimum length of each word [default: 4].
      --max=<length>           the maximum length of each word [default: 10].

License
-------
Copyright © 2014 `Matt Deacalion Stevens`_, released under The `MIT License`_.

.. _Matt Deacalion Stevens: http://dirtymonkey.co.uk
.. _MIT License: http://deacalion.mit-license.org
