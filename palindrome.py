def es_palindromo(palabra):

    palabra = palabra.lower()
    return palabra == palabra[::-1]

import unittest

class TestPalindromo(unittest.TestCase):
    def test_palindromo(self):
        self.assertTrue(es_palindromo("reconocer"), "'reconocer' debería ser un palíndromo.")
        self.assertFalse(es_palindromo("python"), "'python' no debería ser un palíndromo.")
        self.assertTrue(es_palindromo("Anita lava la tina"), "'Anita lava la tina' debería ser un palíndromo.")
    unittest.main()