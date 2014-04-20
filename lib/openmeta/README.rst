pythonic file tagging
==========================

Simple-to-trivial wrapper for OpenMeta_. Rather than re-implementing OpenMeta
using, say, Bob Ippolito's excellent xattr_, I decided to do it by wrapping
the already-functional CLI binary, on advice from those more experienced than
myself who suggested that the pain in getting OpenMeta working as advertised
from the direct xattr business was great and terrible.

Warning - this thing does rely on parsing the output of CLI apps, with the
flakiness and performance troubles that implies. However, it's working
reliably for me.

Usage
-----
    
    >>> import openmeta
    >>> open('./test.txt', 'w').close()
    >>> openmeta.set_tags('./test.txt', ['foo', 'bar'])
    >>> openmeta.get_meta('./test.txt')['tags']
    ['foo', 'bar']
    
TODO
-----

  * more graceful error message when the openmeta CLI binary is not installed
  

Credits
-------

- OpenMeta_
- xattr_

.. _OpenMeta: http://code.google.com/p/openmeta/
.. _xattr: http://undefined.org/python/#xattr
