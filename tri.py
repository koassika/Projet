#!/bin/env python3
import sys, re, getliste

"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.

    Ce programme lit des liste de type L sur l'entrÃ©e standard, au format
    [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
    et sort cette liste dans laquelle les sous-listes d'entiers sont triÃ©es.  
"""

def tri(l):
    """
    Cette fonction rÃ©cursive tri la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)


if __name__=="__main__":
    # programme principal
    if len(sys.argv)==1:
		while True:
			line = input("? ").rstrip("\n").strip()
			if line=="":
				break
			getliste.lline = re.split(r' +',line.rstrip("\n"))
			getliste.i = 0
			l = getliste.mklist()                      # rÃ©cupÃ©ration de la liste

			
    elif len(sys.argv)==2:
		f = open("listes.txt", "r")
		for line in f:
			lline = re.split(r' +',line.rstrip("\n"))
			l = getliste.build(lline)                     
			
	else:
		i = 1                              # indice pour parcourir les arguments
		l = getliste.construire()                   # rÃ©cupÃ©ration de la liste
		
	tri(l)
	print(f"{l=}")
	
	
