import random

# version récursive
def checkTypeEntreeUtil(message):
	try:
		return(int(input(message)))
	except Exception:
		print('Attention, entiers uniquement autorisés')
		return checkTypeEntreeUtil(message)
 
# # version itérative
# def checkTypeEntreeUtil(message,a):
# 	while True:
# 		try:
# 			return(int(input(message)))
# 		except Exception:
# 			print('Attention, entiers uniquement autorisés')
 
# version récursive		
def checkBoundariesEntreeUtil(message,bB,bH):
	value=checkTypeEntreeUtil(message)
	if value<bB or value>bH :
		print('Attention, entiers entre '+bB+' et '+bH+' uniquement')
		value=checkBoundariesEntreeUtil(message,bB,bH)
	return value
 
 
# # version itérative
# def checkBoundariesEntreeUtil(message,bB,bH,a):
# 	value=checkTypeEntreeUtil(message)
# 	if value<bB or value>bH :
# 		print('Attention, entiers entre '+bB+' et '+bH+' uniquement')
# 		value=checkTypeEntreeUtil(message)
# 	return value
 
 
def plusOuMoins():
	difficulte=checkBoundariesEntreeUtil('Choisissez la difficulte : (1) facile, (2) moyenne, (3) difficile',1,3)
	# version codeur savy
	borneMax=10**difficulte
	# version bourrin
	#if difficulte==1:
	#	borneMax=10
	#elif difficulte==2:
	#	borneMax=100
	#elif difficulte==3:
	#	borneMax=1000
	nbTrouve=random.randint(1,100)
	proposition=nbTrouve+1
	compteur=0
	while proposition!=nbTrouve:
		proposition=checkBoundariesEntreeUtil('Quel nombre ai-je choisi?\n',0,borneMax)
		compteur+=1
		if proposition<nbTrouve:
			print('c\'est +')
		elif proposition>nbTrouve:
			print('c\'est -')
 
	print('TROUVE! En '+str(compteur)+' coup'+'s'*(compteur>1))
 
def main():
	plusOuMoins()
 
if __name__=='__main__':
	main()