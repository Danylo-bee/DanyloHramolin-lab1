from entity import Entity

def main():
    # Створення об'єктів класу Entity
    entity1 = Entity("Danylo", 17)
    entity2 = Entity("Artem", 21)
    entity3 = Entity("Mykola", 35)

    # Виведення значень всіх полів
    print(entity1)
    print(entity2)
    print(entity3)

    # Приклад роботи з методами доступу
    entity1.set_name("UpdatedAlice")
    entity1.set_age(26)
    print(f"Updated entity1: {entity1}")

# Виклик main методу
if __name__ == "__main__":
    main()