import pandas as pd #handing data
from colorama import Fore, init 
import time
import sys
from textblob import Textblob #sentiment of a movie
from sklearn.feature_extraction.text import TfidfVectorizer # convert movie descp. into numertic data
from sklearn.metrics.pairwise import cosine_similarity # deside how similar movies are

init(autoreset=True)

# Load and preprocess the dataset
def load_data(file_path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()
movies_df = load_data()

# Vectorize the combined features and compute cosine similarity
tfidf=TfidfVectorizer(stop_words="english")
tfidf_metrics=tfidf.fit_transform(movies_df["combined_features"])
cosineSimilarity=cosine_similarity(tfidf_metrics, tfidf_metrics)

# List all unique genres
def listGenres(data):
    return sorted(set(genre.strip()for sublist in data["Genre"].dropna().str.split(", ") for genre in sublist))
genre=listGenres(movies_df)

# Recommend movies based on filters (genre, mood, rating)
def displayRecommendations(recommendation, name):
    print(f"\n Ai Analyze Movie Recommendation for {name}.")
    for index, (title, polarity) in enumerate(recommendation, 1):
        sentiment="postive" if polarity>0 else "negative" if polarity<0 else "Neutral"
        print(f"{index}.{title}(polarity):{polarity:.2f}{sentiment}")

# Display recommendations🍿 😊  😞  🎥
def recommendMovies(genre=None, mood=None, rating=None, top5=5):
    filterData=movies_df 
    if genre:
        filterData=filterData[filterData["Genre"].str.contains(genre, case=False, na=False)]
    if rating:
        filterData=filterData[filterData["IMBB_Rating"].str.contains(genre, case=False, na=False)]
    filterData=filterData.sample(frac=1).reset_index(drop=True)
    recommendations=[]
    for index, row in filterData.iterrows():
        overview=row["Overview"]
        if pd.isna(overview):
            continue
        polarity=Textblob(overview).sentiment.polarity
# Small processing animation


# Handle AI recommendation flow 🔍


    # Processing animation while analyzing mood 😊  😞  😐
    
    # Processing animation while finding movies
    
      # Small processing animation while finding movies 🎬🍿

   
# Main program 🎥
