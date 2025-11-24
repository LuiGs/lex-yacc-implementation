#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menú principal para probar el analizador léxico y sintáctico
"""

import sys
import os

# Agregar la carpeta analizadores al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'analizadores'))

# Intentar importar el analizador sintáctico de varias formas para evitar errores
try:
    from analizador_sintactico import analizar
except ImportError:
    try:
        # Si la carpeta 'analizadores' es un paquete
        from analizadores.analizador_sintactico import analizar
    except ImportError:
        # Intento por ruta absoluta al archivo
        import importlib.util
        analizador_path = os.path.join(os.path.dirname(__file__), 'analizadores', 'analizador_sintactico.py')
        if os.path.isfile(analizador_path):
            spec = importlib.util.spec_from_file_location("analizador_sintactico", analizador_path)
            analizador = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(analizador)
            analizar = analizador.analizar
        else:
            # Repetimos el ImportError original con información adicional
            raise ImportError(f"No se pudo importar 'analizador_sintactico' ni desde el path ni como paquete; buscado en: {analizador_path}")

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresiona Enter para continuar...")

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("ANALIZADOR LÉXICO Y SINTÁCTICO - Subconjunto de Python".center(60))
    print("=" * 60)
    print("\n📋 MENÚ DE OPCIONES:\n")
    print("  1. Probar archivo con error léxico")
    print("  2. Probar archivo con error sintáctico")
    print("  3. Probar programa correcto")
    print("  4. Analizar archivo personalizado")
    print("  5. Salir")
    print("\n" + "=" * 60)

def analizar_archivo(ruta_archivo, nombre_prueba=""):
    """
    Analiza un archivo con el compilador
    """
    print("\n" + "=" * 60)
    if nombre_prueba:
        print(f"PRUEBA: {nombre_prueba}".center(60))
    print(f"Archivo: {ruta_archivo}".center(60))
    print("=" * 60)
    
    try:
        # Leer el archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
        
        # Mostrar el código
        print("\n📄 CÓDIGO A ANALIZAR:")
        print("-" * 60)
        print(codigo)
        print("-" * 60)
        
        # Analizar
        print("\n🔍 RESULTADO DEL ANÁLISIS:")
        print("-" * 60)
        
        exito, resultado = analizar(codigo)
        
        if exito:
            print("✅ ¡Análisis sintáctico CORRECTO!")
            print("\n📊 Árbol sintáctico generado:")
            print(resultado)
        else:
            print("❌ Análisis sintáctico INCORRECTO")
            print(f"Error: {resultado}")
            
    except FileNotFoundError:
        print(f"\n❌ ERROR: No se encontró el archivo '{ruta_archivo}'")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
    
    print("=" * 60)

def opcion_error_lexico():
    """Opción 1: Probar archivo con error léxico"""
    limpiar_pantalla()
    ruta = "pruebas/error_lexico.txt"
    analizar_archivo(ruta, "Error Léxico (carácter ilegal '@')")
    pausar()

def opcion_error_sintactico():
    """Opción 2: Probar archivo con error sintáctico"""
    limpiar_pantalla()
    ruta = "pruebas/error_sintactico.txt"
    analizar_archivo(ruta, "Error Sintáctico (3 parámetros en vez de 2)")
    pausar()

def opcion_programa_correcto():
    """Opción 3: Probar programa correcto"""
    limpiar_pantalla()
    ruta = "pruebas/programa_correcto.txt"
    analizar_archivo(ruta, "Programa Correcto (todos los elementos del lenguaje)")
    pausar()

def opcion_archivo_personalizado():
    """Opción 4: Analizar archivo personalizado"""
    limpiar_pantalla()
    print("\n" + "=" * 60)
    print("ANÁLISIS DE ARCHIVO PERSONALIZADO".center(60))
    print("=" * 60)
    print("\n📁 Ingresa la ruta del archivo a analizar:")
    print("   (Ejemplo: pruebas/mi_programa.txt)")
    print("   (Presiona Enter sin escribir nada para cancelar)")
    
    ruta = input("\n➤ Ruta: ").strip()
    
    if ruta:
        limpiar_pantalla()
        analizar_archivo(ruta, "Archivo Personalizado")
    else:
        print("\n⚠️ Operación cancelada")
    
    pausar()

def main():
    """Función principal del menú"""
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("\n➤ Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            opcion_error_lexico()
        elif opcion == "2":
            opcion_error_sintactico()
        elif opcion == "3":
            opcion_programa_correcto()
        elif opcion == "4":
            opcion_archivo_personalizado()
        elif opcion == "5":
            limpiar_pantalla()
            print("\n" + "=" * 60)
            print("¡Gracias por usar el analizador!".center(60))
            print("=" * 60)
            print()
            break
        else:
            print("\n❌ Opción inválida. Por favor selecciona una opción del 1 al 5.")
            pausar()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrumpido por el usuario.")
        print("=" * 60)
        print()
        sys.exit(0)