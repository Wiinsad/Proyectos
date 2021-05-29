#!/usr/bin/env python3

from Crypto.PublicKey import RSA
import binascii
from Crypto.Util.number import *

def rsa_decry(cipher_key):

	with open('keys/public-key.pem') as f:
		pub_key = RSA.import_key(f.read())

	with open('keys/private-key.pem') as t:
		priv_key = RSA.import_key(t.read())

	text = pow(cipher_key,priv_key.d,pub_key.n)
	plaint = long_to_bytes(text).decode()

	return plaint 
