from collections import Counter
from config.settings import PREPROCESSED_CORPUS_FILE, VOCAB_FILE

def create_vocabulary(corpus_file, vocab_file, min_count=1):
    word_counts = Counter()
    
    with open(corpus_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            words = line.split()
            word_counts.update(words)
    
    with open(vocab_file, 'w', encoding='utf-8') as outfile:
        for word, count in word_counts.items():
            if count >= min_count:
                outfile.write(f"{word} {count}\n")

if __name__ == "__main__":
    create_vocabulary(PREPROCESSED_CORPUS_FILE, VOCAB_FILE)
    print(f"Словарь создан и сохранен в {VOCAB_FILE}")