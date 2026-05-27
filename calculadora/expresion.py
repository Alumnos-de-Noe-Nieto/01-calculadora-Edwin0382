from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion


def evaluar(expresion: str) -> int:
    try:
        tokens = evaluar_expresion(expresion)

        tokens_limpios = [t for t in tokens if t.tipo != 'ESPACIO']

        if not tokens_limpios:
            raise ExpresionInvalida("La expresión está vacía.")

        token_inicial = tokens_limpios[0]
        if token_inicial.tipo != 'ROMANO':
            raise ExpresionInvalida("Debe comenzar con un romano.")

        resultado = romano_a_entero(token_inicial.valor)

        i = 1
        while i < len(tokens_limpios):
            tipo_operador = tokens_limpios[i].tipo

            if i + 1 >= len(tokens_limpios):
                raise ExpresionInvalida("Expresión incompleta.")

            valor_siguiente = tokens_limpios[i + 1].valor
            entero_siguiente = romano_a_entero(valor_siguiente)

            if tipo_operador == 'SUMA':
                resultado += entero_siguiente
            elif tipo_operador == 'RESTA':
                resultado -= entero_siguiente
            i += 2

        if resultado <= 0:
            raise ExpresionInvalida(f"Resultado {resultado} inválido.")

        return resultado

    except ExpresionInvalida as e:
        raise e
    except ValueError as e:
        raise ExpresionInvalida(f"Error inesperado en la expresión: {str(e)}")
