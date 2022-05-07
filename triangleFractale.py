# Fichier : triangleFractale.py
# Auteur : Mario Sekpona
# Date : 2021-11-29
#
#Cette procédure permet de générer dans codeBoot un triangle équilatéral fractal avec un
# niveau de récursivité.le niveau 0 dessine un triangle plein. Le niveau 1, un triangle, 
#avec 3 sous-triangle pleinet un vide. Le niveau 2, un triangle, avec 3 sous-triangle plein 
#et un vide,où les sous-triangles pleins ont eu le même niveau de composition comme cela vient d'être indiqué.

#Pour exécuter ce code, lancé le serveur web, ouvrir dans le navigateur localhost, 
#glisser et déposer les fichiers géométries et celui-ci.
#Rappel: le serveur et géométrie sont fournis par Marc Feeley.


import geometrie
def fract(cote, niveau):

    if niveau == 0:

        geometrie.trianglePlein(cote)
        
    else:
      
        sqrt3 = math.sqrt(3)
        cote = cote/2
        
        posX =  cote/2
        posY = (sqrt3/6)*cote 

        pu(); rt(90); fd(-posX,-posY); lt(90);pd()
        fract(cote, niveau-1)
        pu(); rt(90); fd(cote,0); lt(90);pd()
        fract(cote, niveau-1)
       
        pu(); lt(30);fd(cote) ; rt(30);pd()
        fract(cote, niveau-1)
        pu();fd(-2*posY); pd()
        #pu(); rt(90); fd(cote,0); lt(90);pd()
        
        
lt(90);fract(200, 10)        
        
        
        
        
          