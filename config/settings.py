import os

# Пути к данным
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Имена файлов
CORPUS_FILE = os.path.join(PROCESSED_DATA_DIR, 'corpus.txt')
PREPROCESSED_CORPUS_FILE = os.path.join(PROCESSED_DATA_DIR, 'preprocessed_corpus.txt')
VOCAB_FILE = os.path.join(PROCESSED_DATA_DIR, 'vocab.txt')
VECTORS_FILE = os.path.join(PROCESSED_DATA_DIR, 'vectors.txt')

# Параметры GloVe
GLOVE_VECTOR_SIZE = 100
GLOVE_WINDOW_SIZE = 15
GLOVE_ITERATIONS = 15
GLOVE_THREADS = 8

# Логирование
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'project.log')
