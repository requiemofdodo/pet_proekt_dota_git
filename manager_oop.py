from hero_oop import Hero


class HeroManager:
    def __init__(self):
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)
        return self

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
        return self

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return None

    def list_all(self):
        print("=== ВСЕ ГЕРОИ ===")
        if not self.heroes:
            print('Нет героев')
        else:
            for i, hero in enumerate(self.heroes, 1):
                print(f"{i}. {hero.name} ({hero.role}) - {', '.join(hero.get_skills())}")
        return (self)


manager = HeroManager()
# создаешь героев через класс Hero
invoker = Hero("Invoker", "mid")
invoker.add_skill("Quas").add_skill("Wex").add_skill("Exort")
manager.add_hero(invoker)
manager.list_all()
