def main():
    inventaire = [
        ("pommes", 22),
        ("melons", 4),
        ("poires", 18),
        ("fraises", 76),
        ("prunes", 51),
        ]

# On change le sens de l'inventaire, la quantité avant le nom
    inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On trie l'inventaire inversé dans l'ordre décroissant
    inventaire_inverse.sort(reverse=True)
# Et on reconstitue l'inventaire
    inventaire = [(nom_fruit, qtt) for qtt, nom_fruit in inventaire_inverse]
    print(inventaire)

if __name__ == "__main__":
    main()