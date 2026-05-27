"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones.alfabeto import validar_simbolos
from calculadora.validaciones.orden_descendente import validar_orden_descendente
from calculadora.validaciones.repeticiones_icxm import validar_repeticiones_icxm
from calculadora.validaciones.repeticiones_vld import validar_repeticiones_vld
from calculadora.validaciones.restas import validar_restas


def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.
    """
    if not validar_simbolos(cadena):
        raise ExpresionInvalida(f"La cadena '{cadena}' contiene símbolos inválidos.")


    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida(f"La cadena '{cadena}' tiene repeticiones inválidas de I, X, C o M.")

    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida(f"La cadena '{cadena}' tiene repeticiones inválidas de V, L o D.")

    if not validar_orden_descendente(cadena):
     raise ExpresionInvalida(f"La cadena '{cadena}' tiene un orden de símbolos incorrecto.")

    if not validar_restas(cadena):
        raise ExpresionInvalida(f"La cadena '{cadena}' contiene restas no permitidas.")

    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    valor_anterior = 0

    for caracter in reversed(cadena):
        valor_actual = valores[caracter]

        if valor_actual >= valor_anterior:
            total += valor_actual
        else:
            total -= valor_actual

        valor_anterior = valor_actual

    return total
