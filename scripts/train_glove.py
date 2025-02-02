import subprocess
import os
from config.settings import PREPROCESSED_CORPUS_FILE, VOCAB_FILE, COOCCUR_FILE, SHUFFLED_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS, LOG_FILE
import logging

# Настройка логирования
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_cooccur(corpus_file, vocab_file, cooccur_file, window_size, memory=8.0):
    """
    Запускает утилиту cooccur для создания файла совместного появления слов.
    """
    command = [
        './glove/cooccur',
        '-memory', str(memory),
        '-vocab-file', vocab_file,
        '-verbose', '2',
        '-window-size', str(window_size),
    ]
    logging.info("Запуск cooccur...")
    with open(corpus_file, 'r') as infile, open(cooccur_file, 'w') as outfile:
        subprocess.run(command, stdin=infile, stdout=outfile, check=True)
    logging.info(f"Файл совместного появления слов сохранён в {cooccur_file}")

def run_shuffle(cooccur_file, shuffled_file, memory=8.0):
    """
    Запускает утилиту shuffle для перемешивания данных.
    """
    command = [
        './glove/shuffle',
        '-memory', str(memory),
        '-verbose', '2',
    ]
    logging.info("Запуск shuffle...")
    with open(cooccur_file, 'r') as infile, open(shuffled_file, 'w') as outfile:
        subprocess.run(command, stdin=infile, stdout=outfile, check=True)
    logging.info(f"Перемешанный файл сохранён в {shuffled_file}")

def run_glove(shuffled_file, vocab_file, vectors_file, vector_size, window_size, iterations, threads, x_max=100.0):
    """
    Запускает утилиту glove для обучения модели.
    """
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
    subprocess.run(command, check=True)
    logging.info(f"Эмбеддинги сохранены в {vectors_file}")

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
        run_glove(SHUFFLED_FILE, VOCAB_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS)

        logging.info("Обучение модели завершено.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Ошибка при выполнении команды: {e}")
    except Exception as e:
        logging.error(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    train_glove()