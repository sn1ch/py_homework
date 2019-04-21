class Animal:
    satiety = False
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def feed(self):
        self.satiety = True
        print(self.name, 'накормлен.')

    def who_is_voice(self):
        if self.voice == 'ко-ко':
            print(self.name, ' - это курица.')
        elif self.voice == 'му-му':
            print(self.name, ' - это коровка.')
        elif self.voice == 'кря-кря':
            print(self.name, ' - это утка.')
        elif self.voice == 'мее-мее':
            print(self.name, ' - это коза.')
        elif self.voice == 'бее-бее':
            print(self.name, ' - это овца.')
        elif self.voice == 'га-га':
            print(self.name, ' - это гусь.')


class Beef(Animal):
    voice = 'му-му'
    milk = True

    def pick_milk(self):
        self.milk = False
        print('Подоил ', self.name + '.')


class Hen(Animal):
    voice = 'ко-ко'
    eggs = True

    def pick_eggs(self):
        self.eggs = False
        print('Собрал яйца с ', self.name + '.')


class Duck(Hen):
    voice = 'кря-кря'


class Sheep(Animal):
    voice = 'бее-бее'
    hair = True

    def pick_hair(self):
        self.hair = False
        print('Собрал шерсть с ', self.name + '.')


class Goose(Hen):
    voice = 'га-га'


class Goat(Beef):
    voice = 'мее-мее'


def sum_weight(some_animal_list):
    total_weight = 0
    for animal in some_animal_list:
        total_weight += animal.weight
    return total_weight


goose1 = Goose('Серый', 5)
goose2 = Goose('Белый', 6)
cow1 = Beef('Манька', 20)
sheep1 = Sheep('Барашек', 10)
sheep2 = Sheep('Кудрявый', 12)
hen1 = Hen('Ко-Ко', 1)
hen2 = Hen('Кукареку', 2)
goat1 = Goat('Рога', 11)
goat2 = Goat('Копыта', 12)
duck1 = Duck('Кряква', 3)

all_animals = [cow1, hen1, hen2, goose1, goose2, sheep1, sheep1,
               goat1, goat2, duck1]

goose1.feed()
goose1.pick_eggs()
goose1.who_is_voice()

goose2.feed()
goose2.pick_eggs()
goose2.who_is_voice()

cow1.feed()
cow1.pick_milk()
cow1.who_is_voice()

sheep1.feed()
sheep1.pick_hair()
sheep1.who_is_voice()

sheep2.feed()
sheep2.pick_hair()
sheep2.who_is_voice()

hen1.feed()
hen1.pick_eggs()
hen1.who_is_voice()

hen2.feed()
hen2.pick_eggs()
hen2.who_is_voice()

goat1.feed()
goat1.pick_milk()
goat1.who_is_voice()

goat2.feed()
goat2.pick_milk()
goat2.who_is_voice()

duck1.feed()
duck1.pick_eggs()
duck1.who_is_voice()

print(f'Общий вес всех животных {sum_weight(all_animals)}.')
print(f'Самый жирный на ферме это {max(all_animals).name}.')
