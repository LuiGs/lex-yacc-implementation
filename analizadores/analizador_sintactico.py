# Importar librería Yacc
from ply.yacc import yacc
from analizador_lexico import tokens, lexer

# Definición de reglas de producción

# Regla Inicial
def p_lista_sentencias_multiple(p):
    '''lista_sentencias : sentencia lista_sentencias'''
    p[0] = [p[1]] + p[2]

def p_lista_sentencias_simple(p):
    '''lista_sentencias : sentencia'''
    p[0] = [p[1]]

def p_sentencia(p):
    '''sentencia : definicion_funcion
                 | asignacion
                 | llamada_funcion'''
    p[0] = p[1]

def p_definicion_funcion(p):
    '''definicion_funcion : DEF_FUNCION ID I_PAR ID COMA ID D_PAR DOS_PUNTOS bloque_funcion'''
    p[0] = ('def_funcion', p[2], p[4], p[6], p[9])

def p_bloque_funcion(p):
    '''bloque_funcion : bloque sentencia_return'''
    p[0] = ('bloque_funcion', p[1], p[2])

def p_bloque_vacio(p):
    '''bloque : '''
    p[0] = []

def p_bloque_sentencias(p):
    '''bloque : sentencia_bloque bloque'''
    p[0] = [p[1]] + p[2]

def p_sentencia_bloque(p):
    '''sentencia_bloque : asignacion
                        | llamada_funcion'''
    p[0] = p[1]

def p_sentencia_return(p):
    '''sentencia_return : RESERVADA_RETURN expresion'''
    p[0] = ('return', p[2])

def p_asignacion(p):
    '''asignacion : ID operador_asignacion expresion'''
    p[0] = ('asignacion', p[1], p[2], p[3])

def p_operador_asignacion(p):
    '''operador_asignacion : ASIGN
                           | ASIGN_MAS
                           | ASIGN_MENOS'''
    p[0] = p[1]

def p_expresion(p):
    '''expresion : exp_or'''
    p[0] = p[1]

def p_exp_or_simple(p):
    '''exp_or : exp_and'''
    p[0] = p[1]

def p_exp_or_operacion(p):
    '''exp_or : exp_or OPERADOR_OR exp_and'''
    p[0] = ('or', p[1], p[3])

def p_exp_and_simple(p):
    '''exp_and : exp_not'''
    p[0] = p[1]

def p_exp_and_operacion(p):
    '''exp_and : exp_and OPERADOR_AND exp_not'''
    p[0] = ('and', p[1], p[3])

def p_exp_not_simple(p):
    '''exp_not : exp_comparacion'''
    p[0] = p[1]

def p_exp_not_operacion(p):
    '''exp_not : OPERADOR_NOT exp_comparacion'''
    p[0] = ('not', p[2])

def p_exp_comparacion_simple(p):
    '''exp_comparacion : exp_suma'''
    p[0] = p[1]

def p_exp_comparacion_operacion(p):
    '''exp_comparacion : exp_suma operador_comparacion exp_suma'''
    p[0] = (p[2], p[1], p[3])

def p_operador_comparacion(p):
    '''operador_comparacion : COMP_MENORIGUAL
                            | COMP_MAYORIGUAL
                            | COMP_IGUALDAD'''
    p[0] = p[1]

def p_exp_suma_simple(p):
    '''exp_suma : exp_multiplicacion'''
    p[0] = p[1]

def p_exp_suma_mas(p):
    '''exp_suma : exp_suma OPERADOR_MAS exp_multiplicacion'''
    p[0] = ('+', p[1], p[3])

def p_exp_suma_menos(p):
    '''exp_suma : exp_suma OPERADOR_MENOS exp_multiplicacion'''
    p[0] = ('-', p[1], p[3])

def p_exp_multiplicacion_simple(p):
    '''exp_multiplicacion : atomo'''
    p[0] = p[1]

