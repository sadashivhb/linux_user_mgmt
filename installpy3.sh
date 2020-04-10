#!/bin/bash
VERSION="3.8.1"
PYTHON="Python-$VERSION"
MD5="ef7f82485e83c7f8f8bcb920a9c2457b"
PREFIX="`pwd`/usr"
PY_PATH="bin/python3"
DOWNLOAD_PREFIX="http://www.python.org/ftp/python/$VERSION"
DOWNLOADDIR="downloads"
LOGNAME="output.log"
SETUPTOOL_VERSION="40.8.0"
PIP_VERSION="19.0.3"

mkdir -p $DOWNLOADDIR
cd $DOWNLOADDIR
if [ -f $PYTHON.tar.xz ];
then
    echo "*********************************************"
    echo "Python package $PYTHON avalibale locally"
    echo "*********************************************"
else
    echo "*********************************************"
    echo "Started download of $PYTHON"
    wget -c $DOWNLOAD_PREFIX/$PYTHON.tar.xz --no-check-certificate 1>$LOGNAME 2>>$LOGNAME
    echo "Completed download of $PYTHON"
    echo "*********************************************"
fi

#Check the python already exists
VALIDATE_PY_PATH=$PREFIX/$PY_PATH
if [ -f $VALIDATE_PY_PATH ];
then
    echo "*********************************************"
    echo "Python3 already installed in path ---->"
    echo "$PREFIX/bin/python3"
    echo "*********************************************"
else
    echo "*********************************************"
    echo "Installing python-$VERSION"
    tar xf $PYTHON.tar.xz
    cd $PYTHON
    ./configure --prefix=$PREFIX --enable-unicode=ucs4 1>>$LOGNAME 2>>$LOGNAME
    make 1>$LOGNAME
    make install 1>$LOGNAME
    cd ..
    echo "Completed installation for python: $VERSION"
    echo "*********************************************"
fi
echo "$PYTHON is installed here:"
echo "./usr/bin/python3"
echo "*********************************************"

if [ ! -f "setuptools-$SETUPTOOL_VERSION.zip" ];
then
    wget -c https://pypi.python.org/packages/source/s/setuptools/setuptools-$SETUPTOOL_VERSION.zip 1>>$LOGNAME 2>>$LOGNAME 
fi
if [ ! -f "pip-$PIP_VERSION.tar.gz" ];
then
    wget -c https://pypi.python.org/packages/source/p/pip/pip-19.0.3.tar.gz 1>>$LOGNAME 2>>$LOGNAME
fi
unzip -o setuptools-$SETUPTOOL_VERSION.zip 1>>$LOGNAME 2>>$LOGNAME
tar xf pip-$PIP_VERSION.tar.gz
echo "*********************************************"
echo "Started Installing the setuptools and pip"
cd setuptools-$SETUPTOOL_VERSION && ../../usr/bin/python3 setup.py install 1>>$LOGNAME 2>>$LOGNAME && cd ..
cd pip-$PIP_VERSION && ../../usr/bin/python3 setup.py install 1>>$LOGNAME 2>>$LOGNAME && cd ..
echo "Completed Installing the setuptools and pip"
echo "*********************************************"
