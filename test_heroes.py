from heroes import create_hero, add_skill
from manager import create_manager, add_hero_to_manager, remove_hero_from_manager
# ТЕСТ 1: Создание героя
def test_create_hero():
    hero = create_hero("Invoker", "mid")
    assert hero['name'] == "Invoker"
    assert hero['role'] == "mid"
    assert hero['skills'] == []
    print("✓ Тест 1 пройден")

# ТЕСТ 2: Добавление навыка
def test_add_skill():
    hero = create_hero("Invoker", "mid")
    hero = add_skill(hero, "Quas")
    assert "Quas" in hero['skills']
    print("✓ Тест 2 пройден")

# ТЕСТ 3: Создание менеджера
def test_create_manager():
    manager = create_manager()
    assert manager['heroes'] == []
    print("✓ Тест 3 пройден")

# ТЕСТ 4: Добавление героя в менеджер
def test_add_hero_to_manager():
    manager = create_manager()
    hero = create_hero("Invoker", "mid")
    manager = add_hero_to_manager(manager, hero)
    assert len(manager['heroes']) == 1
    assert manager['heroes'][0]['name'] == "Invoker"
    print("✓ Тест 4 пройден")

# ТЕСТ 5: Удаление героя
def test_remove_hero():
    manager = create_manager()
    hero = create_hero("Invoker", "mid")
    manager = add_hero_to_manager(manager, hero)
    manager = remove_hero_from_manager(manager, "Invoker")
    assert len(manager['heroes']) == 0
    print("✓ Тест 5 пройден")

# Запускаем тесты
if __name__ == "__main__":
    test_create_hero()
    test_add_skill()
    test_create_manager()
    test_add_hero_to_manager()
    test_remove_hero()
    print("\n✓✓✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ! ✓✓✓")
