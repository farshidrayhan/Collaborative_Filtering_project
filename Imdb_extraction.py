from imdb import IMDb
ia = IMDb()

# get a movie and print its director(s)
the_matrix = ia.get_movie('0133093')
# print(the_matrix['director'])
print(the_matrix['runtimes'][0])
print(the_matrix['year'])


# show all the information sets avaiable for Movie objects
# print(ia.get_movie_infoset())