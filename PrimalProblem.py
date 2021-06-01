import numpy as np

class PrimalProblem:
    """
    self.Model - system of Polygons.
    self.Model is a 2d array of pairs (x, y)
    """
    def __init__(self, model, view_points):
        self.Model = model
        self.View_Points = view_points
        
    def Field_Calculate(self, view_point):
        result = 0
        for i in len(self.Model):
            Sigm_v1 = self.Model[i+1]
            Sigm_v = self.Model[i]
            A_v = (Sigm_v1.conjugate() - Sigm_v.conjugate())/(Sigm_v1 - Sigm_v) 
            B_v = Sigm_v1.conjugate() - A_v * Sigm_v.conjugate()
            ln = np.log((Sigm_v1 - view_point)/(Sigm_v - view_point))
            result += A_v * view_point + B_v -view_point.conjugate() * ln
        
        return result * self.Model

