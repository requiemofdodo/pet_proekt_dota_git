from heroes import create_hero, add_skill, show_hero
from manager import create_manager, add_hero_to_manager,remove_hero_from_manager, show_all_heroes
manager = create_manager()

# БЕСКОНЕЧНЫЙ ЦИКЛ (меню)
while True:
    print("\n=== ГЛАВНОЕ МЕНЮ ===")
    print("1. Добавить героя")
    print("2. Показать всех героев")
    print("3. Удалить героя")
    print("4. Выход")

    choice = input("Выбери пункт (1-4): ")

    # ПУНКТ 1: Добавить героя
    if choice == "1":
        print("\n--- ДОБАВИТЬ ГЕРОЯ ---")
        name = input("Имя героя: ")
        role = input("Роль (mid/carry/support): ")

        hero = create_hero(name, role)

        # Добавляем навыки
        while True:
            skill = input("Добавить навык (или 'стоп' чтобы закончить): ")
            if skill.lower() == "стоп":
                break
            hero = add_skill(hero, skill)

        manager = add_hero_to_manager(manager, hero)
        print(f"✓ Герой {name} добавлен!")

    # ПУНКТ 2: Показать всех героев
    elif choice == "2":
        print()
        show_all_heroes(manager)

    # ПУНКТ 3: Удалить героя
    elif choice == "3":
        print("\n--- УДАЛИТЬ ГЕРОЯ ---")
        hero_name = input("Имя героя для удаления: ")
        manager = remove_hero_from_manager(manager, hero_name)
        print(f"✓ Герой {hero_name} удален!")

    # ПУНКТ 4: Выход
    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("❌ Неверный выбор!")