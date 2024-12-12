def calculate_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

@pytest.mark.parametrize("length, width, expected", [
    (3, 4, 12),
    (0, 5, 0),
    (7, 0, 0),
    (2.5, 4, 10.0),
    (10, 10, 100)
])
def test_calculate_area(length, width, expected):
    assert calculate_area(length, width) == expected
