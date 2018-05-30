
# coding: utf-8

# In[1]:
class joueur:#une structure joueur

    def __init__(self): 

      
        self.nom = ""
        self.dernier_score=0
        self.meilleur_score = 0

# In[2]:


def verifié (list):#verifié si ona arriver a la fin du jeu ou pas encors
    k=0;
    i=len(list)
    for j in range (i):
        k=list[j]+k;
    if k==1 :
        return 0
    else :
        return 1 

# In[3]:


def convert(str):#convertir le chaine en une liste d'entier naturel
    z=[]
    if len(t)==3:
        z.append(int(str[0]));
        z.append(int(str[2]));
    elif len(t)==4:
        z.append(int(str[0]));
        z.append(int(str[2]));
        z.append(int(str[3]));
        z[1]=z[2]+z[1]*10;
    else :
        print("vous devez entrer une chaine de caractères de la forme ' Numéro du tas' - 'Nombre de pierres à retirer");
    return z


# In[4]:


def affichage (list):#afficher l'etat du jeux
    
    for j in range (len(list)):
        
        print(j+1,"|",end=''),
        for k in range(list[j]):
            print ("*", end='') 
        for espace in range(23-list[j]):
            print(" ",end='')
        print("|",list[j]);
    


# In[5]:


def Score(tour):#compter le score a chaque tour
    t=0
    for i in range(m.ceil(tour/2)): 
        t+=i*(10**i)
    return t


# In[12]:


def setup():#enregistrer les données
    
    global joueur1
    global joueur2
    
    
    
    joueur1.nom,joueur2.nom=("A déterminer","A déterminer")
    joueur1.dernier_score,joueur2.dernier_score,joueur1.meilleur_score,joueur2.meilleur_score=0,0,0,0
    joueu1=input("Joueur 1 entrez votre nom: ")
    joueu2=input("Joueur 2 entrez votre nom: ")
    with open("save.txt",'r') as save:
        for ligne in save:
            if ligne.split(':')[0]==joueur1.nom:
                joueur1.nom,joueur1.dernier_score,joueur1.meilleur_score=ligne.strip('\n').split(':')
                
            if ligne.split(':')[0]==joueur2:
                joueur2.nom,joueur2.dernier_score,joueur2.meilleur_score=ligne.strip('\n').split(':')
                
    if joueur1.nom=="A déterminer":
        joueur1.nom=joueu1
    if joueur2.nom=="A déterminer":
        joueur2.nom=joueu2


# In[15]:


import os
import random
joueur1 =joueur 
joueur2 =joueur
joueur1.score=0
joueur2.score=0
x=joueur
setup()
print("Joueur1:",joueur1.nom,"| Score partie précédente:",joueur1.dernier_score,"| Meilleur Score:",joueur1.meuilleur_score)
print("Joueur2:",joueur2.nom,"| Score partie précédente:",joueur2.dernier_score,"| Meilleur Score:",joueur2.meuilleur_score)


tas= [];
    
i=random.randrange(3,7);
print("le nombre de tas = ",i)
for j in range (i):
    tas.append(random.randrange(5,23));
affichage(tas)  
tour=1;
while verifié(tas) !=0 :
    if tour%2==0:
        joueur2.score=joueur2.score+1;
        print("Au tour de",joueur2.nom)
        x=joueur1;
    else:
        joueur1.score=joueur1.score +1 ;
        print("Au tour de",joueur1.nom)
        x=joueur2;
        
    z=[]

      
    t=input("vous devez entrer une chaine de caractères de la forme ' Numéro du tas' - 'Nombre de pierres à retirer");
    z=convert(t)
    print(z)
    while z[0] not in range(i) or z[1] not in range(tas[z[0]]) :
        t=input("le numeros de tas de vous avez choisis  ou le nombre de pierre dans le tas choisis n'existe pas esseyez a nouveau");
        z=convert(t);
    tas[z[0]-1]=tas[z[0]-1]-z[1];
    affichage (tas);
    tour=tour+1;
    score=calculScore(tour)
    f = open("save.txt","r")
    lignes = f.readlines()
    f.close()

    
    print ("a l'autre joueur de jouer ");
if x==joueur1:
    x==joueur2
    
else :
    x==joueur1
    
print ("le joueur ",x.nom,"vous avez perdus");

