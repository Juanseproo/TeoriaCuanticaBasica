import Simulaciones as c
import unittest
class TestSimulaciones(unittest.TestCase):

    def test_Cal_Prob_Posi(self):
        Cal_Prob_Posi = c.Cal_Prob_Posi([-3-1j, -2j, 1j, 2], 2)
        self.assertAlmostEqual(Cal_Prob_Posi, 5.263157894736841)
        Cal_Prob_Posi = c.Cal_Prob_Posi([2+1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], 7)
        self.assertAlmostEqual(Cal_Prob_Posi, 10.869565217391303) 


if __name__ == "__main__":
    unittest.main()
