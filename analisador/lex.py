import re

# Definindo os tipos de tokens
tokens = [
    ("JOGO", r"jogo"),
    ("APOSTA", r"aposta"),
    ("MAO", r"mão"),  # Tratar "ão" corretamente
    ("RESULTADO", r"resultado"),
    ("JOGADOR", r"jogador"),
    ("BANQUEIRO", r"banqueiro"),
    ("EMPATE", r"empate"),
    ("NUMERO", r"\d+"),
    ("PALAVRA", r"[A-Za-záéíóúãàâêô]+"),  # Permitindo letras com acento ou til
    ("ESPACO", r"\s+"),  # Para ignorar espaços em branco
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
