from character import character
from action import action

if __name__ == "__main__":
    nbj = int(input("combien de joueur ?"))
    partie = character()
    dicoinfo = {}
    for i in range(0, nbj-1):
        dicoinfo["J"+str(i)] = partie.choix()
    Act = action
    while(len(dicoinfo)>1):
        for nom, role in dicoinfo.items():
            pioche = partie.choix()
            #demander quel carte piocher
            carte = ""
            if carte == pioche:
                dicoinfo = Act(dicoinfo, pioche, nom).action1()
            if carte == role:
                dicoinfo[nom] = pioche
                dicoinfo = Act(dicoinfo, role, nom).action1()
        if partie.getnbrole() == 0:
            print("fin de partie")
            break
    print("fin de partie")
    #choisir qui commence