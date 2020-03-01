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
input_value_float_negative_exponent = 7.86e-3
models_results_float_negative_exponent = [
        ("1.00e-3", "7.86e-3"),
        ("1.00e-4", "78.60e-4"),
        ("1.00e-2", "0.79e-2"),
        ("1.00e-6", "7860.00e-6"),
        ("1.00e0", "0.01e0"),
        ("1.000e-3", "7.860e-3"),
        # ("1.e-3", "8.e-3"), # to decide - should this account for the decimal point?
    ]
collection_float_negative_exponent = InputModelResultCollection(input_value_float_negative_exponent, models_results_float_negative_exponent)

## Parametrized testing
@pytest.mark.parametrize("input_value,model_string,desired_result", collection_float_negative_exponent.input_models_results_list)
def test_compare_string_trunc_model_result(input_value, model_string, desired_result):
    assert str(TruncNum(input_value, model_string)) == desired_result
