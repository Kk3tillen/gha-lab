"""Operações aritméticas simples."""


def soma(a: float, b: float) -> float:
    return a + b


def subtrai(a: float, b: float) -> float:
    return a - b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a / b


def media(valores: list[float]) -> float:
    if not valores:
        raise ValueError("lista vazia")
    return sum(valores) / len(valores)

def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("fatorial não definido para números negativos")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado