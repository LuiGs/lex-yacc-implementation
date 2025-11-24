# Instrucciones de Ejecución

## Requisitos Previos

- **Python 3.6 o superior**
- **Biblioteca PLY** (Python Lex-Yacc)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/LuiGs/lex-yacc-implementation.git
cd lex-yacc-implementation
```

O descarga el ZIP y extráelo en tu computadora.

### 2. Instalar dependencias

#### En Windows (PowerShell o CMD):
```bash
pip install ply
```

#### En macOS/Linux:
```bash
pip3 install ply
```

## Ejecución del Proyecto

### En Windows (PowerShell o CMD):
```bash
python menu.py
```

### En macOS/Linux:
```bash
python3 menu.py
```

## Estructura del Proyecto

```
proyecto_compiladores/
├── analizadores/
│   ├── analizador_lexico.py
│   └── analizador_sintactico.py
├── pruebas/
│   ├── error_lexico.txt
│   ├── error_sintactico.txt
│   ├── programa_correcto.txt
│   └── prueba_personalizable.txt
├── menu.py
├── README.md
└── INSTRUCCIONES.md
```

## Uso del Menú Interactivo

El menú tiene 5 opciones:

1. **Error Léxico** - Prueba con un carácter ilegal (@)
2. **Error Sintáctico** - Prueba con 3 parámetros en vez de 2
3. **Programa Correcto** - Programa válido con todos los elementos del lenguaje
4. **Prueba Personalizable** - Edita `pruebas/prueba_personalizable.txt` para tus propias pruebas
5. **Salir**

## Solución de Problemas

### Error: "No module named 'ply'"
Instala la biblioteca PLY:
- Windows: `pip install ply`
- macOS/Linux: `pip3 install ply`

### Error: "No se encontró el archivo"
Asegúrate de ejecutar `menu.py` desde el directorio raíz del proyecto.

### Error: "command not found: python3"
En Windows, usa `python` en vez de `python3`.

## Compatibilidad

✅ Windows 10/11  
✅ macOS (todas las versiones)  
✅ Linux (Ubuntu, Debian, Fedora, etc.)
