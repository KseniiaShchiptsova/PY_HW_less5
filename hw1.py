# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок


txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "галок"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')