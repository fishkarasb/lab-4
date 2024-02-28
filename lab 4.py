class Cosmetic:
    def __int__(self, brand: str, expiration_date: int):
        self.brand = brand
        self.expiration_date = expiration_date
        """
               Создание объекта "Косметика"

               :param brand: Название бренда косметики
               :param expiration_date: Срок годности открытой косметики в месяцах
        """

    def __str__(self) -> str:
        return f"Бренд {self.brand}, срок годности  {self.expiration_date}."

    def __repr__(self) -> str:
        return f"(brand={self.brand!r}, expiration_date={self.expiration_date!r})"


class Mascara(Cosmetic):
    def __init__(self, brand: str, expiration_date: int, durability: str):
        super().__int__(brand, expiration_date)
        self.durability = durability

    """
                   Создание объекта "Тушь"

                   :param brand: Название бренда туши
                   :param expiration_date: Срок годности туши в месяцах
                   :param durability: Стойкость туши 
    """
    def warning(self) -> str:
        return "Закрытая тушь хранится 12 месяцев!"

    """
                  Предупреждение для пользователей
                  :return: Показывает сколько хранится закрытый продукт
    """
    def __str__(self) -> str:
        return f"Бренд {self.brand}, срок годности  {self.expiration_date}, уровень стойкости {self.durability}."

    def __repr__(self) -> str:
        return f"(brand={self.brand!r}, expiration_date={self.expiration_date!r}, durability={self.durability})"


class Lipstick(Cosmetic):
    def __init__(self, brand: str, expiration_date: int, shade_number: int):
        super().__int__(brand, expiration_date)
        self.shade_number = shade_number

    """
                   Создание объекта "Помада"

                   :param brand: Название бренда помады
                   :param expiration_date: Срок годности помады в месяцах
                   :param shade_number: Оттенок помады
    """

    @property
    def shade_number(self):
        return self._shade_number

    @shade_number.setter
    def shade_number(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Номер оттенка должен быть типа int")
        if value < 0:
            raise ValueError("Номер оттенка должен  быть положительным числом")
        self._shade_number = value

    """
                    Проверка, что номер оттенка является положительным числом и типа int
    """

    def __str__(self) -> str:
        return f"Бренд {self.brand}, срок годности  {self.expiration_date}, номер оттенка {self.shade_number}."

    def __repr__(self) -> str:
        return f"(brand={self.brand!r}, expiration_date={self.expiration_date!r}, shade_number={self.shade_number})"


if __name__ == "__main__":
    mascara = Mascara("Maybelline", 6, "Водостойкая")
    lipstick = Lipstick("MAC", 24, 10)
    print(mascara)
    print(lipstick)
    lipstick.shade_number = 0
    print(lipstick)
    print(mascara.warning())
    pass
