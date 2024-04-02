def get_chess_notation(i):
    lettres = ['A','B','C','D','E','F','G','H']
    nombres = ['1','2','3','4','5','6','7','8']
    chess_notation = []
    for lettre in lettres:
        for chiffre in nombres:
            chess_notation.append(lettre + chiffre)
    return chess_notation[i]