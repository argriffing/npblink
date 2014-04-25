#!/usr/bin/env python
"""
Stochastic mapping on a tree with a specific continuous time Bayesian network.

"""

DOCLINES = __doc__.split('\n')

# This setup script is written according to
# http://docs.python.org/2/distutils/setupscript.html
#
# It is meant to be installed through github using pip.
#
# More stuff was added for cython extensions.

from distutils.core import setup

from distutils.extension import Extension

from Cython.Distutils import build_ext

setup(
        name='npblink',
        version='0.1',
        description=DOCLINES[0],
        author='alex',
        url='https://github.com/argriffing/npblink/',
        download_url='https://github.com/argriffing/npblink/',
        packages=['npblink'],
        test_suite='nose.collector',
        package_data={'npblink' : ['tests/test_*.py']},
        cmdclass={'build_ext' : build_ext},
        ext_modules=[Extension('npblink.hello', ['npblink/hello.pyx'])],
        )

