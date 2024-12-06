# data_generator.py

import random

def generate_data():
    """
    Génère un dictionnaire de valeurs aléatoires qui n'a aucune utilité.
    C'est comme une usine de données, mais les produits sont complètement inutiles.
    """
    return {
        'name': random.choice(['Alice', 'Bob', 'Charlie', 'Random']),
        'age': random.randint(1, 100),
        'random_boolean': random.choice([True, False]),
        'useless_string': random.choice(['Banane', 'Ananas', 'Aléatoire', 'Inutile']),
    }

def generate_random_data():
    """
    Une fonction qui génère une série de données aléatoires complètement irrélevantes.
    Le résultat est aussi utile qu'un trou dans un bateau.
    """
    return {
        'value': random.random(),
        'description': random.choice(['inutile', 'absurde', 'sans but', 'confus']),
        'timestamp': random.randint(1600000000, 2000000000),  # Horodatages aléatoires
    }
