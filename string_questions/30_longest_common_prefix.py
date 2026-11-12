# def longest_common_prefix(words):
#     if not words:
#         return ""
#     if len(words) == 1:
#         return words[0]
#     flag = True
#     prefix = words[0][0]
#     for i in range(1, len(words[0])):
        
#         for element in words:
#             if not element.startswith(prefix):
#                 return prefix[:i-1]
#         else:
#             prefix+= words[0][i]


# words = ["Flower", "Flight"]
# print(longest_common_prefix(words))

words = ["Flower", "Flow", "Flight"]

def longest_common_prefix(words):
    word = ""

    for ch in words[0]:
        word += ch

        for i in words[1:]:
            if not i.startswith(word):
                return word[:-1]

    return word

print(longest_common_prefix(words))
