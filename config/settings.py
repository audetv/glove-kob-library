import os

# Пути к данным
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# Имена файлов
CORPUS_FILE = os.path.join(PROCESSED_DATA_DIR, 'corpus.txt')
PREPROCESSED_CORPUS_FILE = os.path.join(PROCESSED_DATA_DIR, 'preprocessed_corpus.txt')
VOCAB_FILE = os.path.join(PROCESSED_DATA_DIR, 'vocab.txt')
COOCCUR_FILE = os.path.join(PROCESSED_DATA_DIR, 'cooccurrence.bin')
SHUFFLED_FILE = os.path.join(PROCESSED_DATA_DIR, 'cooccurrence.shuf.bin')
VECTORS_FILE = os.path.join(MODELS_DIR, 'vectors')

# Параметры GloVe
GLOVE_VECTOR_SIZE = 300
GLOVE_WINDOW_SIZE = 10
GLOVE_ITERATIONS = 10
GLOVE_THREADS = 8
GLOVE_X_MAX = 100.0

# Логирование
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'project.log')