#!/bin/bash
VERSION="2.7.9"
PYTHON="Python-$VERSION"
MD5="8d530f7efc373d64a8fb1637e3baaa7 	"
PREFIX="`pwd`/usr"
DOWNLOAD_PREFIX="http://www.python.org/ftp/python/$VERSION"
DOWNLOADDIR="downloads"
mkdir -p $DOWNLOADDIR
cd $DOWNLOADDIR
wget -c $DOWNLOAD_PREFIX/$PYTHON.tar.xz --no-check-certificate
if [ -e "Python-$VERSION.tar.xz" ]; then
echo "Python exits"
fi
echo "*********************************************"
echo "Installing the python-version : $VERSION"
tar xvf $PYTHON.tar.xz
cd $PYTHON
./configure --prefix=$PREFIX --enable-unicode=ucs4
make >  /dev/null
make install  > /dev/null
cd ..
echo
echo "$PYTHON is installed here:"
echo "./usr/bin/python"
echo
wget -c https://pypi.python.org/packages/source/s/setuptools/setuptools-14.0.tar.gz 
wget -c https://pypi.python.org/packages/source/D/Django/Django-1.7.5.tar.gz
tar xvf Django-1.7.5.tar.gz
tar xvf setuptools-14.0.tar.gz
cd setuptools-14.0 && ../../usr/bin/python setup.py install && cd ..
cd Django-1.7.5 && ../../usr/bin/python setup.py install && cd ..
