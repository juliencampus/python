import characters


def main():
    # warrior1 = characters.Character('toto')
    # warrior1.string_chara()
    arch = characters.Archer('arch')
    arch.string_chara()
    wizz = characters.Wizard('wizz')
    wizz.string_chara()
    arch.attack(wizz, 1)
    arch.string_chara()


if __name__ == "__main__":
    main()
