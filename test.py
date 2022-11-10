# Arquivo para testes com pyUnit - Aula de Engenharia de Software Aplicada

import unittest


class TestClass(unittest.TestCase):

    def test_metodo(self):
        self.assertEqual('TAATG', 'TAAGT', "Falha")

    if __name__ == "__main__":
        unittest.main()
