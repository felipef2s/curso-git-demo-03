"""
Módulo para operações matemáticas simples.
Este módulo contém funções para soma e subtração.
"""


def somar(a, b):
    """Soma dois números."""
    resultado = a + b
    return resultado


def subtrair(a, b):
    """Subtrai dois números."""
    resultado = a - b
    # Bug intencional: tentando acessar um índice de lista inválido
    lista_vazia = []
    return lista_vazia[0]  # IndexError: list index out of range


def multiplicar(a, b):
    """Multiplica dois números."""
    # Bug intencional: variável não definida
    resultado = a * b + valor_indefinido
    return resultado


def dividir(a, b):
    """Divide dois números."""
    # Bug intencional: divisão por zero não tratada
    resultado = a / b
    return resultado


if __name__ == "__main__":
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
