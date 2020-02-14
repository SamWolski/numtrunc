import numpy as np

class TruncNum:
    '''
    A number that maintains its truncation, ie. the number of decimal figures, or the size of the exponent.
    '''
    def __init__(self, value=None, model_value=None):
        self.set_template_from_model(model_value)
        self.value = value

    ## Printing dunders
    ###################

    def __repr__(self):
        return '<{} with value {} and template {}>'.format(type(self).__name__, self.value, self.template)

    def __str__(self):
        return str(self.value)
    
    ## Arithmetic dunders
    #####################

    ## TODO

    ## Attribute getters and setters
    ################################

    ## TODO

    ## Logic methods
    ################

    def set_template_from_model(self, model_value):
        self.template = None