def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 3, 3, "Equilateral"),
    (3, 4, 4, "Isosceles"),
    (5, 4, 6, "Scalene"),
    (1, 2, 3, "Not a triangle"),
    (2, 2, 4, "Not a triangle")
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
