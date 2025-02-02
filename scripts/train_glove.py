import subprocess
import os
import logging
from config.settings import PREPROCESSED_CORPUS_FILE, VOCAB_FILE, COOCCUR_FILE, SHUFFLED_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS, LOG_FILE, GLOVE_X_MAX

# Настройка логирования
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_file_exists(file_path):
    """
    Проверяет, существует ли файл.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

def run_cooccur(corpus_file, vocab_file, cooccur_file, window_size, memory=8.0):
    """
    Запускает утилиту cooccur для создания файла совместного появления слов.
    """
    # Проверка существования файлов
    check_file_exists(corpus_file)
    check_file_exists(vocab_file)

    command = [
        './glove/cooccur',
        '-memory', str(memory),
        '-vocab-file', vocab_file,
        '-verbose', '2',
        '-window-size', str(window_size),
    ]
    logging.info("Запуск cooccur...")
    try:
        with open(corpus_file, 'r') as infile, open(cooccur_file, 'w') as outfile:
            subprocess.run(command, stdin=infile, stdout=outfile, check=True)
        logging.info(f"Файл совместного появления слов сохранён в {cooccur_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Ошибка при выполнении команды cooccur: {e}")
        raise
    except Exception as e:
        logging.error(f"Неожиданная ошибка в cooccur: {e}")
        raise

def run_shuffle(cooccur_file, shuffled_file, memory=8.0):
    """
    Запускает утилиту shuffle для перемешивания данных.
    """
    # Проверка существования файлов
    check_file_exists(cooccur_file)

    command = [
        './glove/shuffle',
        '-memory', str(memory),
        '-verbose', '2',
    ]
    logging.info("Запуск shuffle...")
    try:
        with open(cooccur_file, 'r') as infile, open(shuffled_file, 'w') as outfile:
            subprocess.run(command, stdin=infile, stdout=outfile, check=True)
        logging.info(f"Перемешанный файл сохранён в {shuffled_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Ошибка при выполнении команды shuffle: {e}")
        raise
    except Exception as e:
        logging.error(f"Неожиданная ошибка в shuffle: {e}")
        raise

def run_glove(shuffled_file, vocab_file, vectors_file, vector_size, window_size, iterations, threads, x_max=10.0):
    """
    Запускает утилиту glove для обучения модели.
    """
    # Проверка существования файлов
    check_file_exists(shuffled_file)
    check_file_exists(vocab_file)

    command = [
        './glove/glove',
        '-save-file', vectors_file,
        '-threads', str(threads),
        '-input-file', shuffled_file,
        '-x-max', str(x_max),
        '-iter', str(iterations),
        '-vector-size', str(vector_size),
        '-binary', '2',
        '-vocab-file', vocab_file,
        '-verbose', '2',
    ]
    logging.info("Запуск glove...")
    try:
        subprocess.run(command, check=True)
        logging.info(f"Эмбеддинги сохранены в {vectors_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Ошибка при выполнении команды glove: {e}")
        raise
    except Exception as e:
        logging.error(f"Неожиданная ошибка в glove: {e}")
        raise

def train_glove():
    """
    Основная функция для обучения модели GloVe.
    """
    try:
        # Сбор статистики совместного появления слов
        run_cooccur(PREPROCESSED_CORPUS_FILE, VOCAB_FILE, COOCCUR_FILE, GLOVE_WINDOW_SIZE)

        # Перемешивание данных
        run_shuffle(COOCCUR_FILE, SHUFFLED_FILE)

        # Обучение модели
        run_glove(SHUFFLED_FILE, VOCAB_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS, GLOVE_X_MAX)

        logging.info("Обучение модели завершено.")
    except Exception as e:
        logging.error(f"Ошибка при обучении модели: {e}")
        raise

if __name__ == "__main__":
    train_glove()