#!/usr/bin/env python3

import sys
import os.path as op
from setuptools import setup, find_namespace_packages, Extension
from Cython.Build import cythonize
from mt.struct.version import VERSION

sys.path.append(op.join(op.dirname(__file__), 'mt', 'struct'))

extensions = [
    Extension(
        name="mt.struct.trie",
        sources=["mt/struct/trie.pyx", "../cpp/wordtrie.cpp"],
        include_dirs=["../cpp/", "mt/struct"],
    )
]

setup(
    name='mtstruct',
    version=VERSION,
    description="Minh-Tri's C/C++ structures that can be useful for Python.",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=['mt.*']),
    ext_modules=cythonize(extensions),
    package_data={
        'mt.struct': ['*.pyx', '*.pxd'],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'mtbase>=0.4.1',  # Minh-Tri's base modules for logging and multi-threading
        'numpy',
        # You need Boost.Serialization as well but only at run time.
    ],
    url='https://github.com/inteplus/mtstruct',
    project_urls={
        'Documentation': 'https://mtdoc.readthedocs.io/en/latest/mt.struct/mt.struct.html',
        'Source Code': 'https://github.com/inteplus/mtstruct',
    }
)
