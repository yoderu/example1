# bmi計算ツールコマンドライン版
import argparse
from bmi.Util import Util
# BMIを計算する関数
def BMI_caLC(weight:int,height:int):
    result = weight / height**2
    return result
def standardBMI(height:int):
    return height**2 * 22, height**2 * 20
    

# メインルーチン呼び出し
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('weight', type=int, help="体重") # コマンドライン引数(整数)を追加（1）
    parser.add_argument('height', type=int, help='身長') # コマンドライン引数(整数)を追加（2）
    # コマンドライン引数の解析
    args = parser.parse_args()
    
    #result = BMI_caLC(args.weight, args.height/100) # 引数1つめ args.param1  引数2つめ　args.param2
    ytil = Util(args.height, args.weight)
    print(f"BMI は {ytil.calc_bmi()}") 
    #   BMI 18.5～25未満が普通体、BMI 18.5未満は痩せすぎ、BMI 25以上は肥満
    if ytil.calc_bmi() >= 25:
       print("肥満です")
    
    elif ytil.calc_bmi() < 18.5:
        print("痩せすぎ") 
        
    elif ytil.calc_bmi() <= 22:
        print("美容体重")
        
    else:
        print("標準体重")
    #result = standardBMI(args.height/100)
    print(f"BMI標準体重 は {ytil.standardBMI()[0]:.1f}kg")
    print(f"BMI美容体重 は {ytil.standardBMI()[1]:.1f}kg")