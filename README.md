# Wizard Battle

A turn-based command-line RPG where you fight the Evil Wizard to save the world.

## How to Play

```bash
python Wizard_Battle.py
```

Choose a character class, enter your name, then battle the Dark Wizard in turns until one of you falls.

## Character Classes

- **Warrior** — 140 HP, 25 attack — Power Strike: doubles attack damage
- **Mage** — 100 HP, 35 attack — Fireball: deals 40–60 random magic damage
- **Archer** — 120 HP, 30 attack — Two Arrows (attack twice) or Range (evade next hit)
- **Paladin** — 160 HP, 20 attack — Magic Strike (bonus damage) or Plasma Magic Shield (block next attack)

## Battle Actions

Each turn you choose:
1. **Attack** — deal randomized damage (±20% of attack power)
2. **Use Special Ability** — class-specific power
3. **Heal** — restore 15–30 HP (capped at max health)
4. **View Stats** — display current health and attack power

After your turn, the Evil Wizard regenerates 5 HP and attacks — unless your evade or shield ability is active.

## The Enemy

**The Dark Wizard** — 150 HP, 15 attack power. Regenerates 5 HP every turn, making long fights increasingly difficult.

## Functions

**Game Flow**
- `main()` — entry point; creates the player and starts the battle
- `create_character()` — prompts the player to pick a class and name, returns the character object
- `battle(player, wizard)` — runs the main turn loop until one side is defeated
- `display_battle_status(player, wizard)` — prints HP bars for both combatants each turn

**Character (base class)**
- `attack(opponent)` — deals randomized damage (±20% of attack power) to the opponent
- `heal()` — restores 15–30 HP, capped at max health
- `display_stats()` — prints current and max HP plus attack power

**EvilWizard**
- `regenerate()` — restores 5 HP at the start of every wizard turn

**Archer**
- `two_arrows(opponent)` — calls `attack()` twice in one turn
- `take_distance(opponent)` — sets evade flag so the next incoming attack is dodged

**Paladin**
- `magic_strike(opponent)` — deals attack power plus a 10–20 bonus
- `plasma_magic_shield()` — sets shield flag so the next incoming attack is fully blocked

## Requirements

- Python 3.x (no external dependencies)
