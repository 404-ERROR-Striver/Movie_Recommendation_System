import numpy as np
import ast
import pandas as pd
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
print(new_df)

