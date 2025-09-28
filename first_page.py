import numpy as np
import ast
import pandas as pd
import nltk
movies = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\movie recommendation system\movies.csv")
credits = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\movie recommendation system\tmdb_5000_credits.csv")
# print(movies.head())
# print(credits.head())
movies = movies.merge(credits, on='title')
# print(movies.shape)
movies = movies[['id','title','overview','genres','keywords','popularity','release_date','production_companies']]
movies.isnull().sum()
movies.dropna(inplace=True)
# print(movies)
# print(movies.head())
# print(movies.isnull().sum())
def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
movies['genres']=movies['genres'].apply(convert)   
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x]) 
movies['keywords']=movies['keywords'].apply(convert)
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])  
# print(movies.head())
# print(movies['genres'])

# def convert3(obj):
#     L=[]
#     counter=0
#     for i in ast.literal_eval(obj):
#         if counter!=3:
#             L.append(i['name'])
#             counter+=1
#         else:
#             break
#         return L
# movies['cast']=movies['cast'].apply(convert3)  

def fetch_production(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
        break
    return L
movies['production_companies']=movies['production_companies'].apply(fetch_production)
movies['production_companies']=movies['production_companies'].apply(lambda x:[i.replace(" ","") for i in x]) 
# print(movies['production_companies'])
movies['overview']= movies['overview'].apply(lambda x:x.split())
movies['overview']=movies['overview'].apply(lambda x:[i.replace(" ","") for i in x]) 
movies['tag']= movies['genres']+movies['keywords']+movies['production_companies']+movies['overview']
# print(movies.head())
new_df = movies[['id','title','tag']]
new_df['tag']=new_df['tag'].apply(lambda x:" ".join(x))
new_df['tag']=new_df['tag'].apply(lambda x:x.lower())
# print(new_df)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(new_df['tag']).toarray()
# print(cv.get_feature_names_out())
# print(vector)

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer

def stem(text):
    y=[]

    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)    

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vector)
# print(similarity[0])
sorted(list(enumerate(similarity[0])),reverse=True, key =lambda x:x[1])[1:6]
def recommend(movies):
    movie_index = new_df[new_df['title']==movies].index[0]
    distances =  similarity[movie_index]
    movies_list =sorted(list(enumerate(distances)),reverse=True, key =lambda x:x[1])[1:6]
    

    for i in movies_list:
        print(new_df.iloc[i[0]].title)
       

print(recommend('Avatar'))

import pickle
pickle.dump(new_df,open('movies.pkl','wb'))
pickle.dump(new_df.to_dict(),open('movies_dict.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))