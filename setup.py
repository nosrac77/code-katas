"""This file contains the setup necessary to run tox."""

from setuptools import setup

setup(
    name='Day of Code',
    description='This module contains Code Wars tests, functions, and best practices.',
    author='Carson',
    author_email='carson.newton@outlook.com',
    package_dir={'': 'src'},
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'tox']},
)
