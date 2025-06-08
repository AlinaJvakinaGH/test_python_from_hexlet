from lesson_9.implementations.wrong3 import fill

coll =  [1, 2, 3, 4]
cil = [1, 2, 3, 4]

def func_fill():
    fill(coll, '*', 1, 3)
    assert coll == [1, '*', '*', 4]

def test_fill():
    fill(cil, '*', 1, 9)
    assert cil == [1, '*', '*', '*']