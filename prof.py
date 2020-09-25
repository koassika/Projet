#!/bin/env python3
import sys, re, getliste

"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.
    Ce programme est appelÃ© avec le nom d'un fichier sur la ligne de commande,
    ce fichier contenant des listes de type L.
    Il sort la profondeur de chaque liste.
"""


def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passÃ©e en argument.
    """

    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

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
		
    print(f"{l=}")
	print(f"{profondeur(l)=}")
