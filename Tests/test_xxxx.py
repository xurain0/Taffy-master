from nose.tools import nottest,istest
from nose.tools import assert_equal

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
    @nottest
    def test_three(self):
        assert True
    @istest
    def xxxxx(self):
        assert True

class test_haha():
    def setUp(self):
        print("============test class setup==============")
    def teardown(self):
        print("============test class teardown==============")
    def test_xxx(self):
        print "test_xxx"
        assert_equal(9, 9)
    def test_kkk(self):
        print "test_kkk"
        assert_equal(1, 1)