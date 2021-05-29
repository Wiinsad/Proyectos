#!/bin/bash

mkdir keys
cd keys

openssl genrsa -out private-key.pem 2048
openssl rsa -in private-key.pem -pubout -out public-key.pem

python3 -m pip install pycryptodome
python3 -m pip install pycryptodomex

