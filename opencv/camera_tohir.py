import cv2
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App (QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Sample image to save to DB'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()

    def initUI(self):

        # ウィンドウのtitleを設定
        self.setWindowTitle(self.title)

        # ウィンドウサイズを設定
        self.setGeometry(self.left, self.top, self.width, self.height)

        # ボタンのtitleを設定
        buttton = QPushButton('Save Captcha to DB', self)
        # ボタンの意味を設定
        buttton.setToolTip('This is a button to save the camera Captcha image to DB')
        # ボタンの描画位置を設定
        buttton.move(80, 70)
        # ボタン押下処理を設定
        buttton.clicked.connect(self.on_click)

        self.show()

    def camera_capture(self):
        cap = cv2.VideoCapture(0)
        count = 0

        while count < 10:
            count+=1
            ret, frame = cap.read()
            # デバッグ用：画像表示
            #cv2.imshow('camera capture', frame)
            cv2.waitKey(1)

            if count == 10:
                # データベース作成・コネクション作成
                db = sqlite3.connect("my.db")
                # カーソルをコネクションから作成
                cur = db.cursor()
                # テーブル作成
                try:
                    cur.execute('''create table images (id string, img blob)''')
                except sqlite3.OperationalError:
                    print
                    "table images already exists!"

                # コネクションを保存(コミット)
                db.commit()

                # 画像エンコーディング
                _, enc = cv2.imencode(".png", frame)

                # データを追加
                sql = "insert into images values (?, ?)"
                cur.execute(sql, ("camera", memoryview(enc)))

                # コネクションを保存(コミット)
                db.commit()

                # データの読み出し
                # byteデータの取得
                row = cur.execute('SELECT * FROM images').fetchone()
                pic = row[1]

                # 画像保存
                f = open('load2DBforCameraImage.png', 'wb')
                f.write(pic)
                f.close()
                cur.close()
                # OpneCvでも画像保存
                cv2.imwrite("save.png", frame)

        cap.release()
        exit()


    @pyqtSlot()
    def on_click(self):
        print('button on click!')
        self.camera_capture()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())