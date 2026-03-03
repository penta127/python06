def main() -> None:
    print()
    print("=== Pathway Debate Mastery ===")
    print()

    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print("Testing Absolute Imports (from basic.py):")
    lead = lead_to_gold()
    gem = stone_to_gem()
    print(f"lead_to_gold(): {lead}")
    print(f"stone_to_gem(): {gem}")
    print()

    from alchemy.transmutation.advanced import (
        philosophers_stone,
        elixir_of_life,
    )
    print("Testing Relative Imports (from advanced.py):")
    stone = philosophers_stone()
    elixir = elixir_of_life()
    print(f"philosophers_stone(): {stone}")
    print(f"elixir_of_life(): {elixir}")
    print()

    print("Testing Package Access:")
    import alchemy.transmutation
    lead = alchemy.transmutation.lead_to_gold()
    stone = alchemy.transmutation.philosophers_stone()
    print(f"alchemy.transmutation.lead_to_gold(): {lead}")
    print(f"alchemy.transmutation.philosophers_stone(): {stone}")
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
