text = "Python is easy and Python is fun and I love Python"

# 1. lowercase and split into a list
text = text.lower()
words = text.split()
print(words)

# 2. total number of words
print("Total words:", len(words))

# 3. convert to set, count unique words
unique_words = set(words)
print(unique_words)
print("Unique words:", len(unique_words))

# 4. dictionary that counts each word
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

# 5. words that appear more than once
for word, times in count.items():
    if times > 1:
        print(word, times)

# 6. words in the set longer than 3 letters
for word in unique_words:
    if len(word) > 3:
        print(word)






