import re

# Definindo os tipos de tokens
tokens = [
    ("JOGO", r"\bjogo\b"),
    ("APOSTA", r"\baposta\b"),
    ("MAO", r"\bmão\b"),  # Corrigido para "mao" sem acento
    ("RESULTADO", r"\bresultado\b"),
    ("JOGADOR", r"\bjogador\b"),
    ("BANQUEIRO", r"\bbanqueiro\b"),
    ("EMPATE", r"\bempate\b"),
    ("NUMERO", r"\d+"),
    ("STRING", r'"[A-Za-záéíóúãàâêô0-9]+"'),
    ("ESPACO", r"\s+"),
]


# Função para o analisador léxico
def lexar(input_text):
    tokens_encontrados = []
    pos = 0
    while pos < len(input_text):
        match = None
        for tipo, regex in tokens:
            regex_compilado = re.compile(regex)
            match = regex_compilado.match(input_text, pos)
            if match:
                if tipo != "ESPACO":  # Ignorar espaços em branco
                    tokens_encontrados.append((tipo, match.group(0)))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Caractere inválido na posição {pos}")
    
    # Imprimir tokens encontrados para depuração
    print(f"Tokens encontrados: {tokens_encontrados}")
    
    return tokens_encontrados
