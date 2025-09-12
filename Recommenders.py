import numpy as np
import pandas
from sklearn.model_selection import train_test_split
import numpy as np
import time
import joblib
import time


    

#Class for Item similarity based Recommender System model
class item_similarity_recommender_py:
    #Create the item similarity based recommender system model
    def __init__(self, train_data, user_id, item_id):
        self.train_data = train_data
        self.user_id = user_id
        self.item_id = item_id
  
        
    #Get unique items (songs) corresponding to a given user
    def get_user_items(self, user):
        user_data = self.train_data[self.train_data[self.user_id] == user]
        user_items = list(user_data[self.item_id].unique())
        
        return user_items
        
    #Get unique users for a given item (song)
    def get_item_users(self, item):
        item_data = self.train_data[self.train_data[self.item_id] == item]
        item_users = set(item_data[self.user_id].unique())
            
        return item_users
    
    # Obtain unique songs in the training data
    def get_all_items_train_data(self):
        all_items = list(self.train_data[self.item_id].unique())

        return all_items
        
    # Make a coocurrence matrix
    def construct_cooccurence_matrix(self, inputSong, all_songs):
            
        # Obtain the user IDs of those who ranked songs that are the same as the songs that the user inputted 
        user_songs_users = []        
        for i in range(len(inputSong)):
            user_songs_users.append(self.get_item_users(inputSong[i]))
            
        # Make a cooccurence matrix 
        cooccurence_matrix = np.matrix(np.zeros(shape=(len(inputSong), len(all_songs))), float)
           
        # Calculate similarity 
        for i in range(len(all_songs)):
            # Obtain a set of unique user IDs of those who listened to a song (song refers to the list of unique values in the training data under the song column)
            songs_i_data = self.train_data[self.train_data[self.item_id] == all_songs[i]]
            users_i = set(songs_i_data[self.user_id].unique())
            
            for j in range(len(inputSong)):       
                    
                # Take a user ID from user_songs_users
                users_j = user_songs_users[j]
                    
                # Compare the user ID from user_songs_users with the user IDs in the set
                users_intersection = users_i.intersection(users_j)
                
                if len(users_intersection) != 0:
                    # Find the union of the two user IDs
                    users_union = users_i.union(users_j)
                    
                    cooccurence_matrix[j,i] = float(len(users_intersection))/float(len(users_union))
                else:
                    cooccurence_matrix[j,i] = 0
                    
        
        return cooccurence_matrix

    
    # Use cooccurence matrix to generate recommendations 
    def generate_top_recommendations(self, user, cooccurence_matrix, all_songs, inputSong):
        print("Non zero values in cooccurence_matrix :%d" % np.count_nonzero(cooccurence_matrix))
        
        
        # Calculate a recommendation score
        user_sim_scores = cooccurence_matrix.sum(axis=0)/float(cooccurence_matrix.shape[0])
        
        user_sim_scores = np.array(user_sim_scores)[0].tolist()
 
        # Sort the scores from highest to lowest
        sort_index = sorted(((e,i) for i,e in enumerate(list(user_sim_scores))), reverse=True)
    
        # Make a new dataframe
        columns = ['user_id', 'song', 'score', 'rank']
        df = pandas.DataFrame(columns=columns)
         
        # Add top 10 highest scores to dataframe
        rank = 1 
        for i in range(len(sort_index)):
            if ~np.isnan(sort_index[i][0]) and all_songs[sort_index[i][1]] not in inputSong and rank <= 10:
                df.loc[len(df)]=[user,all_songs[sort_index[i][1]],sort_index[i][0],rank]
                rank += 1
        
        # Error checking
        if df.shape[0] == 0:
            print("The current user has no songs for training the item similarity based recommendation model.")
            return -1
        else:
            return df
 


    
    # Get similar songs to those that the user inputs
    def get_similar_items(self, inputSong):
        
        # Obtain unique songs in the training data
        all_songs = self.get_all_items_train_data()
        
        print("no. of unique songs in the training set: %d" % len(all_songs))
         
        # Make a cooccurence matrix
        cooccurence_matrix = self.construct_cooccurence_matrix(inputSong, all_songs)
        
        # Use cooccurence matrix to generate recommendations 
        user = ""
        df_recommendations = self.generate_top_recommendations(user, cooccurence_matrix, all_songs, inputSong)
         
        return df_recommendations
        

def init(inputSong):
    # triplets_file consists of a "triplet" of data (user id, song id, listen count)
    triplets_file = "data/test2/10000.txt"
    songs_metadata_file = 'data/test2/song_data.csv'

    # read table and define columns
    song_df_1 = pandas.read_table(triplets_file,header=None)
    song_df_1.columns = ['user_id', 'song_id', 'listen_count']

    # read song metadata
    song_df_2 =  pandas.read_csv(songs_metadata_file)
    # clean data to remove rows with duplicate songs
    song_df_2 = song_df_2.drop_duplicates(['song_id'])


    # merge the two dataframes above to create input dataframe for recommender systems
    # keep the triplet data's song id, drop the duplicate column of "song_id" in the song data's file
    song_df = pandas.merge(song_df_1, song_df_2, on="song_id", how="left") 

    # subset consists of first 10000 songs
    song_df = song_df.head(150000)

    
    song_df['song'] = song_df['title'].map(str) 

    # alternatively, you can: 
    # merge song title and artist_name columns to make a merged column
    # because this recommender only recommends songs; we don't need artists
    #song_df['song'] = song_df['title'].map(str) + " - " + song_df['artist_name']


    
    # using scikit-learn to split data into training and testing data
    # test_size = 0.20: Testing size is 20% => training size is 80%
    train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)

    
    # make an item similarity recommender
    is_model = item_similarity_recommender_py(train_data, "user_id", "song")

    # predict what song you would like based on a song that you input
    df = is_model.get_similar_items(inputSong)

    print(df.loc[0]['song'])
    print(df)
    
    return df    

if __name__ == "__main__":
    # record time
    startTime = time.time()
    init(["Love Story"])
    print("Total time elapsed: " + str(time.time() - startTime))
    

    
  
