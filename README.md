# 🐍 Compilador - Subconjunto de Python

Analizador léxico y sintáctico para un subconjunto del lenguaje Python.

---

## 📌 Subconjunto del lenguaje implementado

### Sentencias
- **DEF:** Definición de funciones con exactamente 2 parámetros
- **ASIGNACIÓN:** `=`, `+=`, `-=`

### Tipos de datos
- **INT:** Números enteros
- **FLOAT:** Números decimales
- **STR:** Cadenas de texto (entre comillas dobles)

### Funciones built-in
- `min(a, b)` - Mínimo de dos valores
- `max(a, b)` - Máximo de dos valores
- `round(x)` - Redondeo
- `int(x)` - Conversión a entero
- `float(x)` - Conversión a decimal
- `str(x)` - Conversión a cadena

### Operadores

#### Aritméticos
- `+` Suma
- `-` Resta
- `*` Multiplicación
- `/` División

#### Lógicos
- `and` - Y lógico
- `or` - O lógico
- `not` - Negación

#### Comparación
- `<=` Menor o igual
- `>=` Mayor o igual
- `==` Igualdad

---

## 🚀 Cómo usar

### **Opción 1: Menú interactivo (Recomendado)**

Ejecuta el menú principal para probar fácilmente los analizadores:

```bash
python3 menu.py
```

#### Opciones del menú:

**1. Probar archivo con error léxico**
- Analiza `pruebas/error_lexico.txt`
- Demuestra la detección de un carácter ilegal (`@`)
- El analizador se detiene al encontrar el primer error

**2. Probar archivo con error sintáctico**
- Analiza `pruebas/error_sintactico.txt`
- Demuestra un error de sintaxis (función con 3 parámetros)
- El analizador se detiene al encontrar el primer error

**3. Probar programa correcto**
- Analiza `pruebas/programa_correcto.txt`
- Programa válido que utiliza todos los elementos del lenguaje
- Genera el árbol sintáctico exitosamente

**4. Analizar archivo personalizado**
- Permite ingresar la ruta de cualquier archivo `.txt`
- Útil para probar tus propios programas
- Ejemplo de uso:
  ```
  ➤ Ruta: pruebas/mi_programa.txt
  ```

**5. Salir**
- Cierra el programa

### **Opción 2: Script de pruebas automáticas**

Ejecuta todas las pruebas de una sola vez:

```bash
python3 probar.py
```

Este script ejecuta automáticamente los 3 casos de prueba y muestra los resultados.

---

## 📂 Estructura del proyecto

```
proyecto_compiladores/
├── menu.py                          # ⭐ Menú principal interactivo
├── probar.py                        # Script de pruebas automáticas
├── README.md                        # Este archivo
│
├── analizadores/
│   ├── analizador_lexico.py         # Analizador léxico
│   └── analizador_sintactico.py     # Analizador sintáctico
│
├── pruebas/
│   ├── error_lexico.txt             # Caso de prueba: error léxico
│   ├── error_sintactico.txt         # Caso de prueba: error sintáctico
│   ├── programa_correcto.txt        # Caso de prueba: programa válido
│   └── README_PRUEBAS.md            # Explicación detallada de las pruebas
│
└── EXPLICACION_ANALIZADOR_SINTACTICO.md  # Documentación técnica
```

---

## 📝 Ejemplo de código válido

```python
def calcular(a, b):
    x = 10
    y = 3.5
    suma = a + b
    mayor = max(a, b)
    menor = min(a, b)
    resultado = suma * 2
    division = resultado / 3
    comparacion = mayor >= 10
    logico = comparacion and menor <= 100
    negacion = not logico
    texto = "Resultado"
    entero = int(3.7)
    decimal = float(10)
    cadena = str(42)
    w = 0
    w += 5
    w -= 2
    return mayor
```

---

## 🧪 Casos de prueba

### ✅ **programa_correcto.txt**
- Programa completo y válido
- Utiliza TODOS los elementos del subconjunto del lenguaje
- Resultado: `✅ ¡Análisis sintáctico CORRECTO!`

### ❌ **error_lexico.txt**
- Contiene el carácter ilegal `@` en la línea 3
- Demuestra cómo se detectan errores léxicos
- Resultado: `Error léxico: carácter ilegal '@' en línea 3`

### ❌ **error_sintactico.txt**
- Función con 3 parámetros (solo se permiten 2)
- Demuestra cómo se detectan errores sintácticos
- Resultado: `Error sintáctico en la línea 1. No se esperaba el token: ','`

---

## 💡 Crear tus propias pruebas

1. Crea un archivo `.txt` en la carpeta `pruebas/`
2. Escribe tu código siguiendo la gramática del lenguaje
3. Usa el menú (opción 4) para analizarlo

**Ejemplo:** `pruebas/mi_programa.txt`
```python
def suma(x, y):
    resultado = x + y
    return resultado
```

---

## ⚙️ Características técnicas

### Herramientas
- **PLY (Python Lex-Yacc):** Generador de analizadores léxicos y sintácticos

### Convenciones
- **Tokens:** MAYÚSCULAS (ej: `ID`, `NUM_ENTERO`, `OPERADOR_MAS`)
- **No terminales:** minúsculas (ej: `expresion`, `lista_sentencias`, `atomo`)

### Manejo de errores
- El analizador **se detiene al primer error** encontrado
- Mensajes claros indicando el tipo y ubicación del error

### Precedencia de operadores
Implementada correctamente de menor a mayor precedencia:
1. `or`
2. `and`
3. `not`
4. `<=`, `>=`, `==`
5. `+`, `-`
6. `*`, `/`

---

## ❌ Errores comunes a evitar

| Error | Incorrecto | Correcto |
|-------|------------|----------|
| Parámetros | `def suma(a, b, c):` | `def suma(a, b):` |
| Negación | `if !activo:` | `if not activo:` |
| Y lógico | `if a && b:` | `if a and b:` |
| O lógico | `if a \|\| b:` | `if a or b:` |
| Caracteres especiales | `x @ y`, `a # b` | Solo operadores permitidos |
| Sin return | `def suma(a, b): x = a + b` | `def suma(a, b): return a + b` |

---

## 📖 Documentación adicional

- **EXPLICACION_ANALIZADOR_SINTACTICO.md:** Explicación técnica detallada paso a paso de cada regla gramatical
- **pruebas/README_PRUEBAS.md:** Detalles completos de los casos de prueba

---

## 👨‍💻 Autor

Proyecto de Compiladores - Universidad

---

## 📄 Licencia

Este proyecto es parte de un trabajo académico.
