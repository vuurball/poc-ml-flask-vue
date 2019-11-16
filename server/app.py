from flask import Flask, jsonify
from flask_cors import CORS
import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#conf
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong')

@app.route('/movies', methods=['GET'])
def index():
    movies_json = {}
    with open('db/movies.csv', mode='r') as data:
        movies = csv.reader(data)
        id = -1
        for row in movies:
            if id != -1:
                movies_json[id] = row[1]
            if id > 10:
                break    
            id += 1
        
    return jsonify(movies_json)


def get_title_from_index(df, i):
    return df.iloc[[i]].Title.values[0]


def get_index_from_title(df, title):
    try:
        return df[df.Title == title].index.values[0]
    except IndexError:
        return 0 # if not found


# putting more weight on films with same actors, than by genre or description
def concat_columns(row):
    return row['Actors'] +" "+ row['Actors'] +" "+ row['Description'] +" "+ row['Genre']


@app.route('/movies/<slug>', methods=['GET'])
def show(slug):
    similar_to_i = slug

    df = pd.read_csv('db/movies.csv')
    df.fillna('', inplace=True)
            
    # df.apply will run the concat_columns() func on each row (axis=1)
    df['features'] = df.apply(concat_columns, axis=1)
    model = CountVectorizer()
    count_matrix = model.fit_transform(df['features'])
    cosine_sim = cosine_similarity(count_matrix)

    similar_movies = list(enumerate(cosine_sim[int(similar_to_i)]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)

    i=1
    movies_json = {}
    for movie in sorted_similar_movies[1:11]:
        movies_json[i-1] = {'name': get_title_from_index(df, movie[0])}
        i+=1
 
    return jsonify(movies_json)


if __name__ == '__main__':
    app.run()