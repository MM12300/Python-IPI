#!/bin/python3
# -*- conding: utf-8 -*-

"""
--------------------
 TD: nombre mystère
--------------------
"""

from random import randint
from time import sleep
import stdiomask

def dispMenu():
	menu = [
		"0. Noob\t\t\t[0-1]",
		"1. Facile\t\t[0-10]",
		"2. Normal\t\t[0-100]",
		"3. Difficile\t\t[0-1000]",
		"4. Hardcore\t\t[0-10000]",
		"5. Cauchemardesque\t[0-100000]",
		"6. ROXOR\t\t[0-1000000]",
	]

	print("\nChoisit le niveau de difficulté:")

	for item in menu:
		print(item)
		sleep(.01)

	print("\n99. Exit")

	return(len(menu) - 1)

def multiPlayer():
	answer = input("Tu veux jouer avec un pote ou pas ? (Yes/No)\n> ")
	return True if(answer in ("y", "Y", "Yes")) else False

def playerName():
	print("Entrer vos noms les fifous")

	return [
		input("Player 1: "),
		input("Player 2: ")
	]

def game(max, multi):
	player = playerName
	M = randint(0, max)
	N = -1
	i = 1

	while(N != M):
		try:
			showPlayer = i%2 if(multi) else 0
			msgInput = "\n{}, entre un nombre !\n> ".format(player[showPlayer])
			N = int(stdiomask.getpass(prompt = msgInput)) if(multi) else int(input(msgInput))
			print("C'est imense") if(N > M) else print("C'est rikiki")
			i += 1

		except Exception:
			print("On a dit un nombre idiot !")

	print("\nGG WP {} !".format(player[showPlayer]))
	print("T'as tout de même fait {} Essaie(s)".format(i))

def retry():
	answer = input("On s'en refait une ? (Yes/No)\n> ")

	if(answer in ("y", "Y", "Yes")):
		dispMenu()
		return True

	else:
		return False

def main():
	diffCount = dispMenu()

	while(True):
		try:
			diff = int(input("\n> "))

			if((diff >= 0) and (diff <= diffCount)):
				game(10**diff, multiPlayer())

				if not(retry()):
					break

			elif(diff == 99):
				break

			else:
				print("T'es un p'tit mâlin toi dit donc !")

		except Exception:
			print("Pas de carabistouille enfoirée !")

if(__name__ == '__main__'):
	playerName = playerName()
	main()
	print("Bye kheyou !")
