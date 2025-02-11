import re
from collections import Counter

text = "  //wont won't won't "

words = re.findall(r"[a-zA-Z']+", text.lower())


words = [word for word in words if re.search(r"[a-zA-z]", word)]

print(words)

count = Counter(words)

print(count)


print([word for word, _ in count.most_common(3)])



# text = text.replace(" ", "") 

# count = {}
# result = []

# for i in text:
#     count[i] = count.get(i, 0) + 1

# # sorted_data = dict(sorted(count.items()))

# # print(sorted_data)

# sorted_count = sorted(count.items(), key=lambda item: item[1])

# for key, value in sorted_count[-3:]:
#     result.append(key)
# print(result)
