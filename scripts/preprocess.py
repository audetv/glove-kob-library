import re
from config.settings import CORPUS_FILE, PREPROCESSED_CORPUS_FILE

def preprocess_text(text):
    """
    Предобработка текста:
    - Приведение к нижнему регистру.
    - Замена неразрывных пробелов (включая <0xa0>) на обычные пробелы.
    - Удаление более двух повторяющихся переносов строк.
    """
    # Приведение к нижнему регистру
    text = text.lower()

    # Замена неразрывных пробелов (включая <0xa0>) на обычные пробелы
    text = text.replace('\xa0', ' ')  # Неразрывный пробел
    text = text.replace('\u200b', ' ')  # Нулевой пробел (Zero-width space)
    text = text.replace('\u202f', ' ')  # Узкий неразрывный пробел

    # Удаление более двух повторяющихся переносов строк
    text = re.sub(r'\n{3,}', '\n\n', text)  # Заменяем 3 и более переносов на 2

    return text

def preprocess_corpus(input_file, output_file):
    """
    Предобработка корпуса текста:
    - Чтение текста из входного файла.
    - Применение предобработки к каждой строке.
    - Сохранение результата в выходной файл.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            processed_line = preprocess_text(line)
            outfile.write(processed_line)

if __name__ == "__main__":
    from config.settings import CORPUS_FILE, PREPROCESSED_CORPUS_FILE

    # Предобработка корпуса
    preprocess_corpus(CORPUS_FILE, PREPROCESSED_CORPUS_FILE)
    print(f"Предобработанный корпус сохранён в {PREPROCESSED_CORPUS_FILE}")