# ライブラリのインポート
import cv2
import numpy as np

# -----------以下記述-----------
cap = cv2.VideoCapture(1)  # カメラの指定 (0: iPhoneカメラ, 1:外付けカメラ)
is_gray = False  # グレースケール表示フラグ
is_reverse = False  # 反転表示フラグ
is_stop = False  # 一時停止フラグ

# 実行
while True:
    # フレーム取得
    if is_stop == False:
        ret, frame = cap.read()

    # 表示用フレームのコピー
    display_frame = frame.copy()

    # 表示切替
    if is_gray:
        display_frame = cv2.cvtColor(
            display_frame, cv2.COLOR_BGR2GRAY
        )  # グレースケール変換
    if is_reverse:
        display_frame = cv2.flip(display_frame, 1)  # 左右反転

    # 表示
    cv2.imshow("camera", display_frame)

    # キー入力
    k = cv2.waitKey(1)  # キー入力待機
    if k == ord("g"):
        is_gray ^= True
    elif k == ord("f"):
        is_reverse ^= True
    elif k == ord("s"):
        is_stop ^= True
    elif k == ord("q"):  # qキーで終了
        break

cap.release()
cv2.destroyAllWindows()
