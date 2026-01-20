"""
Module pour calculer la suite de Fibonacci.

Ce module fournit plusieurs implémentations de la suite de Fibonacci.
"""


def fibonacci_iterative(n):
    """
    Calcule le n-ième nombre de Fibonacci de manière itérative.

    Args:
        n (int): L'indice du nombre de Fibonacci à calculer (n >= 0)

    Returns:
        int: Le n-ième nombre de Fibonacci

    Raises:
        ValueError: Si n est négatif

    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(10)
        55
    """
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def fibonacci_recursive(n):
    """
    Calcule le n-ième nombre de Fibonacci de manière récursive.

    Note: Cette implémentation est simple mais inefficace pour les grandes valeurs de n.

    Args:
        n (int): L'indice du nombre de Fibonacci à calculer (n >= 0)

    Returns:
        int: Le n-ième nombre de Fibonacci

    Raises:
        ValueError: Si n est négatif

    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(10)
        55
    """
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_generator(max_count=None):
    """
    Générateur qui produit les nombres de Fibonacci indéfiniment ou jusqu'à max_count.

    Args:
        max_count (int, optional): Nombre maximum de termes à générer.
                                   Si None, génère indéfiniment.

    Yields:
        int: Les nombres de Fibonacci successifs

    Examples:
        >>> list(fibonacci_generator(10))
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a, b = 0, 1
    count = 0

    while max_count is None or count < max_count:
        yield a
        a, b = b, a + b
        count += 1


def fibonacci_sequence(n):
    """
    Retourne une liste contenant les n premiers nombres de Fibonacci.

    Args:
        n (int): Le nombre de termes de Fibonacci à générer (n >= 0)

    Returns:
        list: Liste des n premiers nombres de Fibonacci

    Raises:
        ValueError: Si n est négatif

    Examples:
        >>> fibonacci_sequence(0)
        []
        >>> fibonacci_sequence(1)
        [0]
        >>> fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")

    return list(fibonacci_generator(n))


# Fonction principale recommandée
fibonacci = fibonacci_iterative


if __name__ == "__main__":
    # Exemples d'utilisation
    print("Les 15 premiers nombres de Fibonacci:")
    print(fibonacci_sequence(15))

    print("\nLe 20ème nombre de Fibonacci:")
    print(fibonacci(20))

    print("\nUtilisation du générateur:")
    for i, fib in enumerate(fibonacci_generator(10)):
        print(f"F({i}) = {fib}")
