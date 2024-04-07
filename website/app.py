import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open(r'../movies.pkl', 'rb'))
movies_df = pd.DataFrame(movies)
movies_list = movies_df['title'].values
similarity_df = pickle.load(open(r'../similarity.pkl', 'rb'))


def recommend(movie):
    # Find the index of the movie in the movies_list.
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity_df[movie_index]
    recommended_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in recommended_indices:
        movie_id = i[0]
        #fetch poster from APIs
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Select the kind of movies you want me to recommend from the below list',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
