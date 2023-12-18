#!/usr/bin/env bash

SCRIPT_PATH=`cd \`dirname $BASH_SOURCE\`; pwd`
cd "$SCRIPT_PATH/.."
export LOCAL_PATH=$(pwd)

OS=`uname -s`

case "$OS" in
	"Darwin"*)
		echo "Enabling OSX specific flags."
		export CFLAGS=-Qunused-arguments
		export CPPFLAGS=-Qunused-arguments
		
		env PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs2 --enable-framework" arch -x86_64 pyenv install -s 3.8.5
		pyenv local 3.8.5
		eval "$(pyenv init --path)"
		rm -rf venv
		python3 -m venv venv
		;;
	"Linux")
		echo "Enabling Linux specific flags."
		;;
	*)
		;;
esac

source ./venv/bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt
