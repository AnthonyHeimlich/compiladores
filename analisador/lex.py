import re

tokens = [
    ("JOGO", r"\bjogo\b"),
    ("APOSTA", r"\baposta\b"),
    ("MAO", r"\bmão\b"), 
    ("RESULTADO", r"\bresultado\b"),
    ("JOGADOR", r"\bjogador\b"),
    ("BANQUEIRO", r"\bbanqueiro\b"),
    ("EMPATE", r"\bempate\b"),
    ("NUMERO", r"\d+"),
    ("STRING", r'"[A-Za-záéíóúãàâêô0-9]+"'),
    ("ESPACO", r"\s+"),
]

def lexar(input_text):
    tokens_encontrados = []
    pos = 0
    while pos < len(input_text):
        match = None
        for tipo, regex in tokens:
            regex_compilado = re.compile(regex)
            match = regex_compilado.match(input_text, pos)
            if match:
                if tipo != "ESPACO":
                    tokens_encontrados.append((tipo, match.group(0)))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Caractere inválido na posição {pos}")
    
    print(f"Tokens encontrados: {tokens_encontrados}")
    
    return tokens_encontrados
