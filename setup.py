from distutils.core import setup
from setuptools import find_packages

setup (
    name='SWUAPI',
    version='0.1',
    author='Matt Harris',
    author_email='matt@sendwithus.com',
    packages=find_packages(),
    scripts=['bin/swuapi.py',],
    url='http://pypi.python.org/pypi/SWUAPI/',
    license='LICENSE.txt',
    description='Python API client for sendwithus.com',
    long_description=open('README.txt').read()
)
