from sklearn.feature_extraction.text import TfidfVectorizer


tfidf_vectorizer = TfidfVectorizer(max_features=1000)  

# Fit the vectorizer on the training data (during training)
# tfidf_vectorizer.fit(train_texts)

# Transform your input text to match the model's expected input
def preprocess_input(input_text: list):
    transformed_input = tfidf_vectorizer.transform(input_text)
    return transformed_input

