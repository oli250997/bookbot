def get_num_words(string):
    count = string.split()
    count = len(count)
    return count

def get_char_count(string):
    string = string.lower()
    dict = {}
    for char in string:
        if char in dict:
            dict[char] = dict[char]+1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def analyse(dict):
    list = []
    for entry in dict:
        list.append({"name":entry,"num":dict[entry]})
    list.sort(reverse=True, key=sort_on)
    
    return list