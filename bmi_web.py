from flask import Flask, render_template, request, jsonify
from bmi.Util import Util
from bmi.AISpeech import AISpeech
import os
app = Flask(__name__)
# API Keyとリージョン
speech_key, service_region = "KEY",  "japaneast"
Speech = AISpeech(speech_key, service_region, "ja-JP-DaichiNeural")
# ホーム
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/transcribe", methods=["POST"])
def transcribe():
    result =  Speech.transcribe()
    if result.reason is None:
       return jsonify({"text": "音声認識に失敗しました"})
    else:
       return jsonify({"text": result.text.replace("。", "")})
    
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
    except ZeroDivisionError:
        error = True 
        msg = "0は入力できません"
    except Exception as e:
        error = True
        msg = "半角数字(整数値)で入力してください"
    finally:    
        return render_template("index.html", error=error, msg=msg)
    return render_template("view_bmi.html", height_centimeters=height_centimeters, weight=weight, error=error, msg=msg)

if __name__ == "__main__":
    # 現在いるディレクトリを取得する
    current_folder = os.getcwd()
    static_folder_path = current_folder + "/static"
    # flaskに staticフォルダーのパスを設定する
    app.config["STATIC_FOLDER"] = static_folder_path    
    app.run(debug=True)