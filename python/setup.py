#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages
from mt.struct.version import VERSION

setup(
    name='mtstruct',
    version=VERSION,
    description="Minh-Tri's C/C++ structures that can be useful for Python.",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=['mt.*']),
    package_data={
        'mt.struct': ['*.pyx', '*.pyxbld', '*.pxd', 'cpp/wordtrie.*'],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'mtbase>=0.4.0',  # Minh-Tri's base modules for logging and multi-threading
        # You need Boost.Serialization as well but only at run time.
    ],
    url='https://github.com/inteplus/mtstruct',
    project_urls={
        'Documentation': 'https://mtstruct.readthedocs.io/en/stable/',
        'Source Code': 'https://github.com/inteplus/mtstruct',
    }
)
