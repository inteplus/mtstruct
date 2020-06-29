Installation
============

C++
---

Use cmake to build and install::

    git clone https://github.com/inteplus/mtstruct.git
    cd mtstruct/cpp
    mkdir build
    cd build
    cmake ..
    make
    make install

Python
------

The Python version includes the C++ source and include files in the Python package. When you import `mt.struct`, Python extensions are compiled using pyximport. Currently, we require `Boost.Serialization` installed at run time.

Install via pip::

    pip3 install mtstruct

Build from source::

    git clone https://github.com/inteplus/mtstruct.git
    cd mtstruct/python
    python3 setup.py install
