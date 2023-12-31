from calculator import squared
import  pytest

def test_positive():
    # assert squared(2) == 4
    # assert squared(3) == 9
    for i in range(10):
        assert squared(i) == i * i

def test_negative():
    assert squared(-2) == 4
    assert squared(-3) == 9

def test_zero():
    assert squared(0) == 0

def test_str():
    with pytest.raises(TypeError):
        squared("cat")