import json

from datetime import datetime

from flask import Flask, render_template, redirect, Markup, escape

application = Flask(__name__)

DATA_FILE = 'norilog.json'

#データの保存をする関数
def save_data(start,finish,memo,created_at):
    """
    :param start:　乗った駅
    :type start: str
    :param finish:降りた駅
    :type finish: str
    :param memo :乗り降りのメモ
    :type memo: str
    :param created_at: 乗り降りの日付
    :type created_at: datetime.datetime
    :return: None
    """

    try:
        #json モジュールでデータベースファイルを開く
        database = json.load(open(DATA_FILE,mode="r",encoding="utf-8"))

    except FileNotFoundError:
        database =[]


    database.insert(0,{
    "start":start,
    "finish":finish,
    "memo":memo,
    "created_at":created_at.strftime("%Y-%m-%d %H:%M")
    })

    json.dump(database,open(DATA_FILE,mode="w",encoding="utf-8"),indent=4,ensure_ascii=False)

#データの引き出し
def load_data():
    """
    記録データを返す
    """
    try:
        #jsonモジュールのデータベースファイルを開く
        database = json.load(open(DATA_FILE,mode="r",encoding="utf-8"))
    except FileNotFoundError:
        database =[]

    return database

@application.route('/save',methods = ['POST'])
#フォームのアクションは/save, アクションが起きると関数が呼ばれる

def save():
    """
    記録用URL
    """
    #記録されたデータの取得
    start = request.form.get('start')
    finish = request.form.get('finish')
    memo = request.form.get('memo')
    created_at = datetime.now()
    #フォームのの参照は,request.formで可能.
    save_data(start,finish,memo,created_at)

    return ridirect('/')

@application.template_filter('nl2br')
def nl2br_filter(s):
    #改行をいれるための関数
    return escape(s).replace('\n',Markup('<br>'))


def index():
    """
    トップページをテンプレートを使用してページを表示する
    """
    #記録データの読み込み
    rides = load_data()
    return render_template('index.html',rides = rides)

def main():
    application.run('127.0.0.1',8000)

if __name__ == '__main__':
    #IPアドレス0.0.0.0の8000番ポートで実行される
    application.run('127.0.0.1',8000,debug=True)

    #Flask.runで実行をする引数にはIPとポートの指定を行う ,debugをTrueにしておくとデバッガーか使用できる
