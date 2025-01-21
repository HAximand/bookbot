def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print("--- Begin report of books/frankenstein.txt ---")

        print(len(words), "words found in the document")
        counts = char_count(file_contents)
        counts_list = list(counts.values())
        counts_list.sort(reverse=True)

        used_chars = [""]

        for count in counts_list:
            char = ""
            i = -1
            while char in used_chars:
                # Find the index 
                i = list(counts.values()).index(count, i + 1)
                chars = list(counts.keys())
                char = chars[i]
            
            if char not in used_chars:
                used_chars.append(char)

            if char.isalpha(): print(f"The '{char}' character was found {counts[chars[i]]} times")
        
        print("--- End report ---")

def char_count(text):
    counts = {}
    for character in text:
        c = character.lower()
        if c not in counts.keys():
            counts[c] = 0
        counts[c] += 1
    return counts

main()