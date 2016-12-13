'''
Setup for the aidapy, a thin wrapper for running AIDA more conveniently
within Python.
'''

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aidapy',
    version='0.0.1',
    description='Run AIDA in Python',
    long_description=long_description,
    url='https://github.com/enewe101/aidapy',
    author='Edward Newell',
    author_email='edward.newell@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords= (
		'NLP natrual language processing computational linguistics '
		'AIDA entity linking disambiguation'
	),

    packages=['aidapy']
)
