from cell import sign
import cell


def test_example1():
    n1 = -2
    assert(sign(n1) == -1)
    n2 = 0
    assert (sign(n2) == 0)
    n3 = 1
    assert (sign(n3) == 1)


test_example1()


def test_example2():

    assert (cell.Speed == 1)


test_example2()


