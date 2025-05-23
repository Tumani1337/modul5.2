from tasks1 import is_palindrom
import pytest


@pytest.mark.parametrize("data, expected_result",
                         [
                             (0, True),
                             (221, False),
                             (112211, True)
                         ])

def test_palindrome_positive(data, expected_result):

    assert is_palindrom(data) == expected_result


@pytest.mark.parametrize("data, expected_result",
                         [
                             (None, TypeError),
                             ("123321", TypeError),
                             (1.111, TypeError)
                         ])

def test_palindrome_negative(data, expected_result):

    with pytest.raises(expected_result):
        is_palindrom(data)


@pytest.mark.parametrize("data, expected_result",
                         [
                             (0, True),
                             (-1, False)
                         ])

def test_palindrome_borderline(data, expected_result):

    assert is_palindrom(data) == expected_result