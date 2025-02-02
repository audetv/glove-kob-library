import logging
from scripts.create_corpus import create_corpus
from scripts.preprocess import preprocess_corpus
from scripts.build_vocab_with_razdel import main as build_vocab
from scripts.train_glove import train_glove
from config.settings import RAW_DATA_DIR, CORPUS_FILE, PREPROCESSED_CORPUS_FILE, VOCAB_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS, LOG_FILE
from scripts.sort_vocab import sort_and_save_vocab
from config.settings import VOCAB_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Создание корпуса...")
    create_corpus(RAW_DATA_DIR, CORPUS_FILE)
    
    logging.info("Предобработка текста...")
    preprocess_corpus(CORPUS_FILE, PREPROCESSED_CORPUS_FILE)
    
    logging.info("Создание словаря с использованием razdel...")
    build_vocab()

    # Сортировка словаря    
    logging.info("Сортировка словаря...")
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    sort_and_save_vocab(VOCAB_FILE, "model/vocab_sorted.txt")
    
    logging.info("Обучение GloVe...")
    train_glove(PREPROCESSED_CORPUS_FILE, VOCAB_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS)
    
    logging.info("Проект завершен.")

if __name__ == "__main__":
    main()