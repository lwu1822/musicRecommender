# import pandas as pd
# from sklearn.metrics.pairwise import sigmoid_kernel
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn import preprocessing

# df=pd.read_csv("data.csv")
# # Just top 30000 popular songs because of memory issue when size is too big
# df = df.sort_values(by='popularity', ascending=False).iloc[:30000]

# feature_cols=['acousticness', 'danceability', 'duration_ms', 'energy',
#               'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
#               'speechiness', 'tempo', 'valence',]

# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# normalized_df =scaler.fit_transform(df[feature_cols])

# # Create a pandas series with song titles as indices and indices as series values 
# indices = pd.Series(df.index, index=df['name']).drop_duplicates()

# # Create cosine similarity matrix based on given matrix
# cosine = cosine_similarity(normalized_df)

# """
# Purpose: Function for song recommendations 
# Inputs: song title, number of recommendations to give, and type of similarity model
# Output: list of recommended songs
# """
# def generate_recommendation(name, n, model_type=cosine):
#     # Get song indices
#     index=indices[name]
#     # Get list of songs for given songs
#     score=list(enumerate(model_type[index]))
#     # Sort the most similar songs
#     similarity_score = sorted(score,key = lambda x:x[1],reverse = True)
#     # Select the top-n recommend songs
#     similarity_score = similarity_score[1:n+1]
#     top_songs_index = [i[0] for i in similarity_score]
#     # Top 10 recommended songs
#     top_songs=df['name'].iloc[top_songs_index]
#     return top_songs.tolist()

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("data.csv")

# Take top 30,000 popular songs to reduce memory
df = df.sort_values(by='popularity', ascending=False).iloc[:30000]

# Feature columns for similarity
feature_cols = [
    'acousticness', 'danceability', 'duration_ms', 'energy',
    'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
    'speechiness', 'tempo', 'valence'
]

# Normalize features
scaler = MinMaxScaler()
normalized_df = scaler.fit_transform(df[feature_cols])

# Map song names to indices
indices = pd.Series(df.index, index=df['name']).drop_duplicates()

# -------------------------------
# Recommendation function
# -------------------------------

def generate_recommendation(name, n=10):
    """
    Generate top-n song recommendations for a given song.
    
    Parameters:
        name (str): Song title
        n (int): Number of recommendations
    Returns:
        list of recommended song titles
    """
    # Get index of the requested song
    index = indices[name]

    # Compute similarity of this song to all songs (1 × N)
    song_vector = normalized_df[index:index+1]  # shape (1, features)
    similarity_scores = cosine_similarity(song_vector, normalized_df)[0]

    # Get indices of top-n similar songs, excluding the song itself
    top_indices = similarity_scores.argsort()[::-1][1:n+1]

    # Return top-n song titles
    return df['name'].iloc[top_indices].tolist()
