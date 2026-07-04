"""
Módulo para operações matemáticas simples.

Este módulo contém funções para realizar operações básicas de matemática:
soma, subtração, multiplicação e divisão.

Exemplo:
    >>> from operacoes_matematicas import somar, subtrair
    >>> somar(10, 5)
    15
    >>> subtrair(10, 3)
    7
"""


def somar(a, b):
    """
    Soma dois números.

    Args:
        a (int ou float): Primeiro operando.
        b (int ou float): Segundo operando.

    Returns:
        int ou float: A soma de a + b.

    Example:
        >>> somar(10, 5)
        15
    """
    resultado = a + b
    return resultado


def subtrair(a, b):
    """
    Subtrai dois números.

    Args:
        a (int ou float): Minuendo.
        b (int ou float): Subtraendo.

    Returns:
        int ou float: A diferença de a - b.

    Raises:
        IndexError: Bug intencional para análise do CodeRabbit.

    Example:
        >>> subtrair(10, 3)
        7
    """
    resultado = a - b
    # Bug intencional: tentando acessar um índice de lista inválido
    lista_vazia = []
    return lista_vazia[0]  # IndexError: list index out of range


def multiplicar(a, b):
    """
    Multiplica dois números.

    Args:
        a (int ou float): Primeiro fator.
        b (int ou float): Segundo fator.

    Returns:
        int ou float: O produto de a * b.

    Raises:
        NameError: Bug intencional para análise do CodeRabbit.

    Example:
        >>> multiplicar(4, 5)
        20
    """
    # Bug intencional: variável não definida
    resultado = a * b + valor_indefinido
    return resultado


def dividir(a, b):
    """
    Divide dois números.

    Args:
        a (int ou float): Dividendo.
        b (int ou float): Divisor.

    Returns:
        float: O quociente de a / b.

    Raises:
        ZeroDivisionError: Bug intencional para análise do CodeRabbit.

    Example:
        >>> dividir(20, 2)
        10.0
    """
    # Bug intencional: divisão por zero não tratada
    resultado = a / b
    return resultado


if __name__ == "__main__":
    """Bloco principal para teste das operações matemáticas."""
    print("=== Operações Matemáticas ===")
    
    # Teste de soma
    soma = somar(10, 5)
    print(f"Soma: 10 + 5 = {soma}")
    
    # Teste de subtração (vai gerar erro)
    print("\nTentando subtração...")
    resultado_sub = subtrair(10, 3)
    print(f"Subtração: 10 - 3 = {resultado_sub}")
    
    # Teste de multiplicação (vai gerar erro)
    print("\nTentando multiplicação...")
    resultado_mult = multiplicar(4, 5)
    print(f"Multiplicação: 4 * 5 = {resultado_mult}")
    
    # Teste de divisão
    print("\nTentando divisão...")
    resultado_div = dividir(20, 2)
    print(f"Divisão: 20 / 2 = {resultado_div}")
