#!/usr/bin/env python3

import encryRSA
import decryRSA
import encryAES
import decryAES
import sys
import random
import time

def validar(r):
	try:
		temp=int(r)
		return True
	except:
		pass

if __name__ == "__main__":


	print("\nJoker: ¿Te sientes afortunado hoy? Juguemos a mi juego preferido, la ruleta rusa. Si te vuelas la cabeza… ¡Ganas!\nEspera!..... Cumples años hoy? vaya vaya\nTe tengo una sorpresa....")
	num = random.randint(1, 6)
	#print(num)
	with open('cartitas.txt', 'r') as f:
		n = 0
		for i in f:
			n = n+1
			if n == num:
				fel = i
	
	#print(fel)
	#print(type(fel))
	mensEncJ = encryAES.aes_encry(fel)

	#Cifrando en AES

	aesMSG = mensEncJ['cipher_text']
	aesKEY = mensEncJ['key']
	
	time.sleep(2)
	print('\nJoker: Ten tu regalito jejeje')

	regalito = encryRSA.rsa_encry(aesKEY.encode())
	print(regalito)

	blu = True

	while blu == True:

		print("\nQuieres saber que significa? (y, n o exit)")
		res = input("R: ")
	#y = 1
	#n = 2
	#print(r)
	#print(y)
		if res == str('y'):

			print("\nEntonces contesta esta pqueña preguntitaaa....")
			n1 = random.randint(1,50)
			n2 = random.randint(1,50)

			print("\nCuanto es " + str(n1)+ "+" + str(n2)+"?")
			r2 = sys.stdin.readline()
			#print(r2)

			if validar(r2):
				print("\nMuy muy bien!!")
				regalo2 = int(input("Ingresa tu regalo:\n"))

				if validar(regalo2):
					if int(regalo2) == regalito:
						print("\nVeamos que dicee!..")
						cart = decryRSA.rsa_decry(int(regalo2))
						cartD = decryAES.aes_decry(mensEncJ,cart).decode()
						print(cartD)
					else:
						print("\nUyy casi casi")
				else:
					print("\nNop Nop Ese no es.....\n")
			else:
				print("\nCasi.....")



			break

		elif res == str('n'):

			print("\nTu te lo pierdes!!\n**BOOOM** **Explota algo**....")
			break
		elif res == str('exit'):
			print("\nTu te lo pierdes!!\n**BOOOM** **Explota algo**....")
			break
		else:

			print("\nMal maal mala respuesta, responde a lo que te digo bien:)")
			pass

	#decryAES.aes_decry()
