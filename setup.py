import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

VERSION = '1.0.0'
DESCRIPTION = "Cookbook app: create, edit, show and filter recipes."

setup(
    name = "cookbook",
    version = VERSION,
    author = "Joshua Schmucker",
    author_email = "joshua.schmucker@gmail.com",
    description = DESCRIPTION,
    license = "GNU GPLv3",
    keywords = ["cookbook", "recpipes", "recipe management"],
    url = "https://github.com/br0uQ/cookbook",
    packages=find_packages(),
    install_requires=[],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: German",
        "Operating System :: Unix",
        "Topic :: Utilities",
    ],
)
