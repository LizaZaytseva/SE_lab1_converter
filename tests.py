import converter


def run_case(test_input):
    input_value = test_input
    output = []

    def mock_input(s):
        output.append(s)
        return input_value.pop(0)

    converter.input = mock_input
    converter.print = lambda s: output.append(s)
    converter.main()
    return output


def test_simple():
    output = run_case(['12 gr', 'oz', '3'])

    assert output[0] == "Weight converter: grams <-> carats <-> ounce"
    assert output[1] == "Enter the value and specify the unit of measurement (gr,ct,oz) e.g. 123 gr: "
    assert output[2] == "Enter the required unit of measurement (gr,ct,oz): "
    assert output[3] == "Rounding accuracy: "
    assert output[4] == "Result:	0.423 oz"


def test_not_enough_arguments1():
    output = run_case(['', 'oz', '3'])

    assert output[0] == "Weight converter: grams <-> carats <-> ounce"
    assert output[1] == "Enter the value and specify the unit of measurement (gr,ct,oz) e.g. 123 gr: "
    assert output[2] == "Enter the required unit of measurement (gr,ct,oz): "
    assert output[3] == "Rounding accuracy: "
    assert output[4] == "Invalid format!"


def test_not_enough_arguments2():
    output = run_case(['122 ct', '', '3'])

    assert output[0] == "Weight converter: grams <-> carats <-> ounce"
    assert output[1] == "Enter the value and specify the unit of measurement (gr,ct,oz) e.g. 123 gr: "
    assert output[2] == "Enter the required unit of measurement (gr,ct,oz): "
    assert output[3] == "Rounding accuracy: "
    assert output[4] == "Invalid format!"


def test_not_enough_arguments3():
    output = run_case(['122 ct', 'oz', ''])

    assert output[0] == "Weight converter: grams <-> carats <-> ounce"
    assert output[1] == "Enter the value and specify the unit of measurement (gr,ct,oz) e.g. 123 gr: "
    assert output[2] == "Enter the required unit of measurement (gr,ct,oz): "
    assert output[3] == "Rounding accuracy: "
    assert output[4] == "Invalid format!"


def test_invalid_argument2():
    output = run_case(['122 ct', 'g', '2'])

    assert output[0] == "Weight converter: grams <-> carats <-> ounce"
    assert output[1] == "Enter the value and specify the unit of measurement (gr,ct,oz) e.g. 123 gr: "
    assert output[2] == "Enter the required unit of measurement (gr,ct,oz): "
    assert output[3] == "Rounding accuracy: "
    assert output[4] == "Invalid format!"


