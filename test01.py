import pytest
@pytest.mark.parametrize("x", [0, 1, 2])
@pytest.mark.parametrize("y", [3, 1, 2])
@pytest.mark.parametrize("z", [4, 5, 6])
def test_01(x,y,z):
    print("x->%s,y->%s,z->%s" % (x, y,z))