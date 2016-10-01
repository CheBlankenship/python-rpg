class Character(object):
    def __init__(self, health, power):
        #self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print "The %s has %d health and %d power." % (self. name, self.health, self.power)

    def attack(self, enemy):
        enemy.health -= self.power
        print "The %s does %d damage to the %s." % (self. name, self.power, enemy.name)
        if enemy.health <= 0:
            print "The %s is dead." % (enemy.name)


class Hero(Character):
    name = "Hero"


class Goblin(Character):
    name = "Goblin"




hero = Hero(10, 5)
goblin =Goblin(6, 2)



while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print "    *********    "
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks goblin
        hero.attack(goblin)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input
    if not goblin.alive():
    # Goblin attacks hero
        goblin.attack(hero)
