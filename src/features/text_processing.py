import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

df = pd.read_csv("./data/processed/Mental_health_cleaned_data.csv")

def clean_text(text):
    """
    Function to clean text by removing URLs, special characters, and optional lowercase conversion.
    """
    text = re.sub(r"http\S+|www.\S+", "", text)  # Remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return text

def tokenize_text(text):
    """
    Function to tokenize text into words.
    """
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    """
    Function to remove stop words from tokens.
    """
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def lemmatize_tokens(tokens):
    """
    Function to lemmatize tokens.
    """
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized_tokens

df['Cleaned_Content'] = df['Cleaned_Content'].apply(clean_text)
df['Tokens'] = df['Cleaned_Content'].apply(tokenize_text)
df['Tokens_No_Stop'] = df['Tokens'].apply(remove_stopwords)
df['Lemmatized'] = df['Tokens_No_Stop'].apply(lemmatize_tokens)
