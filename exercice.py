#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import *
from os import path
import pickle #CP

# TODO: Définissez vos fonction ici
def compare_2_files(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        test = True
        for line_number, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                test=False
                print(f"les lignes {line_number} ne sont pas pareil:", f"\nligne1: {line1}ligne2: {line2}")
        if f1.read()!=f2.read():
            test=False
            print(f"{f2.name} est plus long que {f1.name}")
        if test==True: print("Les fichiers sont pareil")

def triple_spaces(f1, f2):
    with open(f1, 'r', encoding="utf-8") as file1, open(f2, 'w', encoding="utf-8") as file2:
        file2.write(file1.read().replace(" ", " _ "))

def notes(f1, f2):
    with open(f1, encoding="utf-8") as file1:
        pourcentage = file1.read().splitlines()
    
    with open(f2, 'w', encoding="utf-8") as file2:
        for note in pourcentage:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] < int(note) <= value[1]:
                    file2.write(note+" "+ key+"\n")

def recipe_book(recipe_):       #pickle for coherence but any type works (json better)
    if path.exists(recipe_):
        with open(recipe_, 'rb') as loading:    #b for binary as pickle needs binary not string
            recipes = pickle.load(recipe_)
    else: recipes = {}
    
    while True:
        choice = input(
            "Choisissez une option (lettre) et appuyez sur enter ensuite: \n"
            "a) Ajouter une recette \n"
            "b) Modifier une recette \n"
            "c) Supprimer une recette \n"
            "d) Afficher une recette \n"
            "e) Quitter le programme\n"
        )#.strip()

        if choice == "a":
            recipes = add_recipes(recipes)
        elif choice == "b":
            recipes = add_recipes(recipes)
        elif choice == "c":
            recipes = delete_recipe(recipes)
        elif choice == "d":
            print_recipe(recipes)
        elif choice == "e":
            break
        else: print("Ce n'est pas une option valide")

    with open(recipe_, 'wb') as book:
        pickle.dump(recipes, book)

    
    
    pass

def numbers_ascending(f1):
    numbers = []
    with open(f1, 'r', encoding="utf-8") as file1:
        for line in file1:
            for character in line:
                if character.isnumeric():
                    numbers.append(character)
    return sorted(numbers)

def one_of_two(f1, f2):
    with open(f1, 'r', encoding="utf-8") as file1, open(f2, 'w', encoding="utf-8") as file2:
        for line_number, line in enumerate(file1):
            if (line_number%2)==0:
                file2.write(line)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # compare_2_files("exemple.txt", "exemple2.txt")
    # triple_spaces("exemple.txt", "exemple_copy.txt")
    # notes("notes.txt", "notes_letter.txt")
    recipe_book("recettes.txt")
    # print(numbers_ascending("exemple.txt"))
    # one_of_two("notes.txt", "notes_skip.txt")
