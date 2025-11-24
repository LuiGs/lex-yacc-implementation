import ply.lex as lex

tokens = ['ID', 'NUM_ENTERO', 'NUM_FLOAT', 'CADENA_TEXTO','DEF_FUNCION',
          'COMA','DOS_PUNTOS','RESERVADA_RETURN','ASIGN_MAS','ASIGN_MENOS',
          'ASIGN','FUNC_INT','FUNC_FLOAT','FUNC_STR','FUNC_MIN','FUNC_MAX','FUN_ROUND',
          'I_PAR','D_PAR','OPERADOR_MAS','OPERADOR_MENOS','OPERADOR_MULT','OPERADOR_DIV',
          'OPERADOR_AND','OPERADOR_OR','OPERADOR_NOT','COMP_MENORIGUAL',
          'COMP_MAYORIGUAL','COMP_IGUALDAD']

t_COMA             = r','
t_DOS_PUNTOS       = r':'
t_ASIGN_MAS        = r'\+='
t_ASIGN_MENOS      = r'-='
t_ASIGN            = r'='
t_I_PAR            = r'\('
t_D_PAR            = r'\)'
t_OPERADOR_MAS     = r'\+'
t_OPERADOR_MENOS   = r'-'
t_OPERADOR_MULT    = r'\*'
t_OPERADOR_DIV     = r'/'
t_COMP_MENORIGUAL  = r'<='
t_COMP_MAYORIGUAL  = r'>='
t_COMP_IGUALDAD    = r'=='
t_OPERADOR_AND     = r'and'
t_OPERADOR_OR      = r'or'
t_OPERADOR_NOT     = r'not'

# Palabras reservadas y funciones
palabras_reservadas = {
    'def': 'DEF_FUNCION',
    'return': 'RESERVADA_RETURN',
    'min': 'FUNC_MIN',
    'max': 'FUNC_MAX',
    'round': 'FUN_ROUND',
    'int': 'FUNC_INT',
    'str': 'FUNC_STR',
    'float': 'FUNC_FLOAT',
    'and': 'OPERADOR_AND',
    'or': 'OPERADOR_OR',
    'not': 'OPERADOR_NOT'
}

# FUNCIONES
t_ignore = " \t"

def t_CADENA_TEXTO(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_NUM_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r"[A-Za-z_][A-Za-z0-9_]*"
    t.type = palabras_reservadas.get(t.value, 'ID')
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error léxico: carácter ilegal '{t.value[0]}' en línea {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data = """
def calcular(a, b):
    x = 10
    y = >
"""

    print("====== CÓDIGO DE PRUEBA ======")
    print(data)

    print("\n====== TOKENS GENERADOS ======\n")

    lexer.input(data)
    for tok in lexer:
        print(f"{tok.type:20}  →  {tok.value}")
