from parser import rec_Parser


while True:
    linha = input("Escreva uma expressão: ")
    resultado = rec_Parser(linha)
    print("Resultado:", resultado)
