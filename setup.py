import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "adpil",
    version = "1.01",
    author = "RCM",
    author_email = "rubens.campos.machado@gmail.com",
    description = ("Interface between Adessowiki and PIL."
                                   "Used by ia636 and ia870 toolboxes."),
    license = "BSD 3 clauses",
    keywords = "PIL",
    url = "https://github.com/robertoalotufo/adpil",
    packages=['adpil'],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: BSD License",
    ],
)