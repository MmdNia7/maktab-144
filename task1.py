#1
def word_frequency(text):
    try:
        words = text.split()
        dic = {}
        for word in words:
            dic[word] = text.count(word)
        sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        final_list = []
        for item in sorted_items:
            w = item[0]
            count = item[1]
            final_list.append((w,count))
        return final_list
    except ValueError:
        print("Error")

text = "python is great and python is powerful and python is fun"
print(word_frequency(text))

