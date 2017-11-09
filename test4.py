import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer ,WordNetLemmatizer

#nltk.download('stopwords')


example_sent = "This is a sample sentence, showing off the stop words filtration. my name is mayank."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

stemmer = PorterStemmer()
lemma =WordNetLemmatizer()
filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(lemma.lemmatize(str(stemmer.stem(w))))
test=''
for x in filtered_sentence:
    if x == '.':
        test+=x+'\n'
    else:
        test+=x+' '

print(word_tokens)
print(filtered_sentence)
print test