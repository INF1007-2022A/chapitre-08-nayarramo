def add_recipes(dictionnaire):
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Entrez le nom de votre recette?\n")
    ingrediants = input("Entrez la liste d'ingrédiants de la recette, svp séparer les ingrédiants par une ,\n").split(",")
    dictionnaire[name] = ingrediants

    return dictionnaire


def print_recipe(ingredients: dict) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Entrez le nom d'une recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("La recette demandée n'existe pas!")
        print(f"Les recettes existantes sont: {list(ingredients.keys())}")

def delete_recipe(dictionary):
    name = input("Entrez le nom de la recette que vous voulez supprimer.\n")

    if name in dictionary:
        del dictionary[name]
        print("La recette est supprimée!")
    else:
        print("Cette recette n'existe pas!")

    return dictionary