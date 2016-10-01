"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

    def loot(self):
        self.coins += enemy.coins
        print "The hero gets %d coins from %s" %(enemy.coins, enemy.name)


class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def print_status(self):
        print "%s has %d health, %d armor and %d power." % (self.name, self.health, self.armor, self.power)

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def attack(self, enemy):
        super_attack = random.random() < 0.2
        if super_attack:
            print "%s will do double damage on the next attack!" % self.name
            self.power = 2 * self.power
        super(Hero, self).attack(enemy)
        if super_attack:
            self.power = self.power / 2

    def receive_damage(self, points):
        points -= self.armor
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name


class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 4

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 8
        self.power = 2
        self.coins = 2

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        regen = random.random() < 0.2
        if regen:
            print "The Medic has regenerated 2 hit points!"
            self.health +=2
        if self.health <= 0:
            print "%s is dead." % self.name

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 1
        self.coins = 3

    def receive_damage(self, points):
        dodge = random.random() < .9
        if dodge:
            points = 0
            print "The Shadow has dodged the attack!"
            self.health -= points
        else:
            super(Shadow, self).receive_damage(points)

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 2
        self.coins = 1

    def receive_damage(self, points):
        self.health -= points
        if self.health <= 0:
            print "%s received %d damage, but did not DIE!!" % (self.name, points)
        else:
            print "%s received %d damage." % (self.name, points)

    def alive(self):
        return True


class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.loot()
            return True
        else:
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class SuperTonic(object):
    cost = 10
    name = "supertonic"
    def apply(self, character):
        strength = 10 - character.health
        character.health += strength
        print "%s's health increased to %d." % (character.name, character.health)

class Armor(object):
    cost = 5
    name = "armor"
    def apply(self, hero):
        hero.armor += 2
        print "%s armor increased %d points." % (hero.name, hero.armor)

class Evade(object):
    cost = 5
    name = "evade"
    def apply(self, hero):
        hero.evade += 2
        print "%s's evade increased 2 points!" % hero.name


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Goblin()]
#enemies = [Goblin(), Wizard(), Medic(), Shadow()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
