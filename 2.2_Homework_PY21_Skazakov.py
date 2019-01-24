weight_dict = {}
weight_list = []
weight_dict_names = {}

print('Добро пожаловать на ферму Дядюшки Джо! Познакомьтесь с местными обитателями.\n')

class LiveStock(object):
    def __init__(self, name, weight):
        self.name = name  # имя животного
        self.weight = weight  # вес животного

    def feed(self):
        print('Их надо покормить.\n')


class Goose(LiveStock):
    def goose_data(self, name, weight):
        super.__init__(name, weight)

    def __str__(self):
        return 'Это животное: Гусь, его кличка: {}, его вес: {} кг.'.format(self.name, self.weight)

    def product(self):
        print('У гусей надо собрать гусиные яйца.')

    def voice(self):
        sound = 'Га-га-га'
        print('Их можно узнать по звуку {}.'.format(sound))


goose_0 = Goose('Белый', 7)
if goose_0.name == 'Белый':
    weight_list.append(goose_0.weight)
goose_1 = Goose('Серый', 8)
if goose_1.name == 'Серый':
    weight_list.append(goose_1.weight)
print(goose_0)
print(goose_1)
goose_0.product()
goose_0.voice()
goose_0.feed()
weight_dict.setdefault('Гусь', ([{goose_0.name: goose_0.weight, goose_1.name: goose_1.weight}]))
weight_dict_names.setdefault(goose_0.name, goose_0.weight)
weight_dict_names.setdefault(goose_1.name, goose_1.weight)


class Cow(LiveStock):
    def cow_data(self, name, weight):
        super.__init__(name, weight)

    def __str__(self):
        return 'Это животное: Корова, её кличка: {}, её вес: {} кг.'.format(self.name, self.weight)

    def product(self):
        print('Корову надо подоить, чтобы получить с нее молоко.')

    def voice(self):
        sound = 'Мууууу'
        print('Её можно узнать по звуку {}.'.format(sound))


cow = Cow('Манька', 120)
print(cow)
if cow.name == 'Манька':
    weight_dict.setdefault('Корова', ([{cow.name: cow.weight}]))
    weight_list.append(cow.weight)
    weight_dict_names.setdefault(cow.name, cow.weight)
cow.product()
cow.voice()
cow.feed()


class Sheep(LiveStock):
    def sheep_data(self, name, weight):
        super.__init__(name, weight)

    def __str__(self):
        return 'Это животное: Овца, его кличка: {}, его вес: {} кг.'.format(self.name, self.weight)

    def product(self):
        print('Овец надо стричь, чтобы получить шерсть.')

    def voice(self):
        sound = 'Беееееее'
        print('Их можно узнать по звуку {}.'.format(sound))


sheep_0 = Sheep('Барашек', 35)
if sheep_0.name == 'Барашек':
    weight_list.append(sheep_0.weight)
sheep_1 = Sheep('Кудрявый', 42)
if sheep_1.name == 'Кудрявый':
    weight_list.append(sheep_1.weight)
print(sheep_0)
print(sheep_1)
sheep_0.product()
sheep_0.voice()
sheep_0.feed()
weight_dict.setdefault('Овца', ([{sheep_0.name: sheep_0.weight, sheep_1.name: sheep_1.weight}]))
weight_dict_names.setdefault(sheep_0.name, sheep_0.weight)
weight_dict_names.setdefault(sheep_1.name, sheep_1.weight)


class Chicken(Goose):
    def chicken_data(self, name, weight):
        super.__init__(name, weight)

    def __str__(self):
        return 'Это животное: Курица, её кличка: {}, её вес: {} кг.'.format(self.name, self.weight)

    def product(self):
        print('С куриц надо собрать куриные яйца.')

    def voice(self):
        sound = 'Ко-ко-ко-ко и Ку-ка-ре-ку'
        print('Их можно узнать по звуку {}.'.format(sound))


