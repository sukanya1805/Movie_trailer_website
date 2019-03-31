import movie_website
import media

'''Assigning the values for instances declared in media python file'''
Valid_Ratings = {1: 'Very Poor', 2: 'OK', 3: 'Good'}
Titanic = media.Movie("Titanic",
                      "It is an epic,action packed romance set"
                      "againts ill-fated maiden voyage the RMS Titanic",
                      "titanic-the-movie.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
                      Valid_Ratings[3])

Gullyboy = media.Movie("Gully boy",
                       "A boy from a ghetto in mumbai"
                       "realizes his calling to become a Rapper",
                       "gully_boy.jpg",
                       "https://www.youtube.com/watch?v=JfbxcD6biOk",
                       Valid_Ratings[2])

Alladin = media.Movie("Alladin",
                      "Young Aladdin embarks on a magical adventure after"
                      "finding a lamp that releases a"
                      "wisecracking genie.",
                      "Alladin.jpg",
                      "https://www.youtube.com/watch?v=6NqKrhmnVNY",
                      Valid_Ratings[3])

Avengers = media.Movie("Avengers",
                       "Adrift in space with no food or water,"
                       "Tony sends message to Pepper potts as his"
                       "oxygen supply starts to dwindle"
                       "Meanwhile,the remaining avegers must figure"
                       "out a way to bring them back",
                       "avengers.jpg",
                       "https://www.youtube.com/watch?v=ee1172yeqyE",
                       Valid_Ratings[2])

stm = media.Movie("Sarvam Thalam Mayam",
                  "A story of a dalit youngster Peter Johnson,"
                  "who aspires to learn playing the percussion"
                  "instrument mridangam and enter the gates"
                  "of the Carnatic music world hitherto"
                  "dominated by brahmins.",
                  "stm.jpg",
                  "https://www.youtube.com/watch?v=mqA5T-s8tAw",
                  Valid_Ratings[3])


Lego = media.Movie("lego",
                   "The Lego Movie is an American media franchise"
                   "based on Lego construction toys",
                   "the_lego.jpg",
                   "https://www.youtube.com/watch?v=fZ_JOBCLF-I",
                   Valid_Ratings[1])
# create movie list
movies = [Titanic, Gullyboy, Alladin, Avengers, stm, Lego] 

# Generate html
movie_website.open_movies_page(movies) 
