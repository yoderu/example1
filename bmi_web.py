from flask import Flask, render_template, request
from bmi.Util import Util
app = Flask(__name__)
# ホーム
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/calc", methods=["POST"])
def calc():
     # エラーフラグとエラーメッセージを初期化
    error = False
    msg = ""
    height_centimeters = request.form.get("height_centimeters")
    weight = request.form.get("weight")
    try:
        int_height_centimeters = int(height_centimeters)
        int_weight = int(weight)
        ytil = Util(int_height_centimeters, int_weight)
        if ytil.calc_bmi() >= 25:
             text ="肥満です"
    
        elif ytil.calc_bmi() < 18.5:
             text ="痩せすぎ"
         
        elif ytil.calc_bmi() <= 22:
             text ="美容体重"
        
        else:
             text ="標準体重"
    except Exception:
        error = True
        msg = "半角数字(整数値)で入力してください"
    return render_template("view_bmi.html", height_centimeters=height_centimeters, weight=weight, error=error, msg=msg,bmi=ytil.calc_bmi(),text=text)

if __name__ == "__main__":
    
    app.run(debug=True)