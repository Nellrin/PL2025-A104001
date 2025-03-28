import ply.lex as lex
import json
import sys
import re
from datetime import datetime


# DATA ######################################################
saldo = 0
money_bag = {'2e': 2,'1e': 1,'50c': 0.5,'20c': 0.2,'10c': 0.1,'5c': 0.05,'2c': 0.02,'1c': 0.01}
stock = {}
json_path = ""
on = True

# TOKENS ######################################################
tokens = (
    'LISTAR',
    'MOEDA',
    'CASH',
    'SELECIONAR',
    'CODIGO',
    'ADICIONAR',
    'STUFF',
    'SAIR'
)

# STATES ######################################################
states = (
    ('moedastate', 'exclusive'),
    ('selecionarstate', 'exclusive'),
    ('adicionarstate', 'exclusive'),
)

t_ignore = t_moedastate_ignore = t_selecionarstate_ignore = t_adicionarstate_ignore = ' \t\n,'



def t_LISTAR(t):
    r'LISTAR'
    listar()
    return t





def t_SELECIONAR(t):
    r'SELECIONAR'
    t.lexer.begin('selecionarstate')
    return t

def t_selecionarstate_CODIGO(t):
    r'[A-Z]\d{2}'
    select(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_selecionarstate_error(t):
    print("Caracter desconhecido no estado SELECIONA_STATE: '%s'" % t.value[0])
    t.lexer.skip(1)





def t_MOEDA(t):
    r'MOEDA'
    t.lexer.begin('moedastate')
    return t

def t_moedastate_CASH(t):
    r'(\d+[ce],?)+'
    put_the_money_in_the_bag(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_moedastate_error(t):
    print("Caracter desconhecido no estado MOEDA_STATE: '%s'" % t.value[0])
    t.lexer.skip(1)

def put_the_money_in_the_bag(v):
    global money_bag, saldo
    for vbuc in v.split(','):
        saldo += money_bag[vbuc]
    
    print(f"Saldo = {int(saldo)}e{int((saldo*100)%100)}c")





def t_ADICIONAR(t):
    r'ADICIONAR'
    t.lexer.begin('adicionarstate')
    return t

def t_adicionarstate_STUFF(t):
    r'(([A-Z]\d{2}),(.*?),(\d+),(\d+(\.\d+)?))'
    nineteen_dollar_fortnite_card(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_adicionarstate_error(t):
    print("Caracter desconhecido no estado MOEDA_STATE: '%s'" % t.value[0])
    t.lexer.skip(1)

def nineteen_dollar_fortnite_card(v):
    global stock
    cod, nome, quant, preco = v.split(',', 3)
    stock[cod] = {'nome': nome, 'quant': int(quant), 'preco': float(preco)}





def t_SAIR(t):
    r'SAIR'
    
    global on
    on = False

    return t

def t_error(t):
    print(f"Erro: Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)





lexer = lex.lex()





def select(s):
    global saldo
    if s in stock:
        if stock[s]['quant'] <= 0:
            print("O stock de " + stock[s]['nome'] + " acabou")
            return

        elif stock[s]['preco'] > saldo:
            print("Saldo insufuciente para satisfazer o seu pedido")
            print(f"Saldo = {int(saldo)}e{int((saldo*100)%100)}c; Pedido = {int(stock[s]['preco'])}e{int((stock[s]['preco']*100)%100)}c")
            
        else:
            saldo -= stock[s]['preco']
            stock[s]['quant'] -= 1
            print("maq: Pode retirar o produto dispensado \"" + stock[s]['nome'] + "\"")
            print(f"Saldo = {int(saldo)}e{int((saldo*100)%100)}c")

    else:
        print("Produto não encontrado")
        return

def listar():
    global saldo
    print("\nmaq:")
    print("+--------------+----------------------------------+--------------+--------------+")
    print("| cod          | nome                             | quantidade   | preço        |")
    print("+--------------+----------------------------------+--------------+--------------+")
    for linha in stock:
        #for coluna in stock[linha]:
        print(f"| {linha:<12} | {stock[linha]['nome'][:32]:32} | {stock[linha]['quant']:<12} | {stock[linha]['preco']:<12.2f} |")

    print("+--------------+----------------------------------+--------------+--------------+")
    print(f"| Saldo: {int(saldo)}e{int((saldo*100)%100):2}c |")
    print("+--------------+")


#LOAD DATA######################################################
def update_data():
    global json_path
    if json_path:
        with open(json_path, "w", encoding="utf-8") as file:

            json_data = [{"cod": cod, **info} for cod, info in stock.items()]
            json.dump(json_data, file, indent=2, ensure_ascii=False)

def load_data(args):

    global json_path, stock
    if len(args) == 2:
        json_path = args[1]
        with open(json_path, "r") as file:
            data = json.load(file)
            stock = {
                    linha["cod"]:{
                        coluna: v for coluna, v in linha.items() if coluna != 'cod'
                    } for linha in data
                }




#MAIN######################################################
def main(args):

    global on

    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    print("maq: " + str(datetime.now().date()) + " Bom dia. Estou disponível para atender o seu pedido.")

    load_data(args)

    while on:
        cmd = input(">> ").strip()
        lexer.input(cmd)

        while True:
            tok = lexer.token()
            if not tok: break

    update_data()

if __name__ == '__main__':
        main(sys.argv)