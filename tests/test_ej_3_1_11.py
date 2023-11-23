from src.ej_3_1_11 import producto_escalar
import pytest
@pytest.mark.parametrize(
    "input_n1,, input_n2, expected",
    [
    ((-1, 0, 2), (1, 1, 20), [-1, 0, 40]),
    ((-1, 3, 9), (8, 6, 27), [-8, 18, 243]),
    ((-2, 5, 5), (2, 8, 2), [-4, 40, 10]),
    ((-10, 0, 7), (-2, 4, 5), [20, 0, 35])
    ]
)
def test(input_n1, input_n2, expected):
    assert producto_escalar(input_n1, input_n2) == expected