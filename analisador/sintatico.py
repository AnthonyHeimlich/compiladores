from analisador.lex import lexar

def validar_aposta(tokens):
    if len(tokens) != 3 or tokens[0][0] != "APOSTA" or tokens[1][0] not in ["JOGADOR", "BANQUEIRO", "EMPATE"] or tokens[2][0] != "NUMERO":
        raise SyntaxError(f"Erro na sintaxe da aposta: {' '.join([t[1] for t in tokens])}")
    
def validar_mao(tokens):
    if len(tokens) != 4 or tokens[0][0] != "MAO" or tokens[1][0] not in ["JOGADOR", "BANQUEIRO"] or tokens[2][0] not in ["STRING"] or tokens[3][0] not in ["STRING"] :
        raise SyntaxError(f"Erro na sintaxe da mão: {' '.join([t[1] for t in tokens])}")


def validar_resultado(tokens):
    if len(tokens) != 2 or tokens[0][0] != "RESULTADO" or tokens[1][0] not in ["JOGADOR", "BANQUEIRO", "EMPATE", "STRING"]:
        raise SyntaxError(f"Erro na sintaxe do resultado: {' '.join([t[1] for t in tokens])}")

def analisar(input_text):
    tokens = lexar(input_text)
    i = 0
    while i < len(tokens):
        if tokens[i][0] == "APOSTA":
            aposta_tokens = tokens[i:i+3]
            validar_aposta(aposta_tokens)
            i += 3
        elif tokens[i][0] == "MAO":
            mao_tokens = tokens[i:i+4]
            validar_mao(mao_tokens)
            i += 4
        elif tokens[i][0] == "RESULTADO":
            resultado_tokens = tokens[i:i+2]
            validar_resultado(resultado_tokens)
            i += 2
        else:
            raise SyntaxError(f"Token desconhecido: {tokens[i][1]}")
