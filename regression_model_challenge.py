import random as rnd
class linear_regression:
    def __init__(self, X: list, y: list, aut_weight: bool = True, weight: float = 0):
        self.X = X
        self.y = y
        self.aut_w = aut_weight
        if aut_weight:
            self.weight = weight

    
    def one_hot_enconding(self):
        pass

    def standart_scaler(self):
        pass

    def fit(self):
        feature = self.X.copy()

        if self.aut_weight:
            peso = self.weight
        else:
            peso = self.weight

    def preditict(self):
        pass

    def metrics(self):
        pass

meu_modelo = linear_regression([[75, 3]], [[600000]]) # metros quadrados X comodos

print(meu_modelo)

meu_modelo = 40



