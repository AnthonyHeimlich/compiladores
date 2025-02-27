import random
from analisador.sintatico import analisar
from analisador.jogo import jogar_rodada
import os

def gerar_mao():
    """Gera uma mão aleatória com duas cartas"""
    baralho = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return random.sample(baralho, 2)

def registrar_jogada(jogada):
    """Registra a jogada no arquivo"""
    with open("registros/jogadas.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(jogada + "\n")

def menu_apostas():
    """Exibe o menu de apostas e coleta as escolhas do jogador"""
    print("\nEm qual você quer apostar?")
    print("1. Jogador - Paga 2x")
    print("2. Banqueiro - Paga 2x")
    print("3. Empate - Paga 8x")
    aposta = input().strip().lower()
    
    if aposta == '1' or aposta == 'jogador':
        tipo_aposta = 'Jogador'
        multiplicador = 2
    elif aposta == '2' or aposta == 'banqueiro':
        tipo_aposta = 'Banqueiro'
        multiplicador = 2
    elif aposta == '3' or aposta == 'empate':
        tipo_aposta = 'Empate'
        multiplicador = 8
    else:
        print("\nOpção inválida. Tentando novamente...\n")
        return menu_apostas()  
    
    print("\nQuanto você deseja apostar?")
    try:
        valor_aposta = float(input().strip())
    except ValueError:
        print("\nValor inválido. Tentando novamente...\n")
        return menu_apostas()  
    
    return tipo_aposta, multiplicador, valor_aposta

def jogar_novamente():
    """Pergunta ao jogador se ele deseja jogar novamente"""
    print("\nDeseja jogar mais uma vez? (Sim/Não)")
    resposta = input().strip().lower()
    return resposta == 'sim'

def gerar_arvore_derivacao(comando):
    """Gera a árvore de derivação com base no comando"""
    if comando['tipo'] == 'aposta':
        return f"comando\n|\n|-- aposta\n|   |\n|   |-- 'aposta'\n|   |-- jogador\n|   |   |\n|   |   |-- 'jogador'\n|   |-- valor\n|   |   |\n|   |   |-- NUMERO\n|   |   |   |\n|   |   |   |-- {comando['valor']}\n"
    elif comando['tipo'] == 'mao':
        return f"comando\n|\n|-- mao\n|   |\n|   |-- 'mão'\n|   |-- jogador\n|   |   |\n|   |   |-- 'jogador'\n|   |-- carta\n|   |   |\n|   |   |-- STRING\n|   |   |   |\n|   |   |   |-- '{comando['carta1']}'\n|   |-- carta\n|   |   |\n|   |   |-- STRING\n|   |   |   |\n|   |   |   |-- '{comando['carta2']}'\n"
    elif comando['tipo'] == 'resultado':
        return f"comando\n|\n|-- resultado\n|   |\n|   |-- 'resultado'\n|   |-- jogador\n|   |   |\n|   |   |-- 'jogador'\n"
    return ""

def registrar_arvore_derivacao(arvore):
    """Registra a árvore de derivação no arquivo"""
    if not os.path.exists("registros"):
        os.makedirs("registros")
    
    with open("registros/log_arvoreDerivacao.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(arvore + "\n\n")

def main():
    banca = 1000.00
    
    while True: 
        print(f"\nSaldo atual: R${banca:.2f}") 
        
        if banca <= 0:
            print("\nSua banca acabou. Jogo encerrado!")
            break
        
        if banca == 1000.00: 
            print("\nQuer apostar? (Sim/Não)")
            resposta = input().strip().lower()
            
            if resposta != 'sim':
                print(f"\nObrigado por jogar, saldo final: R${banca:.2f}")
                break  
        else:
            resposta = 'sim'  

        try:
            analisar('')
            
            tipo_aposta, multiplicador, valor_aposta = menu_apostas()
            
            if tipo_aposta is None:
                print(f"\nObrigado por jogar, saldo final: R${banca:.2f}")
                break  
            
            if valor_aposta > banca:
                print("\nVocê não tem dinheiro suficiente para essa aposta. Tente uma aposta menor.\n")
                continue
            
            banca -= valor_aposta
            
            mao_jogador = gerar_mao()
            mao_banqueiro = gerar_mao()
            
            print("\nMão do jogador:", mao_jogador)
            print("Mão do banqueiro:", mao_banqueiro)
          
            resultado, soma_jogador, soma_banqueiro = jogar_rodada(mao_jogador, mao_banqueiro)
         
            print(f"\nResultado da rodada: {resultado} (Jogador: {soma_jogador}, Banqueiro: {soma_banqueiro})")
            
            if resultado.lower() == tipo_aposta.lower():
                ganho = valor_aposta * multiplicador
                banca += ganho
                print(f"\nVocê ganhou! {ganho:.2f} reais.")
            else:
                print(f"\nVocê perdeu! Perdeu {valor_aposta:.2f} reais.")
           
            print(f"\nSaldo atual após a rodada: R${banca:.2f}")
        
            jogada = f"Aposta: {tipo_aposta} - {valor_aposta}\nMão: Jogador - {', '.join(mao_jogador)}\n" \
                     f"Mão: Banqueiro - {', '.join(mao_banqueiro)}\nResultado: {resultado}"
         
            arvore_aposta = gerar_arvore_derivacao({'tipo': 'aposta', 'valor': valor_aposta})
            arvore_mao = gerar_arvore_derivacao({'tipo': 'mao', 'carta1': mao_jogador[0], 'carta2': mao_jogador[1]})
            arvore_resultado = gerar_arvore_derivacao({'tipo': 'resultado'})
            
            registrar_arvore_derivacao(arvore_aposta)
            registrar_arvore_derivacao(arvore_mao)
            registrar_arvore_derivacao(arvore_resultado)
            
            registrar_jogada(jogada)
        
        except SyntaxError as e:
            print(f"\nErro de sintaxe: {e}")
        
        if banca <= 0:
            print("\nSua banca acabou. Jogo encerrado!")
            break 

        if not jogar_novamente():
            print(f"\nObrigado por jogar, saldo final: R${banca:.2f}")
            break 

if __name__ == "__main__":
    main()
