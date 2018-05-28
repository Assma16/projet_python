
# coding: utf-8

# In[1]:


class joueur:

    """Classe définissant une personne caractérisée par :

    - son nom

    - son score

    - son meilleur score """


    

    def __init__(self): 

        """Constructeur de notre classe. Chaque attribut va être instancié

        avec une valeur par défaut... original"""


        

        self.nom = ""
        self.dernier_score=0

        self.score = 0 

        self.meilleur_score = 0
  


# In[2]:


def verifié (list):
    k=0;
    i=len(list)
    for j in range (i):
        k=list[j]+k;
    if k==1 :
        return 0
    else :
        return 


# In[4]:


def convert(str):
    if len(t)==3:
        z.append(int(t[0]));
        z.append(int(t[2]));
    elif len(t)==4:
        z.append(int(t[0]));
        z.append(int(t[2]));
        z.append(int(t[3]));
        z[1]=z[2]+z[1]*10;
    else :
        print("vous devez entrer une chaine de caractères de la forme ' Numéro du tas' - 'Nombre de pierres à retirer");
    return z


# In[5]:


def affichage (list):
    
    for j in range (len(list)):
        k=j+1;
        print(k,"|",end=''),
        for k in range(list[j]):
            print ("*", end='') 
        for espace in range(23-list[j]):
            print(" ",end='')
        print("|",list[j]);
    


# In[ ]:


import os
import random
joueur1 =joueur 
joueur2 =joueur
joueur1.score=0
joueur2.score=0

joueur1.nom=input("entrez le nom du joueur n°1");
joueur2.nom=input("entrez le nom du joueur n°2");
tas= [];
    
i=random.randrange(3,7);
print("le nombre de tas = ",i)
for j in range (i):
    tas.append(random.randrange(5,23));
affichage(tas)  
tour=1;
while verifié(tas) != 0 :
    if tour%2==0:
        joueur1.score=joueur1.score+1;
    else:
        joueur2.score=joueur2.score +1 ;
    z=[]
    t=input("vous devez entrer une chaine de caractères de la forme ' Numéro du tas' - 'Nombre de pierres à retirer");
    z=convert(t)
    while z[0]-1 not in range(i) or z[1] not in range (tas[z[0]-1]) :
        t=input("le numeros de tas de vous avez choisis  ou le nombre de pierre dans le tas choisis n'existe pas esseyez a nouveau");
        z=convert(t);
        z[0];
    tas[z[0]-1]=tas[z[0]-1]-z[1];
    affichage (tas);
    print ("a l'autre joueur a jouer ");





