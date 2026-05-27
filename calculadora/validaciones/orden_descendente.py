"""
Nivel 4: Validación de orden descendente.
Maneja bloques sustractivos correctamente para casos como XLIX (49).
"""


def validar_orden_descendente(cadena: str) -> bool:
    s = cadena.strip().upper()
    if not s:
        return False

    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }

    i = 0
    valor_bloque_anterior = float('inf')

    while i < len(s):
        valor_bloque_actual = 0
        paso = 1

        if i + 1 < len(s) and s[i:i+2] in sustracciones_validas:
            if i > 0 and s[i-1] == s[i]:
                return False

            valor_bloque_actual = sustracciones_validas[s[i:i+2]]
            paso = 2
        else:
            valor_bloque_actual = valores[s[i]]
            paso = 1

        if valor_bloque_actual > valor_bloque_anterior:
            return False

        if paso == 2 and valor_bloque_actual == valor_bloque_anterior:
            return False

        if paso == 2 and i + 2 < len(s) and valores[s[i+2]] >= valores[s[i+1]]:
            return False

        valor_bloque_anterior = valor_bloque_actual
        i += paso

    return True
