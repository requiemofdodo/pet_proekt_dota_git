from hero_oop import Hero
from manager_oop import HeroManager  # ← ВОТ ЭТА СТРОКА!


class Carry(Hero):
    def __init__(self, name):
        super().__init__(name, 'carry')
        self.damage = 100

    def special_ability(self):
        return f'{self.name} наносит {self.damage} урона!'


class Support(Hero):
    def __init__(self, name):
        super().__init__(name, 'support')
        self.healing = 50

    def special_ability(self):
        return f'{self.name} лечит на {self.healing} ХП'


class Mid(Hero):
    def __init__(self, name):
        super().__init__(name, 'mid')
        self.mana = 200

    def special_ability(self):
        return f'{self.name} имеет {self.mana} маны в миду'


# Создаём разные типы героев
riki = Carry("Riki")
riki.add_skill("Blink").add_skill("Cloak")

pudge = Support("Abbadon")
pudge.add_skill("Mist Coil").add_skill("Aphatetic Shield")

invoker = Mid("Invoker")
invoker.add_skill("Quas").add_skill("Wex").add_skill("Exort")

# Показываем
print(riki.special_ability())
print(pudge.special_ability())
print(invoker.special_ability())

# Все работают с менеджером!
manager = HeroManager()
manager.add_hero(riki).add_hero(pudge).add_hero(invoker)
manager.list_all()
