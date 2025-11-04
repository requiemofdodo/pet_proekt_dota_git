def create_manager():
    manager = {'heroes': []}
    return manager
def add_hero_to_manager(manager, hero):
    manager['heroes'].append(hero)
    return manager
def remove_hero_from_manager(manager, hero_name):
    for hero in manager['heroes']:
        if hero['name'] == hero_name:
            manager['heroes'].remove(hero)
            break
    return manager
def show_all_heroes(manager):
    print('==== ALL HEROES ====')
    if not manager['heroes']:
        print('нет героев')
        return
    for index, hero in enumerate(manager['heroes'], start=1):
        skill_count = len(hero['skills'])
        print(f"{index}. {hero['name']} ({hero['role']}) - {skill_count} навыков")
print("Шаг 1: Создаём менеджер")
manager = create_manager()
print(manager)
print()

# Шаг 2: Создаём героя (вручную)
print("Шаг 2: Создаём героя вручную")
invoker = {'name': 'Invoker', 'role': 'mid', 'skills': ['Quas', 'Wex']}
print(invoker)
print()

# Шаг 3: Добавляем героя в менеджер
print("Шаг 3: Добавляем героя в менеджер")
manager = add_hero_to_manager(manager, invoker)
print("Герои в менеджере:")
print(manager['heroes'])
print()

# Шаг 4: Создаём второго героя
print("Шаг 4: Создаём второго героя")
riki = {'name': 'Riki', 'role': 'carry', 'skills': ['Blink', 'Cloak']}
print(riki)
print()

# Шаг 5: Добавляем второго героя
print("Шаг 5: Добавляем второго героя в менеджер")
manager = add_hero_to_manager(manager, riki)
print("Герои в менеджере:")
print(manager['heroes'])
print()

# Шаг 6: Показываем всех героев
print("Шаг 6: Показываем всех героев красиво")
show_all_heroes(manager)

# Шаг 7: Удаляем одного героя
print("Шаг 7: Удаляем Riki")
manager = remove_hero_from_manager(manager, "Riki")
print("Герои в менеджере после удаления:")
print(manager['heroes'])
print()

# Шаг 8: Показываем оставшихся героев
print("Шаг 8: Показываем оставшихся героев")
show_all_heroes(manager)