def p_exp_multiplicacion_mult(p):
    '''exp_multiplicacion : exp_multiplicacion OPERADOR_MULT atomo'''
    p[0] = ('*', p[1], p[3])

def p_exp_multiplicacion_div(p):
    '''exp_multiplicacion : exp_multiplicacion OPERADOR_DIV atomo'''
    p[0] = ('/', p[1], p[3])

def p_atomo_id(p):
    '''atomo : ID'''
    p[0] = ('id', p[1])

def p_atomo_num_entero(p):
    '''atomo : NUM_ENTERO'''
    p[0] = ('num_entero', p[1])

def p_atomo_num_float(p):
    '''atomo : NUM_FLOAT'''
    p[0] = ('num_float', p[1])

def p_atomo_cadena(p):
    '''atomo : CADENA_TEXTO'''
    p[0] = ('cadena_texto', p[1])

def p_atomo_llamada_funcion(p):
    '''atomo : llamada_funcion'''
    p[0] = p[1]

def p_atomo_parentesis(p):
    '''atomo : I_PAR expresion D_PAR'''
    p[0] = p[2]

def p_llamada_funcion(p):
    '''llamada_funcion : nombre_funcion I_PAR lista_argumentos D_PAR'''
    p[0] = ('llamada_funcion', p[1], p[3])

def p_nombre_funcion(p):
    '''nombre_funcion : FUNC_MIN
                      | FUNC_MAX
                      | FUN_ROUND
                      | FUNC_INT
                      | FUNC_STR
                      | FUNC_FLOAT'''
    p[0] = p[1]

def p_lista_argumentos_vacia(p):
    '''lista_argumentos : '''
    p[0] = []

def p_lista_argumentos(p):
    '''lista_argumentos : argumentos'''
    p[0] = p[1]

def p_argumentos_simple(p):
    '''argumentos : expresion'''
    p[0] = [p[1]]

def p_argumentos_multiple(p):
    '''argumentos : expresion COMA argumentos'''
    p[0] = [p[1]] + p[3]

# Manejo de errores
def p_error(p):
    if p:
        print(f"Error sintáctico en la línea {p.lineno}. No se esperaba el token: '{p.value}' (tipo: {p.type})")
    else:
        print("Error sintáctico: fin de archivo inesperado")
    raise Exception('syntax', 'error')

# Precedencia y asociatividad de operadores (de menor a mayor precedencia)
precedence = (
    ('left', 'OPERADOR_OR'),
    ('left', 'OPERADOR_AND'),
    ('right', 'OPERADOR_NOT'),
    ('left', 'COMP_MENORIGUAL', 'COMP_MAYORIGUAL', 'COMP_IGUALDAD'),
    ('left', 'OPERADOR_MAS', 'OPERADOR_MENOS'),
    ('left', 'OPERADOR_MULT', 'OPERADOR_DIV'),
)

# Construcción del parser
parser = yacc()

# Función para análisis
def analizar(codigo):
    lexer.lineno = 1
    try:
        resultado = parser.parse(codigo, lexer=lexer)
        return True, resultado
    except Exception as e:
        return False, str(e)

# Prueba del analizador

# Prueba del analizador
if __name__ == "__main__":
    codigo_prueba = """
def suma(x, y):
    z = x + y
    return z
"""
    
    print("=" * 60)
    print("ANALIZADOR SINTÁCTICO - Subconjunto de Python")
    print("=" * 60)
    print("\nCódigo a analizar:")
    print(codigo_prueba)
    print("\n" + "=" * 60)
    
    exito, resultado = analizar(codigo_prueba)
    
    if exito:
        print("✓ Análisis sintáctico CORRECTO")
        print("\nÁrbol de análisis sintáctico:")
        print(resultado)
    else:
        print("✗ Análisis sintáctico INCORRECTO")
        print(f"Error: {resultado}")
    
    print("=" * 60)