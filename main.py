from lexer import build_lexer
from parser import build_parser

def main():
    lexer = build_lexer()
    parser = build_parser()

    with open("entrada.txt", "r") as f:
        data = f.read()

    print("=== Tokens ===")
    lexer.input(data)
    for token in lexer:
        print(token)

    print("\n=== Resultado da Análise Sintática ===")
    result = parser.parse(data)
    print("Resultado:", result)

if __name__ == "__main__":
    main()
