import ply.lex as lex

tokens = ['id', 'num_entero', 'num_float', 'cadena_texto','def_funcion',
          'coma','dos_puntos','reservada_return','asign_mas','asign_menos',
          'asign','func_int','func_float','func_min','func_max','fun_round',
          'i_par','d_par','operador_mas','operador_menos','operador_mult','operador_div',
          'operador_and','operador_or','operador_not','comp_menorigual',
          'comp_mayorigual','comp_igualdad','comillas']

t_coma             = r','
t_dos_puntos       = r':'
t_asign_mas        = r'\+='
t_asign_menos      = r'-='
t_asign            = r'='
t_i_par            = r'\('
t_d_par            = r'\)'
t_operador_mas     = r'\+'
t_operador_menos   = r'-'
t_operador_mult    = r'\*'
t_operador_div     = r'/'
t_comp_menorigual  = r'<='
t_comp_mayorigual  = r'>='
t_comp_igualdad    = r'=='

# FUNCIONES
t_ignore = " \t"

def t_cadena_texto(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Eliminar las comillas
    return t

def t_num_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_num_entero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_id(t):
    r"[A-Za-z][A-Za-z0-9]*"
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
