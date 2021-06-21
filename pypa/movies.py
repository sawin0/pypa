from imdb import IMDb

NO  = '\033[0m'  # white (normal)
RED  = '\033[31m' # red

def format_names(people):
    del people[5:] # Max of 5 people listed
    ret = ''
    for person in people:
        ret += '%s.  ' %person.get('name')
    return ret.strip('. ') 

def handle():
    try:
        ia = IMDb()
        movie_name = raw_input('\nWhich movie? ')
        movie_query = ia.search_movie(movie_name)
        del movie_query[5:]
        for movie in movie_query:
            response = raw_input('\nDid you mean %s (%s)? ' %(movie.get('title'), movie.get('year')))
            if response == 'yes':
                ia.update(movie)
                movie_info = '%s (%s).  ' %(movie.get('title'), movie.get('year'))
                if movie.get('rating'): movie_info += 'Rating.  %s out of 10.  ' %movie.get('rating')
                if movie.get('runtimes'): movie_info += 'Runtime.  %s minutes.  ' %movie.get('runtimes')[0]
                if movie.get('genres'): movie_info += 'Genres.  %s.  ' %'.  '.join(movie.get('genres'))
                if movie.get('plot outline'): movie_info += 'Plot.  %s  ' %movie.get('plot outline')
                if movie.get('director'): movie_info += 'Directors.  %s.  ' %format_names(movie.get('director'))
                if movie.get('producer'): movie_info += 'Producers.  %s.  ' %format_names(movie.get('producer'))
                if movie.get('cast'): movie_info += 'Cast.  %s.  ' %format_names(movie.get('cast'))
                print(movie_info)
                return
                
            print(RED + 'Unable to find information on the requested movie' + NO)
            
    except:
        print(RED + 'An Error Occured!' + NO)
handle()
