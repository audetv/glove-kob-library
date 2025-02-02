import re
import logging
from config.settings import CORPUS_FILE, PREPROCESSED_CORPUS_FILE, LOG_FILE

# Настройка логирования
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_text(text):
    """
    Предобработка текста:
    - Приведение к нижнему регистру.
    - Удаление непечатаемых символов (например, <0x02>, <0x15>).
    - Замена неразрывных пробелов (включая <0xa0>) на обычные пробелы.
    - Удаление более двух повторяющихся переносов строк.
    """
    # Приведение к нижнему регистру
    text = text.lower()

    # Удаление непечатаемых символов (управляющие символы и другие)
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)  # Удаляем управляющие символы

    # Замена неразрывных пробелов на обычные пробелы
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
    logging.info("Начата предобработка корпуса.")
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            processed_line = preprocess_text(line)
            outfile.write(processed_line)
    logging.info("Предобработка корпуса завершена. Результат сохранён в %s", output_file)

def check_processed_corpus(file_path):
    """
    Проверка предобработанного корпуса на наличие непечатаемых символов.
    """
    logging.info("Проверка предобработанного корпуса на непечатаемые символы.")
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            if re.search(r'[\x00-\x1F\x7F]', line):
                logging.warning("Найдены непечатаемые символы в строке %d: %s", line_num, line.strip())
    logging.info("Проверка завершена.")

if __name__ == "__main__":
    # Предобработка корпуса
    preprocess_corpus(CORPUS_FILE, PREPROCESSED_CORPUS_FILE)

    # Проверка предобработанного корпуса
    check_processed_corpus(PREPROCESSED_CORPUS_FILE)