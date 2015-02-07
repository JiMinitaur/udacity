# Udacity Nanodegree - Full Stack Developer 
## Project 1 - Movie Trailer Website

### Overview

Having extensive background in programming, but little in Python, I decided to integrate cleaner and more modular paradigms into the assignment, and get familiar with common activities using Python in particular.

Key aspects of this implementation:

* `movies.py` defines the Movie class.  Rather than use a long winded constructor, I used a single-parameter property object.
  * I used a dictionary, because it allows insensitive ordering, and multiple naming conventions.
  * Within the class, aliases are resolved to the expected property id, so that they are stored under a single key.
  * `__getattr__` is used to provide 'dynamic proxy' capability, i.e. attribute calls that don't resolve are deferred to the magic function.  The function resolves the property id to a dictionary key, and returns the value.  This has the added benefit of any valid alias for the dictionary keys also being a valid property.

* `movie_library.py`:
  * loads the dictionaries fed to `Movie(dict)` from JSON file `movies.json` and feeds the movie list into the provided web page generator (`fresh_tomatoes.py`).  
  * Using dictionary as the constructor object proved fruitful here, as the constructor could also be used as a decoding callback.  The result is that a single called to the standard library decoder automatically constructs the objects from the JSON.  The aliasing applied in `movies.py` is still applicable in the JSON.

* `fresh_tomatoes.py` was provided.  The only edit I made was to include my snarky descriptions in the rendered output.

### Usage

Simply run `movie_library.py`.  It will process the data from `movies.json` and feed it `fresh_tomatoes.py`, which it turns will render the page and open it in a web browser.


