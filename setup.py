from setuptools import setup
import glob
from os.path import isdir, exists, join


def package_filter(filename):
    return isdir(filename) and exists(join(filename, '__init__.py'))


setup(
   name='1upcoder',
   version='0.0',
   description='a series of small projects',
   author='1upcoder',
   author_email='1upcoder@gmail.com',
   packages=list(filter(package_filter, glob.glob('*'))),
   install_requires=['pytest', 'gspread', 'oauth2client', 'simplejson'], #external packages as dependencies
)
