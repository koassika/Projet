#!/bin/env python3
import sys

i=1
"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  

    Ce programme est appelÃ© avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.  

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit Ãªtre fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""

def construire():
    """
    Cette fonction rÃ©cursive construit la liste 
    Ã  partir des arguments fournis sur la ligne de commande.
    Elle retourne la liste construite.
    """
	
    global i  
    l = []          
    while True:
        if sys.argv[i]=="[":   
            i+=1               
            if i!=2:                  # pour la premiÃ¨re liste, on ne fait rien
                l.append(construire()) 
        elif sys.argv[i]=="]":        # c'est la fin de la liste,
            i+=1
            return l                  # on renvoie la liste constuite
        else:                         # c'est une liste d'entiers
            l.append(int(sys.argv[i]))   
            i+=1

def build(l0):
    """
    Cette fonction construit la liste correspondant Ã  sa reprÃ©sentation chaine de caractÃ¨re fourni en argument.
    """

    def _build():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la premiÃ¨re sous-liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    res = _build()
    return res
   
def mklist():
    global i
    l = []          # liste courante
    while True:
        if lline[i]=="[":   # c'est une liste de listes
            i+=1                 # argument suivant
            if i!=1:             # pour la premiÃ¨re liste, on ne fait rien
                l.append(mklist())    # sinon on construit cette sous-liste et on la met dans la liste courante
        elif lline[i]=="]": # c'est la fin de la liste,
            i+=1
            return l             # on renvoie la liste courante
        else:                  # c'est une liste d'entiers
            l.append(int(lline[i]))   
            i+=1
           
            
            
            
            
            
