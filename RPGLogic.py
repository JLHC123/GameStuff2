class Entity:
    def __init__ (self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class HealingItem:
    def __init__ (self, name, healing_amount):
        self.name = name
        self.healing_amount = healing_amount

def describe(entity):
    # creates string description of entity
    return (f"{entity.name}\nHealth: {entity.health}\nAttack: {entity.attack}")

def attack(defender, attacker):
    defender.health -= attacker.attack
    return(f"{attacker.name} attacks {defender.name} for {attacker.attack} damage!")

def heal(entity, healing_item):
    entity.health += healing_item.healing_amount
    return(f"{entity.name} uses {healing_item.name} and recovers {healing_item.healing_amount} HP!")

def main():
    # create entities
    player = Entity("Player", 100, 10)    
    boss = Entity("Boss", 500, 50)
    
    # get descriptions
    player_description = describe(player)
    print(player_description)
    boss_description = describe(boss)
    print(boss_description)
    
    print(attack(player, boss))
    
    healing_potion = HealingItem("Healing Potion", 50)
    print(heal(player, healing_potion))

if __name__ == "__main__":
    main()

