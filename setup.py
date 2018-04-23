'''
Simple script which creates a python venv, and installs the dependencies.
'''
from setuptools import setup

setup(
    name='pysetup',
    version='0.1',
    description='Simple setup package for dummies.',
    author='Richard Taggart',
    url='https://www.github.com/rwtaggart/pysetup',
    packages=[],
    install_requires=[
        'matplotlib'
    ],
)
