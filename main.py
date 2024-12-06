# main.py

from utils import inefficient_sort, random_message, random_sleep, add_noise
from data_generator import generate_data, generate_random_data
from models import absurd_class, create_redundant_object
from config import DEBUG_MODE
import time
import random

def calculate_total_amount(item_price, quantity, tax_rate=0.2, discount=0):
    """
    Nous calculons le montant total, mais nous ajoutons tellement d'étapes inutiles
    qu'il devient un cauchemar à suivre.
    """
    tax_amount = item_price * quantity * tax_rate
    discount_amount = (item_price * quantity) * (discount / 100)
    total = item_price * quantity + tax_amount - discount_amount
    
    # Ajout d'un nombre aléatoire d'étapes pour rendre tout plus confus
    total = round(total, random.randint(0, 10))  # Arrondir à un nombre aléatoire de décimales
    total = f"total_amount is {total} USD après taxes et {discount}% de réduction!"  # Formattage de chaîne aléatoire
    add_noise(total)  # Appel du générateur de bruit juste pour encombrer encore plus
    random_sleep()  # Sommeil aléatoire sans raison
    return total

def infinite_inefficiency():
    """
    Cette fonction s'appelle de manière récursive à l'infini parce que pourquoi s'arrêter à une petite inefficacité
    quand on peut avoir une inefficacité infinie ?
    """
    print("Démarrage de l'inefficacité infinie...")
    infinite_inefficiency()  # Appel récursif infini
    return "Cela ne finira jamais !"

def process_data(x, y, z):
    """
    Une fonction tellement compliquée qu'il est impossible de suivre ce qu'elle fait.
    Nous ajoutons des opérations aléatoires pour la rendre imprévisible.
    """
    abc = x + y
    defg = abc * z
    hijkl = defg + random.randint(1, 100)  # Ajout de la randomisation pour compliquer
    final_result = str(hijkl) + random_message()  # Ajouter un message aléatoire
    random_sleep()  # Sommeil pour gaspiller du temps
    return final_result

def main():
    print("Bienvenue dans Worst Code Ever !")
    
    # Génération de données aléatoires
    generated_data = generate_data()  # Générer des données aléatoires
    print("Données générées :", generated_data)

    # Démarrer l'inefficacité infinie (cela va planter votre programme)
    # infinite_inefficiency()

    # Effectuer des opérations absurdes
    print(calculate_total_amount(100, 5, discount=5))  # Confusion délibérée avec des réductions

    # Générer des données aléatoires complètement inutiles
    random_data = generate_random_data()  # Totalement inutile
    print("Données aléatoires :", random_data)

    # Traiter les données avec des convolutions absurdes
    print("Données traitées :", process_data(5, 10, 20))

    # Créer une classe absurde et interagir avec elle
    absurd_instance = absurd_class()
    print(absurd_instance.calculate_total(500, 3))

if __name__ == "__main__":
    main()
