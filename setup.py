#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Absolute Performance Inc <csteam@absolute-performance.com>.

from setuptools import setup

with open('README.rst', 'r') as file:
    long_description = file.read()

setup(
    name='ucbreq',
    version='1.0.0',
    description='Simple format for serialization, similar to CSV.  Not useful for most general use.',
    long_description=long_description,
    author='Taylor C. Richberger',
    author_email='tcr@absolute-performance.com',
    url='https://github.com/absperf/python-req',
    license='MIT',
    py_modules=[
        'ucbreq',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
)
