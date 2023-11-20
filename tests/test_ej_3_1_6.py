from src.ej_3_1_6 import asignaturas_a_repetir
import pytest
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (["Mates", "Lengua"], [2, 8], ["Mates"]),
    (["Geografia", "Algo", "Algo2"], [2, 8, 1], ["Geografia", "Algo2"]),
    (["Historia"], [2], ["Historia"]),
    (["Hola"], [10], [])
    ]
)
def test(input_n1, input_n2, expected):
    assert asignaturas_a_repetir(input_n1, input_n2) == expected