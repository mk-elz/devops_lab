#!/bin/bash

sudo yum install -y libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel \
wget curl llvm ncurses-devel openssl-devel lzma-sdk-devel redhat-rpm-config

curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash


if ! grep pyenv ~/.bashrc
then
echo 'export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
' >> ~/.bashrc
fi

source  ~/.bashrc

pyenv install  2.7.17
pyenv install  3.7.5

pyenv global 3.7.5


pyenv virtualenv 2.7.17env
pyenv virtualenv 3.7.5env

pyenv local 3.7.5env


