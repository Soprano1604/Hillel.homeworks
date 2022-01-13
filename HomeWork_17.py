class Eukaryote:
    def info_eukaryote(self):
        print('У нас есть ядра в клетках и мы появились 1,6—2,1 млрд лет назад.')

class Animals(Eukaryote):
    def info_animals(self):
        print('Мы активно передвигаемся и кушаем готовые органические соединения.')

class Chordata(Animals):
    def info_chordata(self):
        print('У нас есть скелет и череп. У некоторых из нас его нет, но когда то был, так что он с нами.')

class Ray_finned(Chordata):
    def info_ray_finned(self):
        print('Мы живём в морских и пресных водах по всему миру. Научное название класса происходит от др.-греч. ἀκτίς - луч и πτερόν - перо, крыло. Связано со строением плавников (центральная ось базальных элементов скелета в парных плавниках отсутствует).')

# !!!!CAAAARPS!!!!

class Cypriniformes(Ray_finned):
    def info_сypriniformes(self):
        print('У меня есть веберов аппарат: плавательный пузырь соединён с кишечником. Мы преимущественно пресноводные рыбы. Число видов в отряде составляет около 15 % всех костных рыб. Среди нас имеются растительноядные, хищные и всеядные.')

class Cyprinidae(Cypriniformes):
    def info_cyprinidae(self):
        print('У нас самое многочисленное семейство пресноводных рыб. А еще у нас тело покрыто чешуёй, голова голая и зубов нет.')

class Abramis(Cyprinidae):
    def info_abramis(self):
        print('Чешуя умеренной величины. Спинной плавник короткий и высокий без толстого шипа и лежит над промежутком между брюшными плавниками и анальным.')

class Carps(Abramis):
    def info_carps(self):
        print('Голова и рот маленькие. Рот заканчивается трубкой, которая может выдвигаться. Спинной плавник высокий и короткий с тремя жёсткими неветвистыми и 8—10 мягкими ветвистыми лучами. Анальный плавник длинный с тремя жёсткими и 22—29 мягкими лучами, начинается за задним краем основания спинного плавника.')

    def __init__(self, carp_name):
        self.brain = {}
        self.brain['name'] = carp_name

    def info_carp(self):
        print('Привет! Я карп Иван и сейчас я расскажу о себе:')



# !!!!HEEERRRRING!!!!




class Clupeiformes(Ray_finned):
    def info_сlupeiformes(self):
        print('Плавательный пузырь у нас соединён каналом с пищеводом и имеет отростки, которые входят впереди в полость черепа (в слуховые капсулы). Обычно имеется боковая линия. Грудные плавники расположены ближе к брюху, брюшные плавники находятся в средней части брюха (абдоминальные). Хвостовой плавник гомоцеркальный.')

class Clupea(Clupeiformes):
    def info_clupea(self):
        print('Спинной плавник расположен над брюшными. Хвостовой плавник раздвоенный. К нашему роду относят 9 видов. Пищу составляют различные мелкие животные, особенно мелкие ракообразные. Ням-Ням')

class Atlantic_Herring(Clupea):
    def info_herring(self):
        print('Максимальная длина тела 45 см, а масса — 1,1 кг. Питаемся крилем и мелкими видами рыб, а нашими природными хищниками являются киты, треска и другие крупные рыбы и водные млекопитающие. Я - ценная промысловая рыба')

    def __init__(self, herring_name):
        self.brain = {}
        self.brain['name'] = herring_name

    def info_seledka(self):
        print('Привет! Я селёдка Маша и сейчас я расскажу о себе:')



Masha = Atlantic_Herring('Masha')
Masha.info_seledka()
Masha.info_eukaryote()
Masha.info_animals()
Masha.info_chordata()
Masha.info_ray_finned()
Masha.info_сlupeiformes()
Masha.info_clupea()
Masha.info_herring()
print("\n<・ )))><<\n")
Ivan = Carps('Ivan')
Ivan.info_carp()
Ivan.info_eukaryote()
Ivan.info_animals()
Ivan.info_chordata()
Ivan.info_ray_finned()
Ivan.info_сypriniformes()
Ivan.info_cyprinidae()
Ivan.info_abramis()
Ivan.info_carps()
