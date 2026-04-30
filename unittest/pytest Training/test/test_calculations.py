import pytest
from src.calculations import Calculations

class TestCalculations:
    calc = Calculations()

    # @pytest.fixture(scope='module', autouse=True)
    # def setup(self):
    #     print("Fixture")


    @pytest.mark.parametrize("n1, n2, exval",
                              [(5, 5, 10),(-5, -5, -10),(0, 5, 5)])
    def test_add(self, n1, n2, exval):
        res = self.calc.add(n1, n2)
        assert res == exval, 'Adittion Error'

    @pytest.mark.parametrize("n1, n2, exval",
                             [(5, 5, 0),(-5, -5, 0),(0, 5, -5)])
    def test_sub(self, n1, n2, exval):
        res = self.calc.sub(n1, n2)
        assert res == exval, 'Subtraction Error'

    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, 'Multiplication Error'

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2.0, 'Division Error'

    @pytest.mark.skip(reason="NIY")
    def test_ne(self):
        res = self.calc.ne(10,5)
        assert res == True, 'NE'

    @pytest.mark.xfail(reason="exception not handled")
    def test_diverr(self):
        # with pytest.raises(ZeroDivisionError):
        res = self.calc.div(10, 0)
        assert res == 0


