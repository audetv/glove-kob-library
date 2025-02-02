import os

def sort_and_save_vocab(input_file, output_file=None):
    """
    Сортирует словарь по алфавиту и сохраняет его.
    
    :param input_file: Путь к файлу словаря (формат: "слово частота").
    :param output_file: Путь для сохранения отсортированного словаря. Если None, перезаписывает исходный файл.
    """
    # Проверка и создание папки, если она не существует
    if output_file:
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

    # Чтение словаря
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Разделение на слова и частоты
    vocab = []
    for line in lines:
        word, freq = line.strip().split(maxsplit=1)
        vocab.append((word, int(freq)))

    # Сортировка по алфавиту
    vocab_sorted = sorted(vocab, key=lambda x: x[0])

    # Сохранение отсортированного словаря
    if output_file is None:
        output_file = input_file  # Перезапись исходного файла

    with open(output_file, 'w', encoding='utf-8') as file:
        for word, freq in vocab_sorted:
            file.write(f"{word} {freq}\n")

    print(f"Словарь отсортирован и сохранён в {output_file}")

# Пример использования
if __name__ == "__main__":
    vocab_file = "model/vocab.txt"  # Путь к файлу словаря
    sort_and_save_vocab(vocab_file, "model/vocab_sorted.txt")  # Сортировка и пересохранение