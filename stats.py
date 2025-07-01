def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    freq = {}
    for char in book_text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def sort_characters(freq):
    sorted_list = []
    for char, count in freq.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    # Sort by 'num' in descending order
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    
    return sorted_list

