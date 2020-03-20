#coding:utf-8
import  pytest
@pytest.mark.parametrize("test_input,excepted",[
                             ("1+5",6),
                             ("1+7",6),
                             ("2+8",10),
                             ])
def test_eval(test_input,excepted):
    assert eval(test_input) == excepted







