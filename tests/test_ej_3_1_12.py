from src.ej_3_1_12 import producto_escalar
import pytest
@pytest.mark.parametrize(
    "input_n1,, input_n2, expected",
    [
    (((-1, 0), (0, 1) ,(1, 1)), ((1, 2), (3, 4), (5, 6)), ((-1, 0), (0, 4), (5, 6)))
    ]
)
def test(input_n1, input_n2, expected):
    assert producto_escalar(input_n1, input_n2) == expected