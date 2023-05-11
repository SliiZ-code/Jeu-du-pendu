from random import randint  # Importations
from dessin_pendu import dessinpendu  # Des
import pandas  #
import time  # Modules
import re  # Nécessaires

datamot = pandas.read_csv("liste_francais_22k.txt")  # Lecture de la liste de mots
datascore = pandas.read_csv("score.csv")  # Lecture du tableau des scores
datamot2 = datamot.loc[(datamot.mot.str.contains('!', regex=True) == False)]  # Traitement
datamot3 = datamot2.loc[(datamot2.mot.str.contains(' ', regex=True) == False)]  # Des
datamot4 = datamot3.loc[(datamot3.mot.str.contains('^[a-z]', regex=True) == True)]  # Mots
datamot5 = datamot4.loc[(datamot4.mot.apply(len)) > 4]  # Utilisés
datamot6 = datamot5.reset_index()


def choix_mot():  # Fonction qui choisit un mot dans la liste en le renvoie sans majuscule

    mot = datamot6.loc[randint(0, len(datamot6)), "mot"]
    return mot.lower()


def mot_mystere(mot):  # Fonction qui transforme un mot en une suite de '_ '
    myst = ''
    for i in range(len(mot)):
        if mot[i] == '-':
            myst = myst + '- '
        else:
            myst = myst + '_ '

    return myst


def verification(lettre, mot):  # Fonction booléene qui vérifie l'apparition d'une lettre dans un mot
    return lettre in mot


def completer_mot(lettre, mot, myst):  # Fonction qui complète le 'mot_mystere' d'un mot par la lettre donnée
    motmyst = ''
    for i in range(len(mot)):

        if lettre == mot[i]:
            motmyst = motmyst + lettre + ' '

        else:
            motmyst = motmyst + myst[i * 2] + ' '

    return motmyst


def jeu():  # Fonction qui permet de lancer le jeu
    global score
    print('''             --------------Haut de la console visible---------------



































Avant de commencer, veuillez vous assurez que la console est correctement redimensionner jusqu'au pointillés.''')
    pret = input('Etes-vous prêt ? (Y/N)')
    while not pret.lower() == 'y':
        time.sleep(4)
        pret = input('Etes-vous prêt ? (Y/N)')
    nom = input('Entrez votre prénom')
    lettreu = []
    print('Choisir un mode de jeu')
    print('Choisir une difficulté')
    mode = input("C : Mode classique   ou   M : Mort Subite")  # Choix du mode
    while not mode.lower() == 'c' and mode.lower() != 'm':
        print('Choix du mode incorrect')
        mode = input("C : Mode classique   ou   M : Mort Subite")
    if mode.lower() == 'c':
        difficultéchoisi = int(input("1.Facile 2.Intermédiaire 3.Difficile"))  # Choix de la difficulté (1,2,3)
        nivdifficulte = [10, 7, 5]  # Configuration
        tentatives = nivdifficulte[difficultéchoisi - 1]  # Du mode
        mot = difficulté(difficultéchoisi)  # Classique
    else:
        print("Mort Subite activée !")  # Configuration
        mot = choix_mot()  # Du
        tentatives = 10  # Mode
        ratingtotal = 0  # Mort
        chainemots = ''  # Subite
    myst = mot_mystere(mot)
    resultat = myst
    motfinal = ''
    for i in range(len(mot)):
        motfinal = motfinal + mot[i] + ' '
    for i in range(6):
        print('   ' * 30)
    dessinpendu(tentatives)  # Affichage du pendu
    print('Nombres de tentatives restantes :', tentatives)  # Affichage du nombre de tentatives initiales
    print(resultat)  # Affichage de la progression
    print('   ' * 30)
    print('   ' * 30)

    while tentatives > 0:  # Boucle de jeu

        l = input('===> Veuillez choisir un lettre...')  # Choix d'une lettre
        if l.isalpha() == True:
            lettre = l.lower()
            if len(lettre) > 1:
                print("Veuillez ne choisir qu'une seule lettre")
            else:
                resultat = completer_mot(lettre, mot, resultat)  # Complétion du résultat avec la lettre choisi
                if verification(lettre, mot) == True:
                    for i in range(6):
                        print('   ' * 30)
                    dessinpendu(tentatives)
                    print('Nombres de tentatives restantes :', tentatives)
                    if len(lettreu) > 0:
                        print("Liste des lettres non présentes dans le mot",
                              lettreu)  # Affichage des lettres déjà utilisés
                    print(resultat)
                    print('   ' * 30)
                    print('   ' * 30)
                    if motfinal == resultat:  # Vérification de victoire
                        if mode.lower() == 'c':  # Fin en mode classique
                            print('Bravo, vous avez gagné!')
                            print('Votre mot avait un niveau de difficulté évalué à : ', ratingfinal(mot), ' sur 10')
                            print('Voici les meilleurs scores')
                            print(score(nom, mot, ratingfinal(
                                mot)))  # Ajout du score au tableau et affichage des meilleurs scores
                            break
                        else:  # Passage au mot suivant lors de la Mort Subite
                            print('Bravo, passons au mot suivant !')
                            print('Votre mot avait un niveau de difficulté évalué à : ', ratingfinal(mot), ' sur 10')
                            ratingtotal += ratingfinal(mot)  # Ajout de la note du mot à la note totale
                            chainemots += mot + ' (' + str(ratingfinal(
                                mot)) + ') - '  # Ajout du mot et de la note à la chaîne totale pour l'utiliser dans le score plus tard
                            nvmot = choix_mot()  # Choix d'un
                            while rating(nvmot) < rating(mot):  # Nouveau mot
                                nvmot = choix_mot()  # Plus difficile que
                            mot = nvmot  # Le précédent
                            myst = mot_mystere(mot)  #
                            resultat = myst  # Reconfiguration
                            motfinal = ''  #
                            for i in range(len(mot)):
                                motfinal = motfinal + mot[i] + ' '
                            for i in range(6):
                                print('   ' * 30)
                            tentatives += 2  # Ajout de 2 tentatives lors d'un mot trouvé
                            if tentatives > 10:  # Sans dépasser 10 tentatives
                                tentatives = 10
                            dessinpendu(tentatives)
                            print('Nombres de tentatives restantes :', tentatives)
                            print(resultat)
                            print('   ' * 30)
                            print('   ' * 30)
                            lettreu = []  # Réinisialisation des lettres utilisés
                else:
                    for i in range(6):
                        print('   ' * 30)
                    if lettre in lettreu:
                        tentatives = tentatives
                    else:
                        tentatives = tentatives - 1  # Réduction d'une tentaive lors d'une mauvaise lettre donnée
                        lettreu.append(lettre)  # Et ajout dans la liste des lettres utilisés
                    dessinpendu(tentatives)
                    print('Nombres de tentatives restantes :', tentatives)
                    print("Liste des lettres non présentes dans le mot", lettreu)
                    print(resultat)
                    print('   ' * 30)
                    print('   ' * 30)
                    if tentatives == 0:  # Boucle de fin
                        if mode.lower() == 'c' or ratingtotal == 0:  # Fin du mot classique ou si aucun mot n'a été trouvé
                            dessinpendu(tentatives)
                            print('Perdu, le mot était :', mot)
                            print('Votre mot avait un niveau de difficulté évalué à : ', ratingfinal(mot), ' sur 10')
                            print('Voici les meilleurs scores')
                            scoretrie = datascore.sort_values(by=["rating"], ascending=False)  # Affichage
                            score = scoretrie.reset_index(drop=True)  # des 5 premiers
                            print(score.iloc[:5])  # scores triés
                            print("Consultez le table 'score.csv' pour plus de détails")
                        else:  # Fin de la Mort Subite
                            dessinpendu(tentatives)
                            print('Terminé, le dernier mot était :', mot)
                            print('Votre score total est de : ', ratingtotal)
                            print('Voici les meilleurs scores')
                            print(score(nom, chainemots[:-3],
                                        ratingtotal))  # Ajout du score final au tableau et affichage des meilleurs scores
                            print("Consultez le table 'score.csv' pour plus de détails")
        else:
            print("Ceci n'est pas une lettres")
            print('Nombres de tentatives restantes :', tentatives)
            print("Liste des lettres non présentes dans le mot", lettreu)
            print(resultat)


