import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitilize(string_utils):
    # Позитивные тесты
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("SkyPro") == "Skypro"
    # Негативные тесты
    assert string_utils.capitilize("") == ""

def test_trim(string_utils):
    # Позитивные тесты
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    # Негативные тесты
    assert string_utils.trim("") == ""

def test_to_list(string_utils):
    # Позитивные тесты
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    # Негативные тесты
    assert string_utils.to_list("", ",") == []

def test_contains(string_utils):
    # Позитивные тесты
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False
    # Негативные тесты
    assert string_utils.contains("", "S") is False

def test_delete_symbol(string_utils):
    # Позитивные тесты
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    # Негативные тесты
    assert string_utils.delete_symbol("", "a") == ""

def test_starts_with(string_utils):
    # Позитивные тесты
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "P") is False
    # Негативные тесты
    assert string_utils.starts_with("", "S") is False

def test_end_with(string_utils):
    # Позитивные тесты
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "y") is False
    # Негативные тесты
    assert string_utils.end_with("", "o") is False

def test_is_empty(string_utils):
    # Позитивные тесты
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty("   ") is True
    assert string_utils.is_empty("SkyPro") is False

def test_list_to_string(string_utils):
    # Позитивные тесты
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    # Негативные тесты
    assert string_utils.list_to_string([], ", ") == ""
