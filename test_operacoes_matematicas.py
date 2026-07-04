"""
Testes para o módulo de operações matemáticas.

Este módulo contém testes unitários para as funções do módulo operacoes_matematicas.
Inclui testes para casos de sucesso e casos onde erros propositais são esperados.
"""

import unittest
from operacoes_matematicas import somar, subtrair, multiplicar, dividir


class TestSomar(unittest.TestCase):
    """Testes para a função somar()."""

    def test_somar_positivos(self):
        """Testa soma de dois números positivos."""
        self.assertEqual(somar(10, 5), 15)

    def test_somar_negativos(self):
        """Testa soma com números negativos."""
        self.assertEqual(somar(-10, -5), -15)

    def test_somar_misto(self):
        """Testa soma com números positivos e negativos."""
        self.assertEqual(somar(10, -5), 5)

    def test_somar_zero(self):
        """Testa soma com zero."""
        self.assertEqual(somar(0, 5), 5)
        self.assertEqual(somar(5, 0), 5)
        self.assertEqual(somar(0, 0), 0)

    def test_somar_float(self):
        """Testa soma com números decimais."""
        self.assertAlmostEqual(somar(10.5, 5.3), 15.8, places=5)

    def test_somar_comutativo(self):
        """Testa propriedade comutativa da adição."""
        a, b = 10, 5
        self.assertEqual(somar(a, b), somar(b, a))


class TestSubtrair(unittest.TestCase):
    """Testes para a função subtrair()."""

    def test_subtrair_bug_index_error(self):
        """Testa que subtrair gera IndexError (bug intencional)."""
        with self.assertRaises(IndexError):
            subtrair(10, 3)

    def test_subtrair_descripcao_bug(self):
        """Valida que o erro é especificamente IndexError."""
        with self.assertRaises(IndexError):
            subtrair(5, 2)


class TestMultiplicar(unittest.TestCase):
    """Testes para a função multiplicar()."""

    def test_multiplicar_bug_name_error(self):
        """Testa que multiplicar gera NameError (bug intencional)."""
        with self.assertRaises(NameError):
            multiplicar(4, 5)

    def test_multiplicar_descripcao_bug(self):
        """Valida que o erro é especificamente NameError com mensagem esperada."""
        with self.assertRaisesRegex(NameError, "valor_indefinido"):
            multiplicar(10, 2)


class TestDividir(unittest.TestCase):
    """Testes para a função dividir()."""

    def test_dividir_simples(self):
        """Testa divisão simples com números positivos."""
        self.assertEqual(dividir(20, 2), 10.0)

    def test_dividir_resultado_fracao(self):
        """Testa divisão que resulta em fração."""
        resultado = dividir(10, 3)
        self.assertAlmostEqual(resultado, 3.333333, places=5)

    def test_dividir_divisao_por_zero_bug(self):
        """Testa que dividir por zero gera ZeroDivisionError (bug intencional)."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_dividir_zero_numerador(self):
        """Testa divisão com zero no numerador."""
        self.assertEqual(dividir(0, 5), 0.0)

    def test_dividir_negativo(self):
        """Testa divisão com números negativos."""
        self.assertEqual(dividir(-20, 2), -10.0)
        self.assertEqual(dividir(20, -2), -10.0)


class TestIntegracaoErrosIntencionais(unittest.TestCase):
    """Testes de integração focando nos erros propositais."""

    def test_todos_erros_esperados(self):
        """Verifica que todos os três erros são lançados conforme esperado."""
        # subtrair lança IndexError
        with self.assertRaises(IndexError):
            subtrair(10, 5)

        # multiplicar lança NameError
        with self.assertRaises(NameError):
            multiplicar(10, 5)

        # dividir lança ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_somar_funciona_sem_erros(self):
        """Verifica que apenas somar funciona sem erros."""
        resultado = somar(10, 5)
        self.assertEqual(resultado, 15)
        self.assertIsInstance(resultado, int)


if __name__ == "__main__":
    unittest.main(verbosity=2)

