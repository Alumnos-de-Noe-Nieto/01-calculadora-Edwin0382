"""
Nivel 4: Validación de orden descendente.
Maneja bloques sustractivos correctamente para casos como XLIX (49).
"""

def validar_orden_descendente(cadena: str) -> bool:
    s = cadena.strip().upper()
    if not s:
        return False

    VALORES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    SUSTRACCIONES_VALIDAS = {
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }

    i = 0
    valor_bloque_anterior = float('inf')

    while i < len(s):
        valor_bloque_actual = 0
        paso = 1

        if i + 1 < len(s) and s[i:i+2] in SUSTRACCIONES_VALIDAS:
            if i > 0 and s[i-1] == s[i]:
                return False

            valor_bloque_actual = SUSTRACCIONES_VALIDAS[s[i:i+2]]
            paso = 2
        else:
            valor_bloque_actual = VALORES[s[i]]
            paso = 1

        if valor_bloque_actual > valor_bloque_anterior:
            return False

        if paso == 2 and valor_bloque_actual == valor_bloque_anterior:
            return False

        if paso == 2 and i + 2 < len(s):
            if VALORES[s[i+2]] >= VALORES[s[i+1]]:
                return False

        valor_bloque_anterior = valor_bloque_actual
        i += paso

    return True