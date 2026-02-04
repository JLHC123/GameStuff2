def main():
    player = Entity("Player", 100)
    print(player.name)
    

class Entity:
    def __init__ (self, name, health):
        self.name = name
        self.health = health

if __name__ == "__main__":
    main()