import webbrowser


class Movie:
    '''Initializing values of instances'''
    # VALID_RATINGS = ["G","PG","PG-13","R"] # Class variable   
    def __init__(movie_inst, title, storyline, posterimg, trailer, rating):
        movie_inst.title = title
        movie_inst.storyline = storyline
        movie_inst.posterimg = posterimg
        movie_inst.trailer = trailer
        movie_inst.rating = rating 
        
    def show_trailer(movie_instance):
        webbrowser.open(movie_instance.trailer) 
