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
        format_string = '{:.'+sf_str(self.significant_figures)+'f}'
        decimal_string = format_string.format(self.decimal)
        ## Add exponent string if it is not None
        if self.exponent is None:
            exponent_string = ''
        else:
            exponent_string = "e"+str(self.exponent)
        return decimal_string+exponent_string
    
    ## Arithmetic dunders
    #####################

    ## TODO

    ## Attribute getters and setters
    ################################

    ## No explicit setters


    @property
    def decimal(self):
        return self._decimal


    @property
    def significant_figures(self):
        return self._significant_figures


    ## Explicit setters


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
        ## Split the model_string into decimal and exponent if 'e' is found
        if "e" in model_string:
            decimal_string, exponent_string = model_string.split("e")
            self._exponent = int(exponent_string)
        else:
            decimal_string = model_string
            self._exponent = None
        ## Check if formatting should use underscores
        if "_" in decimal_string:
            self._underscore = True
        else:
            self._underscore = False
        ## Check if decimal point is included in template string
        if "." in decimal_string:
            ## Get mantissa as a string to calculate number of significant figures
            mantissa = decimal_string.split(".")[1]
            ## Remove underscores from the string and store the number of sf in mantissa
            self._significant_figures = len(''.join(mantissa.split("_")))
        else:
            ## No sig figs after the decimal point, as it is not included in the template
            self._significant_figures = 0


    @property
    def value(self):
        if self.exponent is None:
            return self.decimal
        else:
            return self.decimal * 10**(self.exponent)
    @value.setter
    def value(self, value):
        if self.exponent is None:
            decimal = value
        else:
            ## Adjust value such that it is in the range of the exponent
            decimal = value * 10**(-self.exponent)
        ## Truncate to number of significant figures after decimal point
        self._decimal = np.round(float(decimal), self.significant_figures)

