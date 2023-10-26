import Simulaciones as c
import unittest
import math
class TestSimulaciones(unittest.TestCase):

    def test_Cal_Prob_Posi(self):
        Cal_Prob_Posi = c.Cal_Prob_Posi([-3-1j, -2j, 1j, 2], 2)
        self.assertAlmostEqual(Cal_Prob_Posi, 5.263157894736841)
        Cal_Prob_Posi = c.Cal_Prob_Posi([2+1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], 7)
        self.assertAlmostEqual(Cal_Prob_Posi, 10.869565217391303) 
    
    def test_Cal_Prob_Posi_Doble(self):
        Cal_Prob_Posi_Doble = c.Cal_Prob_Posi_Doble([2+1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], [-3-1j, -2j, 1j, 2, -3-1j, -3-1j, -3-1j, -3-1j, -3-1j, -3-1j])
        self.assertAlmostEqual(Cal_Prob_Posi_Doble, (557.0))
        Cal_Prob_Posi_Doble = c.Cal_Prob_Posi_Doble([1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], [-1-4j, 2-3j, -7+6j, -1+1j, -5-3j, 5, 5+8j, 4-4j, -8-7j, -2-7j])
        self.assertAlmostEqual(Cal_Prob_Posi_Doble, (914.0000000000001))

    def test_Cal_Prob_Posi_Doble_Normalizada(self):
        Cal_Prob_Posi_Doble_Normalizada = c.Cal_Prob_Posi_Doble_Normalizada([2+1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], [-3-1j, -2j, 1j, 2, -3-1j, -3-1j, -3-1j, -3-1j, -3-1j, -3-1j])
        self.assertAlmostEqual(Cal_Prob_Posi_Doble_Normalizada, (0.15327462850853055))
        Cal_Prob_Posi_Doble_Normalizada = c.Cal_Prob_Posi_Doble_Normalizada([1j, -1+2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], [-1-4j, 2-3j, -7+6j, -1+1j, -5-3j, 5, 5+8j, 4-4j, -8-7j, -2-7j])
        self.assertAlmostEqual(Cal_Prob_Posi_Doble_Normalizada, (0.04700195412938395))

    def test_amplitud_de_transicion(self):
        amplitud_de_transicion = c.amplitud_de_transicion([1j, 1], [1, -1j])
        self.assertAlmostEqual(amplitud_de_transicion, (-2j))
        amplitud_de_transicion = c.amplitud_de_transicion([2j, 5], [2, -1j])
        self.assertAlmostEqual(amplitud_de_transicion, (-9j))

    def test_amplitud_de_transicion_normalizada(self):
        amplitud_de_transicion_normalizada = c.amplitud_de_transicion_normalizada([1j, 1], [1, -1j])
        self.assertAlmostEqual(amplitud_de_transicion_normalizada, (-0.9999999999999998j))
        amplitud_de_transicion_normalizada = c.amplitud_de_transicion_normalizada([2j, 5], [2, -1j])
        self.assertAlmostEqual(amplitud_de_transicion_normalizada, (-0.7474093186836597j))

    def test_varianza_y_media_del_observable(self):
        varianza_y_media_del_observable = c.varianza_y_media_del_observable(([[0, -1j], [1j, 0]]), [1/math.sqrt(2), 1j/math.sqrt(2)])
        self.assertAlmostEqual(varianza_y_media_del_observable, ((1, 0j)))
        varianza_y_media_del_observable = c.varianza_y_media_del_observable(([[0, 1j], [-1j, 0]]), [1/math.sqrt(2), 1j/math.sqrt(2)])
        self.assertAlmostEqual(varianza_y_media_del_observable, ((-1, 0j)))
    
    def test_valores_vectores(self):
        valores_vectores = c.valores_vectores([[1, -1j], [1j, 1]])
        self.assertAlmostEqual(valores_vectores, (([(1.9999999999999991+0j), 0j], [[(-0-0.7071067811865474j), (0.7071067811865476+0j)], [(0.7071067811865476+0j), -0.7071067811865474j]])))
        valores_vectores = c.valores_vectores([[-1, -1j], [1j, 1]])
        self.assertAlmostEqual(valores_vectores, (([(-1.414213562373095+0j), (1.4142135623730951+0j)], [[(0.9238795325112867+0j), (-0-0.3826834323650897j)], [(-0-0.3826834323650898j), (0.9238795325112867+0j)]])))

    def test_probabilidades_vectores(self):
        probabilidades_vectores = c.probabilidades_vectores([1/math.sqrt(2), 1j/math.sqrt(2)], [[0, -1j], [1j, 0]], 1)
        self.assertAlmostEqual(probabilidades_vectores, ((1.1102230246251565e-16+0j)))
        probabilidades_vectores = c.probabilidades_vectores([1/math.sqrt(2), 1j/math.sqrt(2)], [[0, 1j], [1j, 0]], 1)
        self.assertAlmostEqual(probabilidades_vectores, ((0.4999999999999998+0.4999999999999999j)))

if __name__ == "__main__":
    unittest.main()
