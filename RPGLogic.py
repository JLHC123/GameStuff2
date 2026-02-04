HEALING_POTION = 50

class Entity:
    def __init__ (self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

def describe(entity):
    # creates string description of entity
    return (f"{entity.name}\nHealth: {entity.health}\nAttack: {entity.attack}")

def attack(defender, attacker):
    defender.health -= attacker.attack
    return(f"{attacker.name} attacks {defender.name} for {attacker.attack} damage!")

def heal(entity, amount):
    entity.health += amount
    return(f"{entity.name} heals for {amount} HP!")

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
    print(heal(player, HEALING_POTION))

if __name__ == "__main__":
    main()

