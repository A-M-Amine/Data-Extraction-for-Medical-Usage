# importation des bibliothèques
import re, sys, urllib.request
from string import ascii_uppercase


corpus = open(sys.argv[1], 'r+', encoding='utf-8')
tmp = open('subst.dic', 'r+', encoding='utf-16')  # sauvgarde de dictionnaire de vidal avant l'enrechissment pour la création de info3.txt
dct = open('subst.dic', 'a+', encoding='utf-16')
dctenri = open('subst_enri.dic', 'w+', encoding='utf-16')

cpt=0     #nb des substances trouvés dans corpus-medical.txt
listCorpus = corpus.readlines()
motERR = ["intraveineuse","posologie","hémoglobine","crp","eau","kt","kcl","nfs"] # liste des mots prie par erreur dans le regex
for line in listCorpus:
    sreg = re.search(r'''^[-*]?\s?(\w+)\s:?\s?(\d+|,|\d+.\d)+\s(mg|ml|µg|mcg|g|cp|amp|flacon).+''', line, re.I)     
    if sreg:        # si une substance est trouvée 
        if sreg.group(1).lower() not in motERR:
            dctenri.write(sreg.group(1).lower()+',.N+subst\n')
            dct.write(sreg.group(1).lower()+',.N+subst\n')      # ecrire la substance dans les 2 dictionnaires
            cpt+=1
            print(str(cpt)+" : "+sreg.group(1))        #affichage des substances avec un compteur
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Tri et suppression des doublons de subst.dic
dct = open('subst.dic', 'r+', encoding='utf-16')
tri = sorted(list(set(dct.readlines())))
dct = open('subst.dic', 'w+', encoding='utf-16')
for el in tri:
    dct.write(el)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Creation et remplissage du fichier info3.txt
info3 = open('info3.txt', 'w+', encoding='utf-8')
dctenri = open('subst_enri.dic', 'r+', encoding='utf-16')
lst = tmp.readlines()
listDctEnri = dctenri.readlines()
nbLettre = 0
for el in listDctEnri:
    if el not in lst:   #verifie l'existence de medicament dans subst génré d'aprés VIDAL
        nbLettre+=1
        info3.write(el)
info3 = open('info3.txt', 'r+', encoding='utf-8')
lst = info3.readlines()
info3 = open('info3.txt', 'w+', encoding='utf-8')
for letter in ascii_uppercase:       #compter le nombre de substances par lettre de l'alphabet
    nbLettre=0
    for i in lst:
        if letter == i[0].upper():
            nbLettre+=1
            info3.write(i)
    info3.write('---------------------------------------------------\n')
    info3.write('Nombre de '+letter+': '+str(nbLettre)+'\n')
    info3.write('---------------------------------------------------\n')
info3.write('Nombre Total: '+str(len(list(set(lst)))))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Creation et remplissage du fichier info2.txt
info2 = open('info2.txt', 'w+', encoding='utf-8')
dctenri = open('subst_enri.dic', 'r+', encoding='utf-16')
listDctEnri = dctenri.readlines()
for letter in ascii_uppercase:       #compter le nombre de substances par lettre de l'alphabet
    nbLettre=0
    for el in list(set(listDctEnri)):
        if letter == el[0].upper():
            nbLettre+=1
            info2.write(el)
    info2.write('---------------------------------------------------\n')
    info2.write('Nombre de '+letter+': '+str(nbLettre)+'\n')
    info2.write('---------------------------------------------------\n')
info2.write('Nombre Total: '+str(len(list(set(listDctEnri)))) + '\n')
