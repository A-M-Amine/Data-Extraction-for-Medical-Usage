# AHMANE Mohamed Amine
# AZOUZ Mohamed Souhib 

# importation des bibliothèques 
import urllib.request, re, sys, os
from http import server, HTTPStatus
from string import ascii_uppercase

info = open('info.txt', 'w+', encoding='utf-8')
substdct = open('subst.dic', 'w+', encoding='utf-16')
arg1 = sys.argv[1].upper()       #intervalle
port = sys.argv[2]          #port
nbtotal=0 # compteur
if re.match(r'[A-Z]-[A-Z]', arg1):
    for c in ascii_uppercase:
        if c>=arg1[0] and c<=arg1[2]:
            url = urllib.request.urlopen('http://localhost:'+port+'/vidal-Sommaires-Substances-'+c+'.htm')
            res = url.read().decode('utf-8')
            fin = re.findall(r'href="Substance/.*-.*.htm">(\w*)', res)
            inf = ",.N+subst\n".join(fin)
            for line in inf:
                substdct.write(line)
            info.write("Nombre de "+c+": "+str(len(fin))+"\n")
            nbtotal+=len(fin)
    info.write("Nombre Total: "+str(nbtotal))
else:
    print("Error")
