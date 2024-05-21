from main import remove_whitespace


def test_string1():
    actual_result1 = remove_whitespace("this is a string")
    expected_result1 = "thisisastring"
    assert actual_result1 == expected_result1


def test_string2():
    actual_result2 = remove_whitespace("yes, string")
    expected_result2 = "yes,string"
    assert actual_result2 == expected_result2


def test_string3():
    actual_result3 = remove_whitespace("a string")
    expected_result3 = "astring"
    assert actual_result3 == expected_result3
