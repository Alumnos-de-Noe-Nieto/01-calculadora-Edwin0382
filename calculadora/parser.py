"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    if not expresion or not expresion.strip():
        return []

    try:
        tokens = tokenizar_expresion(expresion)
        if not validar_estructura_tokens(tokens):
            raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')
        return tokens
    except ExpresionInvalida:
        raise
    except ValueError:
        raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')


def tokenizar_expresion(expresion: str) -> list[Token]:
    tokens = []
    i = 0
    romanos_validos = "IVXLCDM"

    while i < len(expresion):
        char = expresion[i]

        if char == ' ':
            tokens.append(Token('ESPACIO', ' ', i))
            i += 1
        elif char == '+':
            tokens.append(Token('SUMA', '+', i))
            i += 1
        elif char == '-':
            tokens.append(Token('RESTA', '-', i))
            i += 1
        elif char in romanos_validos:
            inicio = i
            while i < len(expresion) and expresion[i] in romanos_validos:
                i += 1
            tokens.append(Token('ROMANO', expresion[inicio:i], inicio))
        else:
            raise ExpresionInvalida(f"Carácter inválido '{char}' en posición {i}")

    return tokens


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    tokens_limpios = [t for t in tokens if t.tipo != 'ESPACIO']

    # Una expresión matemática debe tener al menos 3 tokens (Romano, Operador, Romano)
    if len(tokens_limpios) < 3:
        return False

    if len(tokens_limpios) % 2 == 0:
        return False

    for i, token in enumerate(tokens_limpios):
        if i % 2 == 0:
            if token.tipo != 'ROMANO':
                return False
        else:
            if token.tipo not in ('SUMA', 'RESTA'):
                return False

    return True
