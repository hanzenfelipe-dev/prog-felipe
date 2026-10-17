"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
def conta_negativos(lista):
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador
    """Media dos numeros. Lista vazia devolve 0."""
def media(lista):
    if len(lista) == 0:
        return 0

    soma = 0
    for numero in lista:
        soma += numero

    return soma / len(lista)


def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
def sem_o_maior(lista):
   
    if len(lista) == 0:
        return []

    nova_lista = lista.copy()
    maior = max(nova_lista)
    nova_lista.remove(maior)

    return nova_lista


def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
def acumulada(lista):
    
    nova_lista = []
    soma = 0

    for numero in lista:
        soma += numero
        nova_lista.append(soma)

    return nova_lista


def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
def achata(lista_de_listas):
    
    nova_lista = []

    for sublista in lista_de_listas:
        for elemento in sublista:
            nova_lista.append(elemento)

    return nova_lista


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
def busca_ultima(lista, alvo):
    
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == alvo:
            return i

    return -1


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
def conta_ocorrencias(lista, alvo):
    
    contador = 0

    for elemento in lista:
        if elemento == alvo:
            contador += 1

    return contador


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
def primeiro_maior_que(lista, limite):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
def busca_binaria_primeira(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    if esquerda < len(lista) and lista[esquerda] == alvo:
        return esquerda

    return -1


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
def soma_pares_contando(lista):
    soma = 0
    operacoes = 0

    for numero in lista:
        operacoes += 1
        if numero % 2 == 0:
            soma += numero

    return soma, operacoes


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
def maior_contando(lista):
    maior = lista[0]
    comparacoes = 0
    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]
    return maior, comparacoes


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
def tem_soma_contando(lista, alvo):
    comparacoes = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return True, comparacoes
    return False, comparacoes


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
def ordenada_contando(lista):
    comparacoes = 0
    for i in range(len(lista) - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return False, comparacoes
    return True, comparacoes


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
def inverte_no_lugar(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
def eh_palindromo(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio += 1
        fim -= 1

    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
def par_que_soma(lista, alvo):
    i = 0
    j = len(lista) - 1

    while i < j:
        soma = lista[i] + lista[j]

        if soma == alvo:
            return i, j
        elif soma < alvo:
            i += 1
        else:
            j -= 1

    return -1, -1


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
def soma_maxima_janela(lista, k):
    soma = sum(lista[:k])
    maior = soma

    for i in range(k, len(lista)):
        soma += lista[i] - lista[i - k]
        if soma > maior:
            maior = soma

    return maior


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
def parenteses_balanceados(texto):
    pilha = []

    for caractere in texto:
        if caractere == '(' or caractere == '[':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha or pilha[-1] != '(':
                return False
            pilha.pop()
        elif caractere == ']':
            if not pilha or pilha[-1] != '[':
                return False
            pilha.pop()

    return len(pilha) == 0
