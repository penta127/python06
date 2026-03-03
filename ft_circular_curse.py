from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:

    print()
    print("=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    test_ingredient = ["fire air", "dragon scales"]
    for test in test_ingredient:
        result = validate_ingredients(test)
        print(f'validate_ingredients("{test}"): {result}')
    print()

    print("Testing spell recording with validation:")
    test_ingredient = ["fire air", "shadow"]
    test_spell = ["Fireball", "Dark Magic"]
    for ingre, spell in zip(test_ingredient, test_spell):
        result = record_spell(spell, ingre)
        print(f'record_spell("{spell}", "{ingre}"): {result}')
    print()

    print("Testing late import technique:")
    lightning = record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {lightning}')

    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
