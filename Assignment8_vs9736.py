# [Assignment 8] Vinayak Sahal vs9736

# naming the parent class
class Character:

    # creating the constructor
    def __init__(self, name='', initial_health=0):
        self.name = name
        self.health = initial_health

    # other functions as specifed from instructions
    def take_damage(self, damage_amount):
        self.health = self.health - damage_amount
        return self.health

    def __str__(self):
        return self.name + ' (health=' + str(self.health) + ')'


# naming the subclass Hero
class Hero(Character):

    # creating the constructor
    def __init__(self, name, initial_health):
        super().__init__(name, initial_health)
        self.__inventory = []

    # function adds restore health amount to self.health
    def restore_health(self, restore_amount):
        self.health += restore_amount

    def add_inventory(self, single_item):
        self.__inventory.append(single_item)

    def remove_inventory(self, single_item):
        self.__inventory.pop(single_item)

    def get_inventory(self):
        return self. __inventory


# naming the subclass Character
class Enemy(Character):

    # creating the constructor
    def __init__(self, name, initial_health, damage_amount):
        super().__init__(name, initial_health)
        self.damage = damage_amount


# main function
def main():

    # creating the different objects
    hero = Hero('Han', 40)
    enemy = Enemy('Zombie', 20, 15)
    warewolf = Enemy('Warewolf', 15, 10)
    print('Start:')
    print(hero)
    print(enemy)
    print(warewolf)

    # printing battles between Hero and others
    print('Battle 1:')
    warewolf.take_damage(10)
    hero.take_damage(warewolf.damage)
    print(hero)
    print(warewolf)

    print('Battle 2:')
    enemy.take_damage(20)
    hero.take_damage(enemy.damage)
    print(hero)
    print(enemy)

    print('Restore Health:')
    hero.restore_health(5)
    print(hero)

    print('Inventory:')
    hero.add_inventory('gold coin')
    hero.add_inventory('candle')
    print(hero.get_inventory())


# calling main function
if __name__ == '__main__':
    main()
