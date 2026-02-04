class Entity:
    def __init__ (self, name, health):
        self.name = name
        self.health = health

def describe(entity):
    # creates string description of entity
    return (f"{entity.name}\nHealth: {entity.health}")

def main():
    # create entities
    player = Entity("Player", 100)    
    boss = Entity("Boss", 500)
    
    # get descriptions
    player_description = describe(player)
    print(player_description)
    boss_description = describe(boss)
    print(boss_description)
    
if __name__ == "__main__":
    main()

