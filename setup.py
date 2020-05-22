from setuptools import setup, find_packages
import glob

setup(
   name='1upcoder',
   version='0.0',
   description='a series of small projects',
   author='1upcoder',
   author_email='1upcoder@gmail.com',
   packages=find_packages(),
   test_suite='pytest',
   install_requires=['pytest',
                     'gspread',
                     'oauth2client',
                     'simplejson',
                     'flake8'],
   scripts=[f for f in glob.glob('youtube/*')]
)
