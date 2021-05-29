#!/usr/bin/env python3

from Crypto.PublicKey import RSA
import binascii

def rsa_encry(aes_key):
	with open('keys/public-key.pem') as f:
		pub_key = RSA.importKey(f.read())

	with open('keys/private-key.pem') as t:
		private_key = RSA.import_key(t.read())


	#print("Valor de n: " + str(pub_key.n) + "\n")
	#print("Valor de e: " + str(pub_key.e) + "\n")

# Computando valor de c

	text = binascii.hexlify(aes_key)
	m = int(text,16)
	c = m ** pub_key.e % pub_key.n

	return c
