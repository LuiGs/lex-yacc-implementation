# Compilador - Subconjunto de Python

Analizador léxico y sintáctico para un subconjunto del lenguaje Python usando PLY.

## Uso

Ejecutar el menú interactivo:

```bash
python3 menu.py
```

### Opciones disponibles

1. **Probar error léxico** - Detecta caracteres ilegales
2. **Probar error sintáctico** - Detecta errores de sintaxis
3. **Probar programa correcto** - Ejemplo completo funcional
4. **Prueba personalizable** - Edita `pruebas/prueba_personalizable.txt` con tu código
5. **Salir**

## Características del lenguaje

**Funciones:**
- Definición con exactamente 2 parámetros: `def nombre(a, b):`
- Return obligatorio

**Asignaciones:**
- `=`, `+=`, `-=`

**Tipos:**
- Enteros, decimales, cadenas (comillas dobles)

**Operadores:**
- Aritméticos: `+`, `-`, `*`, `/`
- Lógicos: `and`, `or`, `not`
- Comparación: `<=`, `>=`, `==`

**Funciones built-in:**
- `min(a, b)`, `max(a, b)`, `round(x)`
- `int(x)`, `float(x)`, `str(x)`

## Ejemplo

```python
def calcular(a, b):
    suma = a + b
    mayor = max(a, b)
    resultado = suma * 2
    return mayor
```

## Estructura

```
proyecto_compiladores/
├── menu.py
├── analizadores/
│   ├── analizador_lexico.py
│   └── analizador_sintactico.py
└── pruebas/
    ├── error_lexico.txt
    ├── error_sintactico.txt
    ├── programa_correcto.txt
    └── prueba_personalizable.txt
```

## Notas

- El analizador se detiene al encontrar el primer error
- Tokens en MAYÚSCULAS, no-terminales en minúsculas
- Usa PLY (Python Lex-Yacc) para generar los analizadores
