import Simulaciones as c
import unittest
class TestSimulaciones(unittest.TestCase):

    def test_Cal_Prob_Posi(self):
        Cal_Prob_Posi = c.Cal_Prob_Posi([2-1j, 2j, 1-1j, 1-2j, 2], (1-1j))
        self.assertAlmostEqual(Cal_Prob_Posi, 0.050000000000000044)
        Cal_Prob_Posi = c.Cal_Prob_Posi([2-1j, 2j, 1-1j, 1-2j, 3], (1-1j))
        self.assertAlmostEqual(Cal_Prob_Posi, 0.040000000000000036) 


if __name__ == "__main__":
    unittest.main()