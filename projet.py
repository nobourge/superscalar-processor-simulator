"""
simulateur de processeur superscalaire
author: Bourgeois Noé
matricule: 496667
section: ba1-info
date: 2019/11/24 ap.J-C
"""

# import des modules externes:


# définitions des constantes globales:
    """
    1. IF : instruction fetch, va chercher l’instruction en mémoire; 
    2. ID : instruction decode, analyse l’instruction; 
    3. EX : execute, appel à l’ALU (si nécessaire); 
    4. MEM : memory access, accès à la mémoire (si nécessaire); 
    5. WB : write back, écriture des résultats dans les registres
    """


# définitions des fonctions (25 lignes max):


def LOAD():
    """
    registre adresse : copie le contenu à l’adresse mémoire donnée dans le registre donné. Rien n’est fait à l’étage EX,
    qui prend un cycle. L’étage MEM consiste à interroger la mémoire pour obtenir la donnée demandée, et prend deux
    cycles.
    L’étage WB consiste à écrire la donnée dans le bon registre et prend un cycle.
    :return:
    """


def STORE():
    """
    adresse registre: copie le contenu du registre donné àl’adresse mémoire donnée. Les étages EX et MEM prennent un
    cycle.
    L’écriture en mémoire est faite à l’étage MEM, rien n’est fait à l’étage WB (qui prend un cycle).
    :return:
    """


def MOVE():
    """
    registre-destination registre-source : consiste à copier le contenu du « registre-source » dans le
    «registre-destination». Tous les étages prennent un cycle (rien n’est fait aux étages EX et MEM, l’écriture est faite à
    l’étage WB).
    :return:
    """


def MVC():
    """
    registre-destination constante: consiste à copier la valeur de la «constante» dans le «registre destination ».
    Tous les étages prennent un cycle (rien n’est fait aux étages EX et MEM, l’écriture est faite à l’étage WB).
    :return:
    """


def IADD():
    """
    registre-destination registre-source: ajoute le contenu du «registre-source» dans le «registre destination».
    Tous les étages prennent un cycle. La somme est réalisée à l’étage EX, l’écriture dans le « registre-destination »
    à l’étage WB, et l’étage MEM ne fait rien.
    :return:
    """


def IMUL():
    """
    registre-destination registre-source : même chose que IADD sauf qu’une multiplication est réalisée, et l’étage EX
    prend 3 cycles.
    :return:
    """


def printState(c , p1 , p2 , Reg , Mem):
    """

    :param c: entier donnant le numéro du cycle
    :param p1: liste de taille 5, donnant les numéros des instructions dans chacun des étages du pipeline
    :param p2: liste de taille 5, donnant les numéros des instructions dans chacun des étages du pipeline
    :param Reg: liste de taille 10 donnant les contenus des registres
    :param Mem: liste de taille 16 donnant les contenus des cases mémoire
    :return:
    """
    print("Cycle:")
    print(c)
    print("Pipeline 1:")
    print(p1)
    print("Pipeline 2:")
    print(p2)
    print("Registres:")
    print(Reg)
    print("Memoire:")
    print(Mem)


def main():
    """

    :return:
    """
    # Exemple d'utilisation

    # Mémoire: toutes les cases sont à 0 (valeur initiale)
    #          sauf la case d'adresse 3 qui contient 10
    M = [0 for x in range(16)]  # Mémoire
    M[3] = 10

    # Registres: tous les registres sont à 0 (valeur initiale)
    #            sauf le registre R2 qui contient 7
    R = [0 for x in range(10)]  # Registres
    R[2] = 7

    # Pipelines: le permier contient l'instruction 4 dans IF,
    #            l'instruction 2 dans ID et l'instruction 0 dans EX.
    #            Le second contient l'instruction 3 dans IF et la 1
    #            dans ID.
    #            Les autres étages sont vides
    p1 = [4 , 2 , 0 , -1 , -1]
    p2 = [3 , 1 , -1 , -1 , -1]

    printState(3 , p1 , p2 , R , M)

    c += 1


# code global:

cycle = 1
Pipeline1: [2, 0, -1, -1, -1]
Pipeline2: [3, 1, -1, -1, -1]
Registres: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Memoire: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

main()

