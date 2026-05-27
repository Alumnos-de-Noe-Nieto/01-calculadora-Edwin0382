"""
Nivel 5: Validación de restas válidas (Análisis Semántico).

Solamente 6 pares específicos de símbolos son permitidos para restar:
IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)

Ejemplos válidos: IV, IX, XL, XC, CD, CM, XIV (X + IV)
Ejemplos inválidos: IL (49), IC (99), XD (490), XM (990), VX (5), LC (50)
"""


def validar_restas(cadena: str) -> bool:
    """
    Valida que las restas (sustracciones) sean válidas.

    Nivel 5: Análisis Semántico - Restas válidas

    💡 PISTA: Para detectar una sustracción (valor actual < valor siguiente):
    💡 PISTA: Ejemplo: "IV" → I(1) < V(5) → par "IV" está en SUSTRACCIONES_VALIDAS → True
    💡 PISTA: Ejemplo: "IL" → I(1) < L(50) → par "IL" NO está en SUSTRACCIONES_VALIDAS → False
    💡 PISTA: Ejemplo: "XIV" → X >= I, luego I < V → par "IV" está en SUSTRACCIONES_VALIDAS → True
    💡 PISTA: Ejemplo: "IIX" → I repetido antes de IX → False
    """
    s = cadena.strip().upper()
    if s == "":
        return False

    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    for i in range(len(s) - 1):
        actual = s[i]
        siguiente = s[i+1]

        if valores[actual] < valores[siguiente]:
            par = actual + siguiente

            if par not in sustracciones_validas:
                return False

            if i > 0 and s[i-1] == actual:
                return False

    return True
