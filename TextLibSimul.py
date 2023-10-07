import Simulaciones as c
import unittest
import math
import numpy as np
class TestSimulaciones(unittest.TestCase):

    def test_Cal_Prob_Posi(self):
        Cal_Prob_Posi = c.Cal_Prob_Posi([-3-1j, -2j, 1j, 2], 2)
        self.assertAlmostEqual(Cal_Prob_Posi, 5.263157894736841)
        Cal_Prob_Posi = c.Cal_Prob_Posi([2+1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], 7)
        self.assertAlmostEqual(Cal_Prob_Posi, 10.869565217391303) 
    
    def test_Cal_Prob_Posi_Doble(self):
        Cal_Prob_Posi_Doble = c.Cal_Prob_Posi_Doble([2+1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], [-3-1j, -2j, 1j, 2, -3-1j, -3-1j, -3-1j, -3-1j, -3-1j, -3-1j])
        self.assertAlmostEqual(Cal_Prob_Posi_Doble, (-0.23223922534223615+0.31518180582160615j))
        Cal_Prob_Posi_Doble = c.Cal_Prob_Posi_Doble([1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], [-1-4j, 2-3j, -7+6j, -1+1j, -5-3j, 5, 5+8j, 4-4j, -8-7j, -2-7j])
        self.assertAlmostEqual(Cal_Prob_Posi_Doble, (-0.12190844191195455+0.17927712045875666j))

    def test_amplitud_de_transicion(self):
        amplitud_de_transicion = c.amplitud_de_transicion([1j, 1], [1, -1j])
        self.assertAlmostEqual(amplitud_de_transicion, (-0.9999999999999998j))
        amplitud_de_transicion = c.amplitud_de_transicion([2j, 5], [2, -1j])
        self.assertAlmostEqual(amplitud_de_transicion, (-0.7474093186836597j))

    def test_varianza_del_observable(self):
        varianza_del_observable = c.varianza_del_observable(np.array([[1, -1j], [1j, 2]], dtype=complex), np.array([math.sqrt(2)/2, math.sqrt(2)*1j/2], dtype=complex))
        self.assertAlmostEqual(varianza_del_observable, (-3.7500000000000013))
        varianza_del_observable = c.varianza_del_observable(np.array([[2, -1j], [1j, 2]], dtype=complex), np.array([math.sqrt(2)/2, math.sqrt(2)*1j/2], dtype=complex))
        self.assertAlmostEqual(varianza_del_observable, (-5.000000000000003))

if __name__ == "__main__":
    unittest.main()
