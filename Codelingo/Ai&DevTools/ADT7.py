import pandas as pd #handing data
from colorama import Fore, init 
import time
import sys
from textblob import TextBlob #sentiment of a movie
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
def recommendMovies(genre=None, mood=None, rating=None, topN=5):
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
        polarity=TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity<0 and polarity>0)or polarity >=0)) or not mood:
            recommendations.append((row["Series_Title"], polarity))
        if len(recommendations)==topN:
            break
    return recommendations if recommendations else "No Suitable Movie Recommedations Found"
# Small processing animation
def processAnimation():
    for i in range(3):
        print(Fore.YELLOW+".",end="", flush=True)
        time.sleep(0.5)
# Handle AI recommendation flow 🔍
def handleAI(name):
    print("Let's find the perfect movie for you.")
    print("Avilable Genres:")
    for index, i in enumerate(genre, 1):
        print(f"{index}.{i}")
    print()
    while True:
        genreInput=input("Enter Genre Name or Number: ").strip()
        if genreInput.isdigit() and 1<= int(genreInput)<=len(genre):
            g=genre[int(genreInput)-1]
            break
        elif genre.title() in genre:
            g=genreInput.title()
            break
        print("Invalid Input\n Try Again")
    moodInput=input("What do you feel today? Discribe your mood: ").strip()
    # Processing animation while analyzing mood 😊  😞  😐
    print("Analyzing Mood", end="", flush=True)
    processAnimation()
    polarity=TextBlob(moodInput).sentiment.polarity
    moodDiscribtion="Postive"
    print(f"Your mood is {moodDiscribtion} (polarity:{polarity:.2f})")
    while True:
        ratingInput=input("Enter Minimun IMBB Rating or Skip").strip()
        if ratingInput.lower()=="skip":
            ratingInput=None
            break
        try:
            rating=float(ratingInput)
            if 7.6<=rating<=9.3:
                break
            print("Rating Out Of Range \n Try Again.")
        except ValueError:
            print("Invalid Input \n Try Again.")
    # Processing animation while finding movies
    print(f"Finding Movie for {name}.", end="", flush=True)
    processAnimation()
    recommend=recommendMovies(genre=g,mood=moodInput,rating=rating,topN=5)
    if isinstance(recommend,str):
        print(recommend)
    else:
        displayRecommendations(recommend, name)
 # Small processing animation while finding movies 🎬🍿
    while True:
        action=input("Would You Like More Recommendations (Yes/No): ").strip().lower()
        if action=="no":
            print("Enjoy Your Movie Picks")
            break
        elif action=="yes":
            recommend=recommendMovies(genre=g,mood=moodInput,rating=rating,topN=5)
            if isinstance(recommend,str):
                print(recommend)
            else:
                displayRecommendations(recommend, name)
        else:
            print("Invaid Choice \n Try Again")
# Main program 🎥
print("Welcome To Your Personal Movie Recommendation Assitant")
name=input("What is your name? ").strip()
print(f"Great to meet you {name}!")
handleAI(name)