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
    return (f"{entity.name}\nHealth: {entity.health}\nAttack: {entity.attack}")

def damage(defender, attack):
    defender.health -= attack.attack
    return(f"{attack.name} deals {attack.attack} damage to {defender.name}!")

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
    
    # renamed function in case attack comes from objects (falling things)
    print(damage(player, boss))
    
    healing_potion = HealingItem("Healing Potion", 50)
    print(heal(player, healing_potion))
    
    # checks if player is healed or not (they were)
    print(describe(player))
    
    falling_boulder = Entity("Falling Boulder", 0, 1000)
    print(damage(player, falling_boulder))
    
    # add defeated / fainted check soon
    
if __name__ == "__main__":
    main()

