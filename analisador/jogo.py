import random

def calcular_mao(mao):
    valores = {"ás": 1, "as": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 0, "j": 0, "q": 0, "k": 0}
    soma = sum([valores[card.lower()] for card in mao]) 
    return soma % 10

def jogar_rodada(mao_jogador, mao_banqueiro):
    resultado = "Empate"
    soma_jogador = calcular_mao(mao_jogador)
    soma_banqueiro = calcular_mao(mao_banqueiro)
    if soma_jogador > soma_banqueiro:
        resultado = "Jogador"
    elif soma_banqueiro > soma_jogador:
        resultado = "Banqueiro"
    return resultado, soma_jogador, soma_banqueiro

def gerar_mao():
    cartas = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return random.sample(cartas, 2)