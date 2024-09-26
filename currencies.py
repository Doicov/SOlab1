from abc import ABC, abstractmethod

# Базовый класс для валют
class Currency(ABC):
    @abstractmethod
    def to_usd(self, amount):
        pass

    @abstractmethod
    def from_usd(self, amount):
        pass


# Класс для валюты Евро
class Euro(Currency):
    exchange_rate = 1.10  # Курс евро к доллару

    def to_usd(self, amount):
        return amount * Euro.exchange_rate

    def from_usd(self, amount):
        return amount / Euro.exchange_rate


# Класс для валюты Рубль
class Ruble(Currency):
    exchange_rate = 0.012  # Курс рубля к доллару

    def to_usd(self, amount):
        return amount * Ruble.exchange_rate

    def from_usd(self, amount):
        return amount / Ruble.exchange_rate


# Класс для валюты Доллар
class Dollar(Currency):
    exchange_rate = 1.0  # Курс доллара к самому себе

    def to_usd(self, amount):
        return amount  # Доллар уже в USD

    def from_usd(self, amount):
        return amount  # Доллар уже в USD


# Основной класс, который управляет конвертацией
class CurrencyConverter:
    def __init__(self):
        # Хранилище валют
        self.currencies = {}

    def add_currency(self, currency_name, currency_class):
        self.currencies[currency_name] = currency_class()

    def convert(self, from_currency, to_currency, amount):
        if from_currency not in self.currencies or to_currency not in self.currencies:
            raise ValueError("Указанная валюта не поддерживается.")

        # Конвертация в USD
        usd_amount = self.currencies[from_currency].to_usd(amount)

        # Конвертация из USD в конечную валюту
        final_amount = self.currencies[to_currency].from_usd(usd_amount)

        return final_amount
