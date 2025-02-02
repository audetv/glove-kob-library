import logging
from scripts.create_corpus import create_corpus
from scripts.preprocess import preprocess_corpus
from scripts.build_vocab_with_razdel import main as build_vocab
from scripts.sort_vocab import sort_and_save_vocab
from scripts.train_glove import train_glove
from config.settings import RAW_DATA_DIR, CORPUS_FILE, PREPROCESSED_CORPUS_FILE, VOCAB_FILE, LOG_FILE

# Настройка логирования
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Создание корпуса...")
    create_corpus(RAW_DATA_DIR, CORPUS_FILE)

    logging.info("Предобработка текста...")
    preprocess_corpus(CORPUS_FILE, PREPROCESSED_CORPUS_FILE)

    logging.info("Создание словаря...")
    build_vocab()

    logging.info("Сортировка словаря...")
    sort_and_save_vocab(VOCAB_FILE)

    logging.info("Обучение модели GloVe...")
    train_glove()

    logging.info("Проект завершён.")

if __name__ == "__main__":
    main()