import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_excel('mentor_data.xlsx')  # Use read_excel for .xlsx files

# Preprocessing
data['techStack'] = data['techStack'].fillna('')
data['specialization'] = data['specialization'].fillna('')
data['profile_text'] = data['specialization'] + " " + data['techStack']

# Convert text data to numerical features using TF-IDF
tfidf = TfidfVectorizer(max_features=100, stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['profile_text']).toarray()

# Add levelOfExperience as a feature
features = np.hstack((tfidf_matrix, data[['levelOfExperience']].values))

# Standardize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# K-means Clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # Adjust n_clusters as needed
mentor_clusters = kmeans.fit_predict(features_scaled)
data['cluster'] = mentor_clusters

# Function to preprocess user input
def preprocess_user_input(specialization, tech_stack, experience_level):
    user_text = f"{specialization} {tech_stack}"
    user_tfidf = tfidf.transform([user_text]).toarray()
    user_features = np.hstack((user_tfidf, [[float(experience_level)]]))
    return scaler.transform(user_features)

# Function to recommend mentors
def recommend_mentors(user_features, top_n=3):
    similarities = cosine_similarity(user_features, features_scaled)[0]
    data['similarity'] = similarities
    top_mentors = data.sort_values(by='similarity', ascending=False).head(top_n)
    return top_mentors[['userName', 'professionalTitle', 'specialization', 'techStack', 'levelOfExperience', 'linkedin', 'combined_reviews', 'similarity']]

# Function to get user input
def get_user_input():
    print("\nEnter your details to find a mentor:")
    specialization = input("Desired Specialization (e.g., Software Engineering, Data Science): ").strip()
    tech_stack = input("Preferred Tech Stack (e.g., Java, Python, React): ").strip()
    experience_level = input("Preferred Mentor Experience Level (e.g., 5 for 5+ years): ").strip()
    return specialization, tech_stack, experience_level

# Function to display mentors
def display_mentors(recommended_mentors):
    print("\nRecommended Mentors:")
    for index, mentor in recommended_mentors.iterrows():
        print(f"\nName: {mentor['userName']}")
        print(f"Professional Title: {mentor['professionalTitle']}")
        print(f"Specialization: {mentor['specialization']}")
        print(f"Tech Stack: {mentor['techStack']}")
        print(f"Experience Level: {mentor['levelOfExperience']} years")
        print(f"LinkedIn: {mentor['linkedin']}")
        print(f"Reviews: {mentor['combined_reviews']}")
        print(f"Similarity Score: {mentor['similarity']:.4f}")
        print("-" * 50)

# Main loop
while True:
    # Get user input and recommend mentors
    specialization, tech_stack, experience_level = get_user_input()
    user_features = preprocess_user_input(specialization, tech_stack, experience_level)
    recommended_mentors = recommend_mentors(user_features)
    display_mentors(recommended_mentors)

    # Ask if user wants to search more
    while True:
        search_more = input("\nDo you want to search more? (Yes/No): ").strip().lower()
        if search_more in ['yes', 'no']:
            break
        print("Please enter 'Yes' or 'No'.")

    if search_more == 'no':
        print("Thank you for using the mentor recommendation system. Goodbye!")
        break  # Exit the program
    # If 'yes', the loop continues for a new search
