#!/usr/bin/env python

from setuptools import setup, find_packages
import os

setup(
    name="tdaemon",
    version="0.1.4",
    maintainer="John Paulett",
    maintainer_email="john@7oars.com",
    description="Test Daemon",
    long_description=open(
        os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url="http://github.com/brunobord/tdaemon",
    license="MIT",
    platforms=['POSIX', 'Windows'],
    py_modules=['tdaemon'],
    keywords=['test', 'testing', 'noestests', 'django', 'py.test'],
    packages=['tdaemon'],
    package_data={'': ['img/button_green.png', 'img/button_red.png'], },
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
    ],
    entry_points={
        'console_scripts': [
            'tdaemon = tdaemon:main',
        ],
    },
)
