from nltk.tokenize import word_tokenize
 
# create bag-of-words
all_words = []
 
for message in processed:
    words = word_tokenize(message)
    for w in words:
        all_words.append(w)
         
all_words = nltk.FreqDist(all_words)
def find_features(message):
    words = word_tokenize(message)
    features = {}
    for word in word_features:
        features[word] = (word in words)
    return features
features = find_features(processed[0])
for key, value in features.items():
    if value == True:
        print(key)
