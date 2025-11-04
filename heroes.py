def create_hero(name, role):
    hero = {
        'name': name,
        'role': role,
        'skills': []
    }
    return hero
def add_skill(hero, skill):
    hero['skills'].append(skill)
    return hero
def show_hero(hero):
    print(f"=== {hero['name']} ===")
    print(f"Роль: {hero['role']}")
    if hero['skills']:
        skills_str = ', '.join(hero['skills'])
        print(f"Навыки: {skills_str}")

print("📝 ТЕСТ 1: Создаём Invoker\n")
invoker = create_hero("Invoker", "mid")
show_hero(invoker)

print("📝 ТЕСТ 2: Добавляем навыки Invoker\n")
invoker = add_skill(invoker, "Quas")
invoker = add_skill(invoker, "Wex")
invoker = add_skill(invoker, "Exort")
show_hero(invoker)

print("📝 ТЕСТ 3: Создаём Riki\n")
riki = create_hero("Riki", "carry")
show_hero(riki)

print("📝 ТЕСТ 4: Добавляем навыки Riki\n")
riki = add_skill(riki, "Blink Strike")
riki = add_skill(riki, "Cloak and Dagger")
riki = add_skill(riki, "Tricks of the Trade")
show_hero(riki)

print("📝 ТЕСТ 5: Проверяем, что герои РАЗНЫЕ\n")
print(f"Invoker: {invoker}")
print(f"Riki: {riki}")
print(f"\nОни разные? {invoker != riki}")