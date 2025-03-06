import ply.lex as lex
import re
import sys

tokens = (
'SELECT',
'WHERE', 
'LIMIT',        
'STRING',
'AT',
'ENC',
'VAR',                             # ?.*
'TP',
'CPF',                             #foaf/dbo
'CPFVAR',
'A',
'L_PAR', 
'R_PAR',
'EOL',                             # \.
'NUM'
)


t_SELECT = r'SELECT|select'
t_WHERE = r'WHERE|where'
t_LIMIT = r'LIMIT|limit'
t_STRING = r'\"[^\"]+\"'
t_AT = r'@'
t_ENC = r'(?<=@)[^ ]*'
t_VAR = r'\?\w+'
t_TP = r':'
t_CPF = r'\w+(?=:)'
t_CPFVAR = r'(?<=:)\w+'
t_A = r'a'
t_L_PAR = r'\{'
t_R_PAR = r'\}'
t_EOL = r'\.'
t_NUM = r'\d+'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("ERRO '%s'" % t.value[0])
    t.lexer.skip(1)
    return t


lexer = lex.lex()

def tokenize(code):
    lexer.input(code)
    tokens_list = []
    i = 0
    j = 0
    for tok in lexer:
        i = tok.lineno

        if(i != j): 
            tokens_list.append(("-----------------------------"))
            tokens_list.append((" "))
            tokens_list.append((" "))
            tokens_list.append((" "))
            tokens_list.append(("-----------------------------"))

        tokens_list.append((tok.lineno, tok.type, tok.value))
        j = tok.lineno
    return tokens_list



def main(args):
    amountArgs = len(args)

    if amountArgs < 2 or amountArgs > 3:
        print('Invalid amount of arguments')
        

    with open(args[1],'r') as file:
        body = file.read()
        y = tokenize(body)

        y.append(("-----------------------------"))

        if amountArgs == 2:
            for z in y[4:]:
                print(z)

        else:
            with open(args[2] + ".txt",'w') as outfile:
                for z in y[4:]:
                    outfile.write(str(z) + "\n")    

if __name__ == '__main__':
        main(sys.argv)
