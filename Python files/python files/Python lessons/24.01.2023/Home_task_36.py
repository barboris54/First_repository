import json

class Character:
    def __init__(self, name, hero_class, hp, lvl, abilities):
        self.name = name
        self.hero = hero_class
        self.hp = hp
        self.lvl = lvl
        self.abilities = abilities

    def __str__(self):
        return f'Name: {self.name}\nClass: {self.hero}\nHP: {self.hp}\nLevel: {self.lvl}\nAbilities:{self.abilities}'
#
#
hero1 = Character('Flint', 'Magician', 15, 2, ['fireball','lighting'])

hero_test = hero1.__dict__

with open('discribe_class.json','w') as f:
    json.dump(hero_test, f)

with open('discribe_class.json', 'r') as f:
    hero = json.load(f)

print(hero)

