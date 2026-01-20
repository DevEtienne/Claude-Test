"""
Tests pour le module fibonacci.
"""

import unittest
from fibonacci import (
    fibonacci_iterative,
    fibonacci_recursive,
    fibonacci_generator,
    fibonacci_sequence,
    fibonacci
)


class TestFibonacci(unittest.TestCase):
    """Tests pour les fonctions de Fibonacci."""

    def test_fibonacci_iterative_base_cases(self):
        """Test des cas de base pour la version itérative."""
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)

    def test_fibonacci_iterative_sequence(self):
        """Test d'une séquence de valeurs connues."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected_val in enumerate(expected):
            self.assertEqual(fibonacci_iterative(i), expected_val)

    def test_fibonacci_iterative_negative(self):
        """Test qu'une erreur est levée pour les valeurs négatives."""
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)

    def test_fibonacci_recursive_base_cases(self):
        """Test des cas de base pour la version récursive."""
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_fibonacci_recursive_sequence(self):
        """Test d'une séquence de valeurs connues (valeurs petites pour éviter la lenteur)."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_val in enumerate(expected):
            self.assertEqual(fibonacci_recursive(i), expected_val)

    def test_fibonacci_recursive_negative(self):
        """Test qu'une erreur est levée pour les valeurs négatives."""
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)

    def test_fibonacci_generator(self):
        """Test du générateur de Fibonacci."""
        result = list(fibonacci_generator(10))
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)

    def test_fibonacci_generator_empty(self):
        """Test du générateur avec 0 éléments."""
        result = list(fibonacci_generator(0))
        self.assertEqual(result, [])

    def test_fibonacci_sequence(self):
        """Test de la fonction qui retourne une séquence."""
        result = fibonacci_sequence(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)

    def test_fibonacci_sequence_empty(self):
        """Test de la séquence vide."""
        result = fibonacci_sequence(0)
        self.assertEqual(result, [])

    def test_fibonacci_sequence_negative(self):
        """Test qu'une erreur est levée pour les valeurs négatives."""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

    def test_fibonacci_alias(self):
        """Test que l'alias fibonacci pointe vers fibonacci_iterative."""
        self.assertEqual(fibonacci(10), fibonacci_iterative(10))

    def test_large_fibonacci(self):
        """Test avec une valeur plus grande."""
        # F(50) = 12586269025
        self.assertEqual(fibonacci_iterative(50), 12586269025)


if __name__ == "__main__":
    unittest.main()
