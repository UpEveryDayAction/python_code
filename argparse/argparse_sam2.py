import argparse    # 1. argparseをインポート

parser = argparse.ArgumentParser(description='ちょっとしたサンプルプログラム')    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('user', help='本を読むひと')    # 必須の引数を追加
parser.add_argument('--compliment', help='誉め言葉')    # オプション引数（指定しなくても良い引数）を追加
parser.add_argument('count', help='本を読む回数')   # よく使う引数なら省略形があると使う時に便利
# オプションなしの引数は定義した順に受け取っていく
args = parser.parse_args()    # 4. 引数を解析

for i in range(int(args.count)):
    print(args.user,'は本を',str(i+1),'回読みました。',args.compliment)