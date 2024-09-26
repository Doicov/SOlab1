import tkinter as tk
from tkinter import ttk
from currencies import CurrencyConverter, Euro, Ruble, Dollar  # Импорт классов коллеги


# Функция для выполнения конвертации и обновления интерфейса
def perform_conversion():
    try:
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        amount = float(amount_entry.get())

        result = converter.convert(from_currency, to_currency, amount)
        result_label.config(text=f"Результат: {result:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Ошибка ввода! Введите корректное число.")
    except Exception as e:
        result_label.config(text=f"Произошла ошибка: {e}")


# Создаем экземпляр конвертера и добавляем валюты
converter = CurrencyConverter()
converter.add_currency("EUR", Euro)
converter.add_currency("RUB", Ruble)
converter.add_currency("USD", Dollar)

# Создаем главное окно
root = tk.Tk()
root.title("Конвертер валют")

# Устанавливаем размер окна (ширина х высота)
root.geometry("500x300")  # Широкое окно

# Центрирование окна
root.eval('tk::PlaceWindow . center')

# Устанавливаем стиль для более красивого интерфейса
style = ttk.Style()
style.theme_use("clam")  # Можно использовать "clam", "alt", "default", "classic"

# Поля для выбора валют
from_currency_var = tk.StringVar(value="EUR")
to_currency_var = tk.StringVar(value="USD")

currency_options = ["EUR", "RUB", "USD"]

# Добавляем отступы между элементами
padding = {'padx': 10, 'pady': 10}

# Создаем Frame для размещения выпадающих списков в одной строке
currency_frame = ttk.Frame(root)
currency_frame.pack(**padding)

# Метка и выпадающее меню для выбора исходной валюты
from_currency_label = ttk.Label(currency_frame, text="Исходная валюта:")
from_currency_label.grid(row=0, column=0, padx=5)

from_currency_menu = ttk.OptionMenu(currency_frame, from_currency_var, *currency_options)
from_currency_menu.grid(row=0, column=1, padx=5)

# Метка и выпадающее меню для выбора целевой валюты
to_currency_label = ttk.Label(currency_frame, text="Целевая валюта:")
to_currency_label.grid(row=0, column=2, padx=5)

to_currency_menu = ttk.OptionMenu(currency_frame, to_currency_var, *currency_options)
to_currency_menu.grid(row=0, column=3, padx=5)

# Поле для ввода суммы
amount_label = ttk.Label(root, text="Введите сумму:")
amount_label.pack(**padding)

amount_entry = ttk.Entry(root)
amount_entry.pack(**padding)

# Кнопка для выполнения конвертации
convert_button = ttk.Button(root, text="Конвертировать", command=perform_conversion)
convert_button.pack(**padding)

# Метка для отображения результата
result_label = ttk.Label(root, text="Результат:")
result_label.pack(**padding)

# Запуск главного цикла программы
root.mainloop()
