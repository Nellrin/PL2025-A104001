from lex import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático:", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        prox_simb = ('erro', '', 0, 0)


def rec_Expr():
    global prox_simb
    print("De P1: Expr → Term Expr'")
    valor = rec_Term()
    resultado = rec_ExprLinha(valor)
    print("A P1: Expr → Term Expr'")
    return resultado


def rec_ExprLinha(valor):
    global prox_simb
    if prox_simb is not None and prox_simb.type in ('PLUS', 'MINUS'):
        op = prox_simb.type
        print(f"De P2: Expr' → {op} Term Expr'")
        rec_term(op)
        termo = rec_Term()
        if op == 'PLUS':
            resultado = rec_ExprLinha(valor + termo)
        else:
            resultado = rec_ExprLinha(valor - termo)
        print(f"A P2: Expr' → {op} Term Expr'")
        return resultado
    print("A P2: Expr' → ε")
    return valor


def rec_Term():
    global prox_simb
    print("De P3: Term → Factor Term'")
    valor = rec_Factor()
    resultado = rec_TermLinha(valor)
    print("A P3: Term → Factor Term'")
    return resultado


def rec_TermLinha(valor):
    global prox_simb
    if prox_simb is not None and prox_simb.type in ('TIMES', 'DIVIDE'):
        op = prox_simb.type
        print(f"De P4: Term' → {op} Factor Term'")
        rec_term(op)
        fator = rec_Factor()
        if op == 'TIMES':
            resultado = rec_TermLinha(valor * fator)
        else:
            resultado = rec_TermLinha(valor / fator)
        print(f"A P4: Term' → {op} Factor Term'")
        return resultado
    print("A P4: Term' → ε")
    return valor


def rec_Factor():
    global prox_simb
    if prox_simb.type == 'NUM':
        print("De P5: Factor → NUM")
        valor = prox_simb.value
        rec_term('NUM')
        print("A P5: Factor → NUM")
        return valor
    elif prox_simb.type == 'LPAREN':
        print("De P5: Factor → '(' Expr ')'")
        rec_term('LPAREN')
        valor = rec_Expr()
        rec_term('RPAREN')
        print("A P5: Factor → '(' Expr ')'")
        return valor
    else:
        parserError(prox_simb)
        return 0 


def rec_Parser(data):
    global prox_simb
    lexer.input(data)

    prox_simb = lexer.token()

    resultado = rec_Expr()

    return resultado