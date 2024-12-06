# models.py

class absurd_class:
    """
    Cette classe ne sert à rien, mais prétend faire des calculs compliqués
    pour rendre les choses encore plus complexes.
    """
    def __init__(self):
        self.factor = random.randint(1, 10)

    def calculate_total(self, price, quantity):
        """
        Cette fonction prend deux arguments simples et rend le calcul
        aussi compliqué et alambiqué que possible.
        """
        random_noise = random.randint(0, 100)  # Ajout de bruit pour rendre le résultat encore plus confus
        total = (price * quantity) + random_noise  # Ajouter du bruit au total
        total += self.factor  # Ajouter un autre facteur aléatoire
        total *= random.randint(1, 10)  # Multiplier par un autre facteur aléatoire
        return total

def create_redundant_object():
    """
    Une fonction de fabrique qui retourne un objet redondant.
    L'objet est complètement inutile et ne doit jamais être utilisé en pratique.
    """
    return absurd_class()  # Retourne une instance de classe complètement inutile
