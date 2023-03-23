from poly import polygon


def test_anticlockwise():
    test1 = [[0, 0], [2, 0], [2, 2], [0, 2]]
    p = polygon(test1)
    assert p.isAntiClockwise  # this test is anti clockwise

    test2 = [[0, 0], [0, 2], [2, 2], [2, 0]]
    p = polygon(test2)
    assert not p.isAntiClockwise  # this test is clockwise
