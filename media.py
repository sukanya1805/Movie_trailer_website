import webbrowser

class Movie:
    '''Initializing values of instances'''
    #VALID_RATINGS = ["G","PG","PG-13","R"] #Class variable
    
    def __init__(movie_instance,movie_title,movie_storyline,movie_poster_image,movie_trailer,movie_rating):
        movie_instance.title = movie_title
        movie_instance.storyline = movie_storyline
        movie_instance.poster_img = movie_poster_image
        movie_instance.trailer = movie_trailer
        movie_instance.rating = movie_rating
        
    def show_trailer(movie_instance):
        webbrowser.open(movie_instance.trailer) 


