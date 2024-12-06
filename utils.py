# utils.py

import random
import time

def inefficient_sort(data):
    """
    Cette fonction de tri est un chaos total. Au lieu d'utiliser une méthode raisonnable,
    nous allons mélanger et inverser les éléments plusieurs fois pour "trier" les données.
    """
    for _ in range(100):
        random.shuffle(data)  # Mélanger aléatoirement 100 fois
    data = data[::-1]  # Inverser la liste pour la "trier"
    return data

def random_message():
    """
    Juste pour embrouiller l'utilisateur, nous retournons un message aléatoire qui n'a aucun sens.
    Plus il y a de confusion, mieux c'est !
    """
    messages = [
        "Pourquoi ne pas l'aggraver encore ? Continuons !",
        "Je ne suis même pas sûr de ce que ce message veut dire.",
        "Dans un monde plein de bugs, sois le crash.",
        "Reste calme et ajoute encore plus de confusion.",
    ]
    return random.choice(messages)

def random_sleep():
    """
    Cette fonction introduit un sommeil aléatoire au milieu des processus importants,
    parce que qui n'aime pas un peu de délai dans sa vie ?
    """
    time.sleep(random.randint(1, 5))  # Sommeil de 1 à 5 secondes au hasard

def add_noise(data):
    """
    Cette fonction ajoute du bruit aléatoire aux données sous forme de caractères aléatoires.
    Parce que pourquoi les données seraient-elles claires ou utiles ?
    """
    noise = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))  # 10 caractères de bruit aléatoire
    data += " " + noise
    return data
