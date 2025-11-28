def count_words(list):
    words = list.split()
    return len(words)

def count_characters(list):
    lowered = list.lower()
    counted = {}
    for li in lowered:
        if li in counted:
            counted[li] += 1
        else:
            counted[li] = 1
    return counted

def sort_on(item):
    return item["num"]

def sort_characters(list):
    sorted_list = []
    for li in list:
        if li.isalpha():
            sorted_list.append({"char": li, "num": list[li]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list