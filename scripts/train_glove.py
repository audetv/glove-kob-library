import subprocess
from config.settings import PREPROCESSED_CORPUS_FILE, VOCAB_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS

def train_glove(input_file, vocab_file, output_file, vector_size, window_size, iterations, threads):
    command = [
        './glove/glove',
        '-input-file', input_file,
        '-vocab-file', vocab_file,
        '-save-file', output_file,
        '-vector-size', str(vector_size),
        '-window-size', str(window_size),
        '-iter', str(iterations),
        '-threads', str(threads),
        '-verbose', '2'
    ]
    
    subprocess.run(command)

if __name__ == "__main__":
    train_glove(PREPROCESSED_CORPUS_FILE, VOCAB_FILE, VECTORS_FILE, GLOVE_VECTOR_SIZE, GLOVE_WINDOW_SIZE, GLOVE_ITERATIONS, GLOVE_THREADS)
    print(f"Эмбеддинги обучены и сохранены в {VECTORS_FILE}")