chicken_0 = Chicken('Коко', 4)
if chicken_0.name == 'Коко':
    weight_list.append(chicken_0.weight)
chicken_1 = Chicken('Кукареку', 5)
if chicken_1.name == 'Кукареку':
    weight_list.append(chicken_1.weight)
print(chicken_0)
print(chicken_1)
chicken_0.product()
chicken_1.voice()
chicken_0.feed()
weight_dict.setdefault('Курица', ([{chicken_0.name: chicken_0.weight, chicken_1.name: chicken_1.weight}]))
weight_dict_names.setdefault(chicken_0.name, chicken_0.weight)
weight_dict_names.setdefault(chicken_0.name, chicken_1.weight)


class Goat(Cow):
    def goat_data(self, name, weight):
        super.__init__(name, weight)

    def __str__(self):
        return 'Это животное: Коза, её кличка: {}, её вес: {} кг.'.format(self.name, self.weight)

    def product(self):
        print('Коз надо подоить, чтобы получить козье молоко. Козла доить не следует.')

    def voice(self):
        sound = 'Бе-бе-бе'
        print('Их можно узнать по звуку {}.'.format(sound))


goat_0 = Goat('Рога', 53)
if goat_0.name == 'Рога':
    weight_list.append(goat_0.weight)
goat_1 = Goat('Копыта', 49)
if goat_1.name == 'Копыта':
    weight_list.append(goat_1.weight)
print(goat_0)
print(goat_1)
goat_0.product()
goat_0.voice()
goat_0.feed()
weight_dict.setdefault('Коза', ([{goat_0.name: goat_0.weight, goat_1.name: goat_1.weight}]))
weight_dict_names.setdefault(goat_0.name, goat_0.weight)
weight_dict_names.setdefault(goat_1.name, goat_1.weight)


class Duck(Goose):
    def duck_data(self, name, weight):
        super.__init__(name, weight)

    def __str__(self):
        return 'Это животное: Утка, её кличка: {}, её вес: {} кг.'.format(self.name, self.weight)

    def product(self):
        print('С утки можно собрать утиные яйца.')

    def voice(self):
        sound = 'Кря-кря-кря'
        print('Её можно узнать по звуку {}.'.format(sound))


duck = Duck('Кряква', 4)
print(duck)
if duck.name == 'Кряква':
    weight_dict.setdefault('Утка', ([{duck.name: duck.weight}]))
    weight_list.append(duck.weight)
    weight_dict_names.setdefault(duck.name, duck.weight)
duck.product()
duck.voice()
duck.feed()

print('\n', 'Список-словарь живого веса по животным:\n {}'.format(weight_dict))

tot_weight = sum(weight_list)
print('\n', 'Общий вес поголовья фермы Дядюшки Джо: {} кг.'.format(tot_weight))

heaviest_name = max(weight_dict_names, key=weight_dict_names.get)
heaviest_weight = max(weight_dict_names.values())
heaviest_animal = ''
for i in weight_dict.items():
    for j in i[-1]:
        if heaviest_name in j:
            heaviest_animal = i[0]

print('\n', 'Самое тяжелое животное на ферме Дядюшки Джо - это {} {}, ее вес составляет {} кг. живого веса.'.format(
    heaviest_animal, heaviest_name, heaviest_weight))

lightiest_name = min(weight_dict_names, key=weight_dict_names.get)
lightiest_weight = min(weight_dict_names.values())
lightiest_animal = ''
for i in weight_dict.items():
    for j in i[-1]:
        if lightiest_name in j:
            lightiest_animal = i[0]

print('\n',
      'Самое легкое животное на ферме Дядюшки Джо - это {} {}, ее вес составляет всего {} кг. живого веса.'.format(
          lightiest_animal, lightiest_name, lightiest_weight))

print('\n И это все на сегодня, дорогие гости. Всего Вам доброго, до свидания и приходите к нам ещё!')
