#コマンドライン実行サンプル
import argparse
# ２つの引数を計算する関数
def func_add(x:int, y:int): # 整数の引数 x, y
    result = x + y # 足し算の計算を変数　resultにいれる
    return result  # resultの値を呼び出し元に返す

# メインルーチン呼び出し
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('param1', type=int, help='整数１') # コマンドライン引数(整数)を追加（1）
    parser.add_argument('param2', type=int, help='整数２') # コマンドライン引数(整数)を追加（2）
    parser.add_argument('label', type=str, help='文字列') # コマンドライン引数(文字列)を追加（3）
    
    # コマンドライン引数の解析
    args = parser.parse_args() 
    
    # 関数 func_add()にコマンドラインから受け取った２つの引数を渡し、変数 resultに結果を入れる
    result = func_add(args.param1, args.param2) # 引数1つめ args.param1  引数2つめ　args.param2
    print(f"引数param1 足す 引数param2 は {result}") # 結果resultをプリント
    print(f"ラベルは {args.label}")