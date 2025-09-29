import streamlit as st
import pickle 
import pandas as pd 
import requests



def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances =  similarity[movie_index]
    movies_list =sorted(list(enumerate(distances)),reverse=True, key =lambda x:x[1])[1:6]
    
    recommended_movies =[]

    for i in movies_list:
        for i in movies_list:
            movie_id =i[0]
            url = f"http://www.omdbapi.com/?i={movie_id}&apikey={API_KEY}"
            response = requests.get(url)
            data = response.json()
            print(data)
            #fetch api for poster 
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
       

similarity= pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movies Recommendation System')
Selected_movies_name = st.selectbox(
    'how would you like to be contacted',
    movies['title'].values)

if st.button('Recommend'):
    recommendation=recommend(Selected_movies_name)
    for i in  recommendation:
        st.write(i)