def ratingliste():  # Fonction qui renvoie le mot de la liste ayant la meilleure note
    meilleurmot = ''
    for i in range(len(datamot6)):
        if rating(datamot6.loc[i, "mot"]) > rating(meilleurmot):
            meilleurmot = datamot6.loc[i, "mot"]
    return meilleurmot


def rating(mot):  # Fonction qui applique un score à un mot en fonction de ses caractères
    llettres = []
    for lettre in mot:
        if lettre not in llettres:
            llettres.append(lettre)
    score = 0
    voyelle = ['a', 'e', 'i', 'o', 'u']
    lfrequentes = ['s', 'n', 'r', 't', 'a', 'e', 'i']
    lrares = ['z', 'w', 'k', 'j', 'x', 'q', 'y', 'h']
    for lettre in llettres:
        score += 1.5
        if lettre in voyelle:
            score += 1
        if lettre in lfrequentes:
            score += 4
        if lettre in lrares:
            score += 8
    lettresdoubles = len(mot) - len(llettres)
    score -= 2 * lettresdoubles

    return score


def ratingfinal(mot):  # Fonction qui équilibre les notes des mots sur 10 par rapport au meilleur mot trouvé
    return round(rating(mot) / (rating(ratingliste()) / 10), 1)


def difficulté(difficultéchoisi):  # Fonction qui renvoie un mot en adéquation avec la difficulté choisi :(1,2,3)
    meilleurmot = ratingliste()
    ratingdifficulte = [4, 7, 10]
    mot = choix_mot()
    supa = ratingdifficulte[difficultéchoisi - 2]
    if supa == 10:
        supa = 0
    infa = ratingdifficulte[difficultéchoisi - 1]
    while not supa < round(rating(mot) / (rating(meilleurmot) / 10), 1) < infa:
        mot = choix_mot()

    return mot


def score(nom, mot,
          rating):  # Fonction qui ajoute le nom du joueur et le.s mot.s trouvé.s et son/leur rating dans un tableau et le renvoie trié en affichant les 5 premiers
    global datascore
    dscore = {'nom': [nom], 'rating': [rating],
              'mot': [mot]}  # Création d'un dictionnaire qui contient les informations
    dfscore = pandas.DataFrame.from_dict(dscore)  # Transformation du dictionnaire en DataFrame
    dfscore.to_csv('score.csv', mode='a', header=False, index=False)  # Ajout du DataFrame au fichier 'score.csv'
    datascore = pandas.read_csv("score.csv")  # Lecture du fichier
    scoretrie = datascore.sort_values(by=["rating"], ascending=False)  # Triage par ordre décroissant du score
    score = scoretrie.reset_index(drop=True)  # Réinisialisation des index
    return score.iloc[:5]  # Affichage des 5 plus hauts scores

jeu()