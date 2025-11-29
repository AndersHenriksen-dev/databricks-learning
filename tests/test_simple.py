from databricks_learning import square_sum


def test_square_sum_empty():
    assert square_sum([]) == 0


def test_square_sum_values():
    assert square_sum([1, 2, 3]) == 1+4+9
