from analisador.sintatico import analisar
from analisador.jogo import gerar_mao, jogar_rodada

def registrar_jogada(jogada):
    with open("registros/jogadas.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(jogada + "\n")

def main():
    entrada = '''
    aposta jogador 100
    aposta banqueiro 200
    aposta empate 50
    mao jogador "As" "5"
    mao banqueiro "6" "3"
    resultado "banqueiro"
    '''
    
    try:
        # Chama a função de análise sintática
        analisar(entrada)
        
        # Exemplo de mãos para o jogo
        mao_jogador = ["As", "5"]
        mao_banqueiro = ["6", "3"]
        
        # Joga uma rodada e obtém o resultado
        resultado, soma_jogador, soma_banqueiro = jogar_rodada(mao_jogador, mao_banqueiro)
        
        # Monta o registro da jogada
        jogada = f"Aposta: Jogador - 100\nAposta: Banqueiro - 200\nMão: Jogador - {', '.join(mao_jogador)}\n" \
                 f"Mão: Banqueiro - {', '.join(mao_banqueiro)}\nResultado: {resultado}"
        
        # Registra a jogada no arquivo
        registrar_jogada(jogada)
        
        # Exibe o resultado da rodada
        print(f"Resultado da rodada: {resultado}")
    
    except SyntaxError as e:
        # Exibe erros de sintaxe, se ocorrerem
        print(f"Erro de sintaxe: {e}")

if __name__ == "__main__":
    main()
