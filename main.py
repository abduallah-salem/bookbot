def read_file(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_case_string = text.lower()
    characters_dict = {}
    for char in lower_case_string:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict


def main():
    path = "books/frankenstein.txt"
    file_contents = read_file(path)
    word_count = count_words(file_contents)
    characters_count = count_characters(file_contents)
    report = (
        f"--- Begin report of {path} ---\n{word_count} words found in the document\n\n"
    )
    for char in characters_count:
        if char.isalpha():
            report += (
                f"The '{char}' character was found {characters_count[char]} times\n"
            )
    report += "--- End report ---"
    print(report)


main()
