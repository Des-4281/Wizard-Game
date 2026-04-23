## STARTER CODE
# Base Character class

import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(
                int(self.attack_power * 0.8),
                int(self.attack_power * 1.2)
        )
    
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
    
    def heal(self):
        heal_amount = random.randint(15,30)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character): 
    def __init__ (self, name):
        super(). __init__(name, health=120, attack_power=30)
        self.evading = False # Archer has a special evade ability that allows them to create distance from the opponent, increasing the chance of a missed attack

    def two_arrows(self, opponent):
        print (f"{self.name} shoots using Two Arrows!")
        self.attack(opponent)
        self.attack(opponent)

    def take_distance(self, opponent):
        self.evading = True
        print(f'{self.name} takes distance and prepares to evade the next attack!')

# Create Paladin class 
class Paladin(Character):
        def __init__ (self, name):
            super(). __init__(name, health=160, attack_power=20)
            self.shielded = False # Shielded allows the player to reduce incoming damage by 30% for the next turn. 

        def magic_strike(self, opponent): 
            bonus = random.randint(10, 20)
            opponent.health -= self.attack_power + bonus
            print (f"{self.name} uses Magic Strike for {self.attack_power + bonus} damage points!")
            if opponent.health <= 0:
                print (f"{opponent.name} has been defeated!")

        def plasma_magic_shield(self):
            self.shielded = True
            print (f"{self.name} uses Plasma Magic Shield! Next attack will be blocked!")   

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)  
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def display_battle_status(player, wizard):
    def hp_bar(health, max_health):
        length = 10
        current = max(0, health)
        filled = int((current / max_health) * length)
        empty = length - filled
        bar = '█' * filled + '░' * empty
        return bar
        
    print("\n" + "=" * 50)
    print(f" 🧙 {wizard.name:<20} HP: [{hp_bar(wizard.health, wizard.max_health)}] {max(0, wizard.health)}/{wizard.max_health}")
    print(f" ⚔️ {player.name:<20} HP: [{hp_bar(player.health, player.max_health)}] {max(0, player.health)}/{player.max_health}")
    print("=" * 50)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        display_battle_status(player, wizard)
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                damage = player.attack_power * 2
                wizard.health -= damage
                print(f"{player.name} uses Power Strike for {damage} damage!")
            elif isinstance(player, Mage):
                damage = random.randint(40, 60)
                wizard.health -= damage
                print(f"{player.name} casts Fireball for {damage} damage!")

            elif isinstance(player, Archer):
                print("1. Two Arrows 2. Range")
                ab = input("Choose your special ability: ")
                if ab == '1':
                    player.two_arrows(wizard)
                elif ab == '2':
                    player.take_distance(wizard)
            elif isinstance(player, Paladin):
                    print("1. Magic Strike 2. Plasma Magic Shield")
                    ab = input("Choose your special ability: ")
                    if ab == '1':
                        player.magic_strike(wizard)
                    elif ab == '2':
                        player.plasma_magic_shield()    
        elif choice == '3':
            player.heal()  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

    # Wizard's turn
        if wizard.health > 0:
            wizard.regenerate()
            if hasattr(player, 'shielded') and player.shielded:
                print(f"{player.name}'s Plasma Magic Shield absorbs the attack!")
                player.shielded = False
            elif hasattr(player, 'evading') and player.evading:
                print(f"{player.name} evades the attack!")
                player.evading = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"Oh no, {player.name} has been defeated!\nThe Wizard says: 'I will rule the world for all the days! HAHAHA!'")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()