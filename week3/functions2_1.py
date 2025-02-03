# Dictionary of movies
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_high_rated(movie):
    return movie.get('imdb', 0) > 5.5 # return True if the movie's rating is greater than 5.5, False otherwise

def high_rated_movies(movies):
    return [movie for movie in movies if movie.get('imdb', 0) > 5.5] # return a list of movies with a rating greater than 5.5

def movies_by_category(movies, category):
    return [movie for movie in movies if movie.get('category') == category] # return a list of movies with the specified category

print(is_high_rated(movies[1])) # accessing the second movie in the list
print(is_high_rated(movies[9])) # accessing the tenth movie in the list

print("High-rated movies with IMDB score more than 5.5:")
print(high_rated_movies(movies)) # get the list of high-rated movies

category_name = str(input("Enter the category to see related movies: ")) # get the category name from the user
filtered_movies = movies_by_category(movies, category_name) # get the list of movies with the specified category
for movie in filtered_movies:
    print(f"Name: {movie['name']}, IMDB: {movie['imdb']}") # print the name and IMDB score of each movie with the specified category