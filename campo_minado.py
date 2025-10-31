import random

def criar_campo(linha, coluna):
    """Cria um matriz com as dimensões fornecidas."""

    mapa = [[' ' for _ in range(coluna)] for _ in range(linha)] #Cria uma matriz vazia
    return mapa


def preenche_campo(mapa):
    """Preenche as bordas do mapa com '-' e '|'. e o interior com '*'."""

    linha = len(mapa) #Calcula quantas linhas tem a matriz
    coluna = len(mapa[0]) #Calcula quantas colunas tem a matriz

    for i in range(linha):
        for j in range(coluna):
            if i == 0 or i == linha - 1: 
                mapa[i][j] = '-' #Preenche as bordas superior e inferior
            elif j == 0 or j == coluna - 1: 
                mapa[i][j] = '|' #Preenche as bordas da esquerda e direita
            else: 
                mapa[i][j] = '*' #Preenche o interior do mapa
    return mapa


def alocar_bombas(mapa, qtd_bombas):
    """Aloca as bombas no mapa."""

    linha = len(mapa) #Calcula quantas linhas tem a matriz
    coluna = len(mapa[0]) #Calcula quantas colunas tem a matriz
    bombas_colocadas = 0 #Contador de bombas

    while bombas_colocadas < qtd_bombas: #Loop até que todas as bombas sejam alocadas
        x = random.randint(1, linha - 2) #Sorteia um número aleatório entre 1 e linha - 2 para ser a coordenada da bomba
        y = random.randint(1, coluna - 2) #Sorteia um número aleatorio entre 1 e coluna -2 para ser a coordenada da bomba

        if mapa[x][y] != 'B': #Verifica se já existe uma bomba na posição
            mapa[x][y] = 'B'  #Se não houver uma bomba ele aloca uma bomba na posição
            bombas_colocadas += 1


def printar_campo(mapa):
    """Mostra o mapa na tela com índices de linha e coluna."""

    linha = len(mapa)
    coluna = len(mapa[0])

    print("   ", end="")
    for j in range(coluna): #Imprime os índices da coluna
        print(j, end=" ")
    print() 

    for i in range(linha): #For que percorre linha por linha
        print(i, end=" ")
        if i < 10:
            print(" ", end="") #Alinha com o índice das colunas
        for j in range(coluna): 
            print(mapa[i][j], end=" ") #Imprime cada elemento
        print() 


def contar_bombas_vizinhas(mapa, x, y):
    """Conta quantas bombas existem nas 8 posições vizinhas de (x, y)."""

    linha = len(mapa)
    coluna = len(mapa[0])
    bombas = 0


    for i in range(x - 1, x + 2): #Percorre a linha acima a linha atual e a linha abaixo de x
        for j in range(y - 1, y + 2): #Percorre a coluna a esquerda a atual e a direita de y
            if 0 <= i < linha and 0 <= j < coluna:
                if mapa[i][j] == 'B': #Conta as bombas vizinhas e retorna o valor delas
                    bombas += 1

    return bombas


def revelar_posicao(mapa_real, mapa_visivel, x, y):
    """Revela apenas a posição (x, y) escolhida pelo jogador."""

    if mapa_visivel[x][y] != '*': 
        return False

    if mapa_real[x][y] == 'B':
        mapa_visivel[x][y] = 'B'
        return True  #Indicando que acertou uma bomba

    bombas_vizinhas = contar_bombas_vizinhas(mapa_real, x, y)
    mapa_visivel[x][y] = str(bombas_vizinhas) #Atualiza a posição no mapa_visivel com o numero de bombas vizinhas
    return False


def marcar_bandeira(mapa_visivel, x, y):
    """Marca ou desmarca uma bandeira na posição (x, y)."""

    if mapa_visivel[x][y] == '*':
        mapa_visivel[x][y] = 'M' #Marca a bandeira
    elif mapa_visivel[x][y] == 'M':
        mapa_visivel[x][y] = '*' #Desmarca a bandeira


def verificar_vitoria(mapa_real, mapa_visivel):
    """Verifica se todas as minas foram corretamente marcadas com 'M'."""

    for i in range(1, len(mapa_real) - 1):
        for j in range(1, len(mapa_real[0]) - 1):
            if mapa_real[i][j] == 'B' and mapa_visivel[i][j] != 'M': #Ainda há bomba não marcada return False
                return False  
            if mapa_real[i][j] != 'B' and mapa_visivel[i][j] == 'M': #Marcou algo errado return False
                return False  
    return True #Se marcou todas as bombas corretamente return True



if __name__ == "__main__":

    print("\n\t==== CAMPO MINADO ====\n")


    while True: #Pede a dimensão do campo ao usuário
        dimensao = int(input("\nDigite a dimensão do campo minado (MÁX: 10): ")) 
        if dimensao > 10:
            print("Dimensão invalida! Digite novamente.")
        elif dimensao < 1:
            print("Dimensão invalida! Digite novamente.")
        else:
            break

    mapa_real = criar_campo(dimensao + 2, dimensao + 2) #Cria o mapa real com bordas
    mapa_visivel = criar_campo(dimensao + 2, dimensao + 2) #Cria o mapa visível ao usuario com bordas

    preenche_campo(mapa_real) #Preenche as bordas e o interior do mapa real
    preenche_campo(mapa_visivel) #Preenche as bordas e o interior do mapa visível

    while True: #Pede a quantidade de bombas ao usuário
        qtd_bombas = int(input(f"Digite o número de bombas (MÁX: {format(dimensao * dimensao - 1)}): "))
        if qtd_bombas > dimensao * dimensao - 1:
            print("Número de bombas inválido! Digite novamente.")
        elif qtd_bombas < 1:
            print("Número de bombas inválido! Digite novamente.")
        else:
            break

    alocar_bombas(mapa_real, qtd_bombas) #Aloca as bombas no mapa real
    printar_campo(mapa_visivel) #Mostra o mapa visível ao usuário


    while True: #Loop principal do jogo
        print("Qual operação deseja realizar?")
        print("1 - Revelar uma posição")
        print("2 - Marcar/Desmarcar uma bandeira")
        print("0 - Sair do jogo")

        opcao = int(input("Digite a opção desejada: "))
       
        if opcao == 1: #Revela uma posição no mapa
            x = int(input("Digite a linha que deseja revelar: "))
            y = int(input("Digite a coluna que deseja revelar: "))

            if revelar_posicao(mapa_real, mapa_visivel, x, y): #Se for revelar_posição() for True acaba o jogo
                print("Você acertou uma bomba! Fim de jogo.")
                printar_campo(mapa_real)
                break

            printar_campo(mapa_visivel)

            if verificar_vitoria(mapa_real, mapa_visivel): #Se verificar_vitoria() for True acaba o jogo
                print("Parabéns! Você venceu o jogo.")
                printar_campo(mapa_real)
                break

        elif opcao == 2:
            x = int(input("Digite a linha da bandeira: "))
            y = int(input("Digite a coluna da bandeira: "))

            marcar_bandeira(mapa_visivel, x, y)
            printar_campo(mapa_visivel)

            if verificar_vitoria(mapa_real, mapa_visivel): #Se verificar_vitoria() for True acaba o jogo
                print("Parabéns! Você venceu o jogo.")
                printar_campo(mapa_real)
                break

        elif opcao == 0:
            print("Saindo do jogo.")
            break

        else:
            print("Opção inválida! Tente novamente.")
