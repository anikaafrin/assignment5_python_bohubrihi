def word_counter(file_path, search_words):
    word_count = {word: 0 for word in search_words}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if word in word_count:
                        word_count[word] += 1

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    print("Word Count:")
    for word, count in word_count.items():
        print(f"{word} -> {count}")


# Example usage:
file_path = "input.txt"
search_words = ["Python", "C", "OOP", "Hello", "Java"]
word_counter(file_path, search_words)
