#!/usr/bin/env python3

from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import hashlib


def aes_decry(dic, key):

	key = b64decode(key)
	salt = b64decode(dic['salt'])
	cipher_text = b64decode(dic['cipher_text'])
	nonce = b64decode(dic['nonce'])
	tag = b64decode(dic['tag'])

	#print(nonce)

	private_key = hashlib.scrypt(
		key, salt=salt, n=2**14, r=8, p=1, dklen=32)


	cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

	decrypted = cipher.decrypt_and_verify(cipher_text, tag)

	return decrypted
