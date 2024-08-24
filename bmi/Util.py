class Util:
    # 初期化メソッド
    # 属性として、身長と体重を持つ
    def __init__(self, height: int, weight: int):  # 整数の引数　身長(cm) 体重(kg)
        self.height = height
        self.weight = weight
    def get_centimeter_height(self):
        return self.height
    
    def get_meter_height(self):
        return self.height/100
    
    def get_weight(self):
        return self.weight
    
    def calc_bmi(self):  # 整数の引数　身長(cm) 体重(kg)
        return self.weight / (self.get_meter_height() ** 2)  # BMI = 体重 / 身長(m)^2
    
    def standardBMI(self):
        return (self.height/100) **2 * 22, (self.height/100) **2 * 20