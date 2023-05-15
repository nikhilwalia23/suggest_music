from flask import Flask,request
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Function to convert the song into Index
def help(z):
    title = z
    count = 1
    for i in (df.track_name):
        if title == i:
            return count
        else:
            count = count + 1

# Load the dataset
df = pd.read_csv('music.csv')

# Select the relevant audio features for the recommendation system
X = df[['release_date', 'dating', 'violence', 'romantic' , 'communication', 'obscene', 'like/girls', 'feelings', 'danceability', 'loudness', 'energy', 'valence', 'age']]
X
# Fit a NearestNeighbors model to find similar songs
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
knn_model.fit(X)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"name":"nikhl Walia","gender":"male"}

@app.route("/about")
def about():
    return "About Page"


@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    songName = data['songName']
    index = help(songName)
    if(index == None):
        return {"error":"Song Not Found"}
    
    sample_song = X.iloc[index]
    
    distances, indices = knn_model.kneighbors([sample_song], n_neighbors=10)
    
    recommended_songs = df.iloc[indices[0]]['track_name']
    songs = dict(recommended_songs)
    return {"songs":songs}