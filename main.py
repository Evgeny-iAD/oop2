import cat
import toys


class CatPerson(cat.Cat, toys.Toy):
    """Класс персоны КОТ"""
    def __init__(self, name, sex, color, breed, nationality_voice):
        super().__init__()
        self.sex = cat.Cat.set_sex(self, sex)
        self.color = cat.Cat.set_color(self, color)
        self.breed = cat.Cat.set_breed(self, breed)
        self.name = name
        self.nationality_voice = nationality_voice
        self.addchild = []
        self.addtoy = []

    def __str__(self):
        return f"{self.name} -- ( {cat.Cat.param(self)} )"

    def add_toy(self, name, material, color):
        p = toys.Toy()
        p.set_param_t(name, material, color)
        self.addtoy.append(p.ret_toy())


    def add_child(self, child):
        ch = child
        self.addchild.append(ch)

    def voice(self):
        return self.nationality_voice

def tree_view(root,n, x):
    print(f' {n}  {root} ')
    for j in root.addtoy:
        print(f'             игрушка кота {root.name}: {j}')
    n = '        |-'
    if x != 0: n = '     |-'
    for i in root.addchild:
        tree_view(i, n, root.addchild.index(i))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cat1 = CatPerson('Васька', 'кот', 'черный', 'русская дворовая', 'мяу')
    cat11 = CatPerson('Леопольд', 'кот', 'бежевый', 'русская дворовая', 'мяу')
    cat111 = CatPerson('Симба', 'кошка', 'коричневая', 'швецкая дворовая', 'мьян-мьян')
    cat112 = CatPerson('Джокер', 'кот', 'бежевый', 'латвийская дворовая', 'нау-нау')
    cat12 = CatPerson('Майло', 'кошка', 'белая', 'данская дворовая', 'миав')
    cat13 = CatPerson('Нафаня', 'кот', 'рыжий', 'французская дворовая', 'миаоу')

    cat1.add_child(cat11)
    cat1.add_child(cat12)
    cat1.add_child(cat13)
    cat11.add_child(cat111)
    cat11.add_child(cat112)

    cat1.add_toy('мяч', 'резина', 'оранжевый')
    cat11.add_toy('не мяч', 'пластик', 'синий')
    cat112.add_toy('мышь', 'пластик', 'серый')
    cat13.add_toy('пакет', 'пластик', 'белый')

    tree_view(cat1, '', 1)






