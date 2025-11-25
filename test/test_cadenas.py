import pytest

from src.ex01_repeat_name import repeat_name
from src.ex02_name_variants import name_variants
from src.ex03_name_length import name_upper_and_length
from src.ex04_phone_core import phone_core
from src.ex05_reverse_phrase import reverse_phrase
from src.ex06_emphasize_vowel import emphasize_vowel
from src.ex07_replace_domain import replace_domain
from src.ex08_euros_cents import euros_cents
from src.ex09_parse_date import parse_date
from src.ex10_split_products import split_products
from src.ex11_format_product import format_product


# ---------------------------------------------------------
# EX01
# ---------------------------------------------------------

def test_ex01_repeat_name_positive():
    assert repeat_name("Ana", 3) == "Ana\nAna\nAna"


def test_ex01_repeat_name_non_positive():
    assert repeat_name("Ana", 0) == ""
    assert repeat_name("Ana", -2) == ""


# ---------------------------------------------------------
# EX02
# ---------------------------------------------------------

def test_ex02_name_variants():
    lower, upper, cap = name_variants("pEpE pErEz")
    assert lower == "pepe perez"
    assert upper == "PEPE PEREZ"
    assert cap == "Pepe Perez"


# ---------------------------------------------------------
# EX03
# ---------------------------------------------------------

def test_ex03_name_length_spaces_ignored():
    up, n = name_upper_and_length("Ana Maria")
    assert up == "ANA MARIA"
    assert n == 8


def test_ex03_name_length_no_spaces():
    up, n = name_upper_and_length("pepe")
    assert up == "PEPE"
    assert n == 4


# ---------------------------------------------------------
# EX04
# ---------------------------------------------------------

def test_ex04_phone_core_ok():
    assert phone_core("+34-913724710-56") == "913724710"


def test_ex04_phone_core_spaces():
    assert phone_core("  +34-600123123-01   ") == "600123123"


def test_ex04_phone_core_bad_format():
    with pytest.raises(ValueError):
        phone_core("34-600123123-01")
    with pytest.raises(ValueError):
        phone_core("+34-600123123")
    with pytest.raises(ValueError):
        phone_core("+34-ABC-11")


# ---------------------------------------------------------
# EX05
# ---------------------------------------------------------

def test_ex05_reverse_phrase_basic():
    assert reverse_phrase("hola") == "aloh"


def test_ex05_reverse_phrase_spaces():
    assert reverse_phrase("hola mundo") == "odnum aloh"


# ---------------------------------------------------------
# EX06
# ---------------------------------------------------------

def test_ex06_emphasize_vowel_a():
    assert emphasize_vowel("anita lava la tina", "a") == "AnitA lAvA lA tinA"


def test_ex06_emphasize_vowel_case_insensitive():
    assert emphasize_vowel("Elefante", "E") == "ElEfAntE"


def test_ex06_emphasize_vowel_invalid():
    with pytest.raises(ValueError):
        emphasize_vowel("hola", "x")
    with pytest.raises(ValueError):
        emphasize_vowel("hola", "ae")


# ---------------------------------------------------------
# EX07
# ---------------------------------------------------------

def test_ex07_replace_domain_basic():
    assert replace_domain("user@example.com") == "user@ceu.es"


def test_ex07_replace_domain_custom():
    assert replace_domain(
        "alumno@miuni.es",
        new_domain="donapea.navarra.es"
    ) == "alumno@donapea.navarra.es"


def test_ex07_replace_domain_invalid():
    with pytest.raises(ValueError):
        replace_domain("sinarroba")
    with pytest.raises(ValueError):
        replace_domain("a@b@c")


# ---------------------------------------------------------
# EX08
# ---------------------------------------------------------

def test_ex08_euros_cents_dot():
    assert euros_cents("123.45") == (123, 45)


def test_ex08_euros_cents_comma():
    assert euros_cents("7,00") == (7, 0)


def test_ex08_euros_cents_bad_format():
    with pytest.raises(ValueError):
        euros_cents("12")
    with pytest.raises(ValueError):
        euros_cents("12.3")
    with pytest.raises(ValueError):
        euros_cents("abc")


# ---------------------------------------------------------
# EX09
# ---------------------------------------------------------

def test_ex09_parse_date_two_digits():
    assert parse_date("09/12/2001") == (9, 12, 2001)


def test_ex09_parse_date_one_digit_day_month():
    assert parse_date("9/1/2001") == (9, 1, 2001)


def test_ex09_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("9-1-2001")
    with pytest.raises(ValueError):
        parse_date("9/13/2001")


# ---------------------------------------------------------
# EX10
# ---------------------------------------------------------

def test_ex10_split_products_basic():
    assert split_products("pan, leche, huevos") == ["pan", "leche", "huevos"]


def test_ex10_split_products_spaces_and_empty():
    assert split_products("  pan ,  ,  leche , huevos  ") == ["pan", "leche", "huevos"]


def test_ex10_split_products_empty():
    assert split_products("   ") == []


# ---------------------------------------------------------
# EX11
# ---------------------------------------------------------

def test_ex11_format_product_widths():
    out = format_product("tornillo", 2.5, 7)
    assert out == "tornillo      2.50 007       17.50"
