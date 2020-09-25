#!/bin/env python3
import sys , getliste

"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  

    Ce programme est appelÃ© avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.  

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit Ãªtre fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""

def minmax(l):
    """
    Cette fonction rÃ©cursive retourne le minmax de la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

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
		

    
    
    
    maxi = []
    minmax(l)
    print(min(maxi))
