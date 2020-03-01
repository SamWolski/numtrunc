import pytest
from src.TruncNum import TruncNum


class InputModelResultCollection:
    '''
    Collect sets of input values, model strings, and expected outputs, with easy generation of parameter sets compatible with pytest.mark.parametrize
    '''
    def __init__(self, input_value, models_results_list):
        self.input_value = input_value
        self.models_results_list = models_results_list
    
    @property
    def input_models_results_list(self):
        return [(self.input_value, mm, ee) for mm, ee in self.models_results_list]

## Test cases - input value, different models, expected result
##############################################################

collections_float = []

## Decimals only - no 'e'
input_value_float_decimal = 3.849
models_results_float_decimal = [
        ("1.000", "3.849"),       # Identity
        ("1.00000", "3.84900"),   # More sf
        ("1.00", "3.85"),         # Fewer sf (2)
        ("1.0", "3.8"),           # Fewer sf (1)
        ("1.", "4"),              # Characteristic only - w/ decimal point
        ("1", "4"),               # Characteristic only - w/o decimal point
    ]
collections_float.append(InputModelResultCollection(input_value_float_decimal, models_results_float_decimal))

## Negative value with decimals only - no 'e'
input_value_float_negative_decimal = -3.849
models_results_float_negative_decimal = [
        ("1.000", "-3.849"),       # Identity
        ("1.00000", "-3.84900"),   # More sf
        ("1.00", "-3.85"),         # Fewer sf (2)
        ("1.0", "-3.8"),           # Fewer sf (1)
        ("1.", "-4"),              # Characteristic only - w/ decimal point
        ("1", "-4"),               # Characteristic only - w/o decimal point
    ]
collections_float.append(InputModelResultCollection(input_value_float_negative_decimal, models_results_float_negative_decimal))

## Negative exponent
input_value_float_negative_exponent = 7.86e-3
models_results_float_negative_exponent = [
        ("1.00e-3", "7.86e-3"),   # Identity
        ("1.00e-4", "78.60e-4"),  # Smaller exponent
        ("1.00e-2", "0.79e-2"),   # Larger exponent
        ("1.00e-6", "7860.00e-6"),# Much smaller exponent
        ("1.00e0", "0.01e0"),     # Zero exponent
        ("1.000e-3", "7.860e-3"), # Additional sf
        ("1.0e-3", "7.9e-3"),     # Fewer sf
        ("1.e-3", "8e-3"),        # Characteristic only - w/ decimal point
        ("1e-3", "8e-3"),         # Characteristic only - w/o decimal point
        ("1.00e-03", "7.86e-3"),  # Padded exponent
    ]
collections_float.append(InputModelResultCollection(input_value_float_negative_exponent, models_results_float_negative_exponent))

## Positive exponent
input_value_float_positive_exponent = 1.923e4
models_results_float_positive_exponent = [
        ("1.000e4", "1.923e4"),    # Identity
        ("1.000e2", "192.300e2"),  # Smaller exponent
        ("1.000e5", "0.192e5"),    # Larger exponent
        ("1.000e7", "0.002e7"),    # Much larger exponent
        ("1.000e0", "19230.000e0"),# Zero exponent
        ("1.0000e4", "1.9230e4"),  # Additional sf
        ("1.0e4", "1.9e4"),        # Fewer sf
        ("1.e4", "2e4"),           # Characteristic only - w/ decimal point
        ("1e4", "2e4"),            # Characteristic only - w/o decimal point
        ("1.000e04", "1.923e4"),   # Padded exponent
    ]
collections_float.append(InputModelResultCollection(input_value_float_positive_exponent, models_results_float_positive_exponent))

## Positive exponent
input_value_float_negative_positive_exponent = -1.923e4
models_results_float_negative_positive_exponent = [
        ("1.000e4", "-1.923e4"),    # Identity
        ("1.000e2", "-192.300e2"),  # Smaller exponent
        ("1.000e5", "-0.192e5"),    # Larger exponent
        ("1.000e7", "-0.002e7"),    # Much larger exponent
        ("1.000e0", "-19230.000e0"),# Zero exponent
        ("1.0000e4", "-1.9230e4"),  # Additional sf
        ("1.0e4", "-1.9e4"),        # Fewer sf
        ("1.e4", "-2e4"),           # Characteristic only - w/ decimal point
        ("1e4", "-2e4"),            # Characteristic only - w/o decimal point
        ("1.000e04", "-1.923e4"),   # Padded exponent
    ]
collections_float.append(InputModelResultCollection(input_value_float_negative_positive_exponent, models_results_float_negative_positive_exponent))


## Concatenate all lists
input_float_with_model_params = [params for cc in collections_float for params in cc.input_models_results_list]


## Parametrized testing
@pytest.mark.parametrize("input_value,model_string,desired_result", input_float_with_model_params)
def test_compare_string_trunc_model_result(input_value, model_string, desired_result):
    assert str(TruncNum(input_value, model_string)) == desired_result
