import numpy as np

## Technical definitions used:
## - exponent : refers to the number after the 'e' in scientific notation
## - characteristic : the whole-number part of a decimal, ie 7 in 7.85
## - mantissa : the non-whole-number part of a decimal, ie 0.85 in 7.85 (in NumTrunc, only the actual significant figures are considered, ie 85)
## - decimal : <characteristic>.<mantissa>
## - value : the actual numerical value of the stored number, ie <decimal>e<exponent>

class TruncNum:
    '''
    A number that maintains its truncation, ie. the number of decimal figures, or the size of the exponent.
    '''
    def __init__(self, value, template=None):
        self.template = template
        self.value = value

    ## Printing dunders
    ###################

    def __repr__(self):
        return '<{} with value {} and template {}>'.format(type(self).__name__, self.value, self.template)

    def __str__(self):
        ## Account for self._significant_figures not being set
        sf_str = lambda s: '' if s is None else str(s)
        format_string = '{:.'+sf_str(self._significant_figures)+'f}'
        return format_string.format(self._decimal)+"e"+str(self.exponent)
    
    ## Arithmetic dunders
    #####################

    ## TODO

    ## Attribute getters and setters
    ################################

    @property
    def exponent(self):
        return self._exponent
    ## TODO - setter


    @property
    def template(self):
        return self._template
    @template.setter
    def template(self, model_string):
        self._template = True
        ## Split the model_string into decimal and exponent
        decimal, exponent = model_string.split("e")
        self._exponent = int(exponent)
        ## Check if formatting should use underscores
        if "_" in decimal:
            self._underscore = True
        else:
            self._underscore = False
        ## Convert the mantissa into a string
        mantissa = decimal.split(".")[1]
        ## Remove underscores from the string and store the number of sf in mantissa
        self._significant_figures = len(''.join(mantissa.split("_")))


    @property
    def value(self):
        return self._decimal * 10**(self._exponent)
    @value.setter
    def value(self, value):
        ## Adjust value such that it is in the range of the exponent
        decimal = value * 10**(-self._exponent)
        ## Truncate to number of significant figures after decimal point
        self._decimal = np.round(float(decimal), self._significant_figures)

