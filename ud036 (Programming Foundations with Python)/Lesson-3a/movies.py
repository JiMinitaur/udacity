class Movie:

    # Property aliases provide flexibility when defining the data,
    # while ensuring that only the expected properties are included.
    property_aliases = {
        'title' : ['name', 'id']
    ,   'storyline' : ['story', 'description']
    ,   'poster_link' : ['poster']
    ,   'trailer_link' : ['trailer', 'youtube']
    }

    # Gets the list of canonical property titles
    @staticmethod
    def list_props():
        return Movie.property_aliases.keys()

    # Gets the canonical title of the property alias
    @staticmethod
    def deduce_prop(alias):
        for key, value in Movie.property_aliases.iteritems():
            if key == alias:
                return key
            else:
                try:
                    value.index(alias)
                    return key
                except:None
        print("!! property alias not found : "+alias)
        return None


    def __init__(self, props):
        # An internal dictionary provides dynamic property behavior
        self.__props = dict()
        for key, value in props.iteritems():
            self.set_prop(key, value)


    def set_prop(self, key, value):
        # The canonical key is used to set the value
        # To prevent rogue entries and searching.
        alias = Movie.deduce_prop(key)
        self.__props[alias] = value
    
    def __getattr__(self, prop):
        # For unknown properties, if there is an alias,
        # retrieve the value with the canonical key
        alias = Movie.deduce_prop(prop)
        if alias == None:
            return None
        else:
            return self.__props[alias]


    def __str__(self):
        # Get the string description of the dynamic property container.
        return str(self.__props)
