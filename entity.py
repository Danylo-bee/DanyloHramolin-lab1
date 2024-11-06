class Entity:
    # Публічні поля
    public_number = 0  # Числове публічне поле
    public_string = "default"  # Стрічкове публічне поле

    # Конструктор за замовчуванням
    def __init__(self):
        self.__name = "Unnamed"  # Приватне поле
        self.__age = 0  # Приватне поле
        print("Object created with default constructor.")

    # Конструктор з параметрами
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("Object created with parameterized constructor.")

    # Деструктор
    def __del__(self):
        print(f"Object {self.__name} is being destroyed.")

    # Методи доступу до приватних полів
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # Перевизначення __str__ та __repr__
    def __str__(self):
        return f"Entity(Name: {self.__name}, Age: {self.__age})"

    def __repr__(self):
        return f"Entity('{self.__name}', {self.__age})"