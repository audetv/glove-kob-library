# GloVe KOB Library

Этот проект создает корпус текста, словарь и обучает эмбеддинги слов с использованием GloVe.

## Структура проекта

- `data/raw/`: Исходные текстовые файлы (книги).
- `data/processed/`: Обработанные данные (корпус, словарь, эмбеддинги).
- `scripts/`: Скрипты для создания корпуса, предобработки, создания словаря и обучения GloVe.
- `config/`: Конфигурация проекта.
- `logs/`: Логи выполнения.

## Запуск проекта

1. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```
1. Поместите текстовые файлы (книги) в папку `data/raw/`.

1. Запустите проект:
   ```bash
   python run.py
   ```
Результаты будут сохранены в папке `data/processed/`.

## Сортировкаи словаря

### Пример файла vocab.txt до сортировки:
```
яблоко 100
ананас 50
банан 200
```
После сортировки:

```
ананас 50
банан 200
яблоко 100
```

### Дополнительные улучшения
Сохранение в новый файл:
Если вы не хотите перезаписывать исходный файл, укажите путь для сохранения:

```python
sort_and_save_vocab(VOCAB_FILE, "model/vocab_sorted.txt")
```
### Сортировка по частоте:
Если нужно отсортировать словарь по частоте (в порядке убывания), измените ключ сортировки:

```python
vocab_sorted = sorted(vocab, key=lambda x: -x[1])
```