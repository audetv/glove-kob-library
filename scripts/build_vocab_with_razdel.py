from razdel import tokenize
from collections import Counter
import os
from config.settings import PREPROCESSED_CORPUS_FILE, VOCAB_FILE

def tokenize_corpus(corpus_file):
    """Токенизация корпуса с использованием razdel."""
    tokens = []
    with open(corpus_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Токенизируем каждую строку
            line_tokens = [_.text for _ in tokenize(line)]
            tokens.extend(line_tokens)
    return tokens

def create_vocabulary(tokens, vocab_file, min_count=1):
    """Создание словаря на основе токенов."""
    word_counts = Counter(tokens)
    
    # Сохраняем только токены, встречающиеся не менее min_count раз
    with open(vocab_file, 'w', encoding='utf-8') as file:
        for word, count in word_counts.items():
            if count >= min_count:
                file.write(f"{word} {count}\n")

def main():
    # Токенизация корпуса
    print("Токенизация корпуса...")
    tokens = tokenize_corpus(PREPROCESSED_CORPUS_FILE)
    
    # Создание словаря
    print("Создание словаря...")
    create_vocabulary(tokens, VOCAB_FILE)
    
    print(f"Словарь сохранен в {VOCAB_FILE}")

if __name__ == "__main__":
    main()