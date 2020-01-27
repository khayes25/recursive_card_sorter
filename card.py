"""
@author: Keon Hayes
"""

"""
Card Object.
"""

#Class Header
class Card :
    """
    Initializer that creates two fields
    """
    def __init__(self, value_in, suit_in, value_index_in, suit_index_in) :
        self.value = value_in
        self.suit = suit_in
        self.value_index = value_index_in
        self.suit_index = suit_index_in

    #ACCESSORS
    """
    Accessor function for the value field
    """
    def get_value(self) :
        return self.value

    """
    Accessor function for the suit field
    """
    def get_suit(self) :
        return self.suit

    """
    Accessor function for the value_index field
    """
    def get_value_index(self) :
        return self.value_index

    """
    Accessor function for the suit_index field
    """
    def get_suit_index(self) :
        return self.get_suit_index