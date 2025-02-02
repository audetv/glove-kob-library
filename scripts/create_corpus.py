import os
from config.settings import RAW_DATA_DIR, CORPUS_FILE

def create_corpus(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read() + '\n')

if __name__ == "__main__":
    create_corpus(RAW_DATA_DIR, CORPUS_FILE)
    print(f"Корпус создан и сохранен в {CORPUS_FILE}")