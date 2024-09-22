from flask import Flask, render_template, request
from bmi.Util import Util
from bmi.AISpeech import AISpeech
app = Flask(__name__)
# API Keyとリージョン
speech_key, service_region = KEY,  "japaneast"
Speech = AISpeech(speech_key, service_region, "ja-JP-DaichiNeural")
# ホーム
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/calc", methods=["POST"])
def calc():
     # エラーフラグとエラーメッセージを初期化
    error = False
    height_centimeters = request.form.get("height_centimeters")
    weight = request.form.get("weight")
    voice_name = request.form.get("voice")
    int_volume = int(request.form.get("volume"))
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
        xytil =  ytil.standardBMI()   
        tmp = ytil.calc_bmi()
     #音声で読み上げ
        ssml = Speech.genSSML(
            voice_name = voice_name,
            volume = int_volume,
            text = f"あなたの身長は{height_centimeters}センチメートル、体重は{weight}キログラムですね。あなたのBMI値は{tmp}です。"
        )  
        Speech.speechSSML(ssml)
        return render_template("view_bmi.html", height_centimeters=height_centimeters, weight=weight, error=error,bmi=tmp,text=text,bt=xytil[1],st=xytil[0])
    except Exception as e:
        error = True
        msg = "半角数字(整数値)で入力してください"
        
    return render_template("view_bmi.html", height_centimeters=height_centimeters, weight=weight, error=error, msg=msg)

if __name__ == "__main__":
    
    app.run(debug=True)