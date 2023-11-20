from src.ej_3_1_3 import listar_asignaturas
import pytest
@pytest.mark.parametrize(
    "input_n1 , input_n2, expected",
    [
    (["Mates", "Lengua"], [2, 10], "En Mates has sacado 2\nEn Lengua has sacado 10\n"),
    (["Geografia"], [7],"En Geografia has sacado 7\n"),
    (["Historia"], [8], "En Historia has sacado 8\n"),
    (["Hola"], [6], "En Hola has sacado 6\n")
    ]
)
def test(input_n1, input_n2, expected):
    assert listar_asignaturas(input_n1, input_n2) == expected