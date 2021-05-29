#!/usr/bin/env python3

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode
import binascii
import hashlib
import random

def aes_encry(plain_text):
	#print(str(randkey))
	key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16)).encode('utf-8')

	salt = get_random_bytes(AES.block_size)
	private_key = hashlib.scrypt(
	key, salt=salt, n=2**14, r=8, p=1, dklen=32)

	cipher_config = AES.new(private_key, AES.MODE_GCM)

	cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text,'UTF-8'))	
	#print(cipher_config)
	#print(b64encode(cipher_config.no))
	return {
		'cipher_text': b64encode(cipher_text).decode('utf-8'),
		'key': b64encode(key).decode('utf-8'),
		'salt': b64encode(salt).decode('utf-8'),
		'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
		'tag': b64encode(tag).decode('utf-8')
	}
