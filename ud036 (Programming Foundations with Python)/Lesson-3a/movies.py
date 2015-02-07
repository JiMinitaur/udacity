import webbrowser

class Movie:

    # Property aliases provide flexibility during get/set operations,
    # while ensuring that only the expected properties are included.
    property_aliases = {
        'title' : ['name', 'id']
    ,   'storyline' : ['story', 'description', 'plot']
    ,   'poster_link' : ['poster', 'poster_image_url']
    ,   'trailer_link' : ['trailer', 'youtube', 'trailer_youtube_url']
    }

    # Gets the list of canonical property titles
    @staticmethod
    def list_props():
        return Movie.property_aliases.keys()

    # Gets the canonical title of the property alias
    @staticmethod
    def deduce_prop(alias):
        # Scan canonical properties for a match / alias and return key
        for key, value in Movie.property_aliases.iteritems():
            if key == alias or alias in value:
                return key
        print("!! property alias not found : "+alias)
        return None


    def __init__(self, props):
        # An internal dictionary provides dynamic property behavior
        self.__props = dict()
        for key, value in props.iteritems():
            self.set_prop(key, value)


    def set_prop(self, key, value):
        # The canonical key is used to set the value
        # to prevent rogue entries and searching.
        alias = Movie.deduce_prop(key)
        self.__props[alias] = value
    
    def __getattr__(self, prop):
        # For unresolved properties, if there is an alias,
        # retrieve the value with the canonical key
        alias = Movie.deduce_prop(prop)
        if alias == None:
            return None
        else:
            return self.__props[alias]

    def __str__(self):
        # Get the string description of the dynamic property container.
        return str(self.__props)

    def show_trailer(self):
        trailer = self.trailer
        print("Playing trailer: " + trailer)
        webbrowser.open(trailer)
