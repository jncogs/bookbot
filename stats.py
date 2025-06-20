def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    file_split = file_contents.split()
    return len(file_split)

def count_chars(contents):
    counts = {}
    for c in contents:
        lowered = c.lower()
        if lowered in counts:
            counts[lowered] += 1
        else:
            counts[lowered] = 1
    return counts

def sort_on(items):
    return items["num"]

def report_characters(text):
    sorted_characters = []
    for c in text:
        if c.isalpha():
            temp = {}
            temp["char"] = c
            temp["num"] = text[c]
            sorted_characters.append(temp)
    
    sorted_characters.sort(key=sort_on, reverse=True)
    return sorted_characters