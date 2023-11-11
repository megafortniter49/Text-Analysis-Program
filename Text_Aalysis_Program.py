def analyze_text(text):
    words = text.split()
    total_words = len(words)

    unique_words = set(words)
    total_unique_words = len(unique_words)

    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    most_common_word = max(word_frequencies, key=word_frequencies.get)

    print(f"Total words: {total_words}")
    print(f"Unique words: {total_unique_words}")
    print(f"Most common word: '{most_common_word}'")

text_to_analyze = input("Write a text to analyze: ")
analyze_text(text_to_analyze)