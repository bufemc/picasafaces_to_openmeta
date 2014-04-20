from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.1dev'

install_requires = [
    # This project requires the openmeta CLI binary from
    # http://code.google.com/p/openmeta/
]


setup(name='openmeta',
    version=version,
    description="Trivial wrapper providing tidy python access to the openmeta command-line client to set OS X openmeta tags on files",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      "Environment :: MacOS X",
      "Topic :: System :: Filesystems",
      "Operating System :: MacOS :: MacOS X",
      "License :: OSI Approved :: BSD License",
    ],
    keywords='metadata',
    author='Dan MacKinlay',
    author_email='pypi@email.possumpalace.orgg',
    url='https://bitbucket.org/howthebodyworks/openmeta/src',
    license='BSD',
    py_modules=['openmeta'],
)
