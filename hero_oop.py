
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)
        return self  # чтобы было удобно цепляться, не обязательно

    def get_skills(self):
        return self.skills

    def info(self):  # метод с self
        print(f'=== {self.name} ===')
        print(f'Роль: {self.role}')
        print(f'Навыки: {", ".join(self.skills)}')


invoker = Hero("Invoker", "mid")
invoker.add_skill("Quas")
invoker.add_skill("Wex")
invoker.add_skill("Exort")

print(f"Герой: {invoker.name}")
print(f"Навыки: {invoker.get_skills()}")
invoker.info()
