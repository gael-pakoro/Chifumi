import random
print("\n*****************************************")
print("************Jeux mystérieux**************")
print("*****************************************\n")
while True:
    max_points = 3
    choix = ["pierre","feuille","ciseaux"]
    tes_points= 0
    points_bot = 0


    while tes_points < max_points and points_bot < max_points:
        print("*****************************************")
        print("OK!!")
        print("PIERRE...FEUILLE...CISEAUX!!")
        ton_choix= input("choisis entre pierre/feuille/ciseaux: ")
        choix_bot = random.choice(choix)
        if choix_bot == "feuille":
            if ton_choix == "ciseaux":
                tes_points+=1
                print("J'ai prit la feuille!!")
                print("Tu es trop fort BG. Le ciseaux coupe la feuille. ")
                print(f"Tu as maintenant {tes_points} points.\n")
                print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
            else:
                if ton_choix == "pierre":
                    points_bot += 1
                    print("J'ai prit la feuille!!")
                    print("J'ai gagné. Le papier recouvre la pierre. :(")
                    print(f"J'ai mainteant {points_bot} points.\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
                elif ton_choix == "feuille":
                    print("J'ai prit la feuille!!")
                    print("On a le même, match nul mec.\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
                else:
                    print("J'ai prit la feuille!!")
                    print("C'est quoi cette merde?? C'est même pas dans le nom du jeux.\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
        elif choix_bot == "pierre":
            if ton_choix == "feuille":
                tes_points+=1
                print("J'ai prit la Pierre!!")
                print("Tu as gagné. La feuille recouvre la pierre.")
                print(f"tu as maintenant {tes_points} points.\n")
                print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
            else:
                if ton_choix == "ciseaux":
                    points_bot += 1
                    print("J'ai prit la Pierre!!")
                    print("J'ai gagné!!! La pierre écrase le ciseaux. :( ")
                    print(f"Jai maintenant {points_bot} points.\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
                elif ton_choix == "pierre":
                    print("On a tous les deux prix Dwayne Johnson. Match nul, The caillou. :D\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
                else:
                    print("J'ai prit la Pierre!!")
                    print("Tu joue en quel langue?? C'est quoi ce truc moche??\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
        else:
            if ton_choix == "pierre":
                tes_points+=1
                print("J'ai prit la Ciseaux!!")
                print("Tu es trop fort, bro. La pierre écrase le ciseaux!")
                print(f"Tu a maintenant {tes_points} points.\n")
                print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
            else:
                if ton_choix == "ciseaux":
                    print("On a le même. Jai aussi prix le ciseaux, match nul, bro.\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
                elif ton_choix == "feuille":
                    points_bot +=1
                    print("J'ai prit le ciseaux!!")
                    print("J'ai gagné!! :) Le ciseaux coupe la feuille.")
                    print(f"J'ai maintenant {points_bot} points.\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
                else:
                    print("J'ai prit le ciseaux!!")
                    print("C'est quoi cette merde?? Euuu.. le jeux est en Français, bro.\n")
                    print(f"[Rappel: tu as {tes_points} points; j'ai {points_bot} points.]\n")
    if tes_points == max_points:
        print(f"Félicitations tu à gagné la battaille, BG !! Tu es trop puissant, mon roi absolut.\n")
        print(f"tu as atteint le nombre max de point qui est de {max_points}.Tu as donc gagné le jeu. :D\n")
        print(f"Je ne suis qu'une grosse Merde, Je vais m'immoler pour toi, mon dieu de la victoire! :3")
        print("\n*******************************************")
        print("*******************************************\n")
    else:
        print("OOOOOH!!! Tu as perduuuu!!!! wa wa ;(\n J'ai réussi à avoir le nombre maximum de point et pas toi!! Waaaaaa xD")
        print(f"( Le nombre maximum de point était de {max_points}. Tu as donc perdu le jeu, en arrivant à {tes_points} points seulements. :d )\n")
        print("\n*******************************************")
        print("*******************************************\n")
    rejouer= input("Veux-tu rejouer? (oui/non): ")
    if rejouer != "oui":
        print("*****************************************")
        print("Jeu terminer! Merci de votre participation.")
        break