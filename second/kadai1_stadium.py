# ライブラリのインポート
import copy

import cv2
import numpy as np


def main():
    # アプリ用のスタジアム、ボール画像を読みこみ
    ball_img = cv2.imread("./image_data/ball.png")
    stadium_img = cv2.imread("./image_data/stadium.png")

    # スタジアムの大きさを適当に変更 (二つ目の引数は(w,h))
    stadium_img = cv2.resize(stadium_img, (1200, 700))

    # / ではなく // で切り捨て
    # ボールの高さ、幅の[半分](半分だから注意！！)
    # (注意!)今回ボールの大きさが H:198、W:200と両方偶数のためこれで良いが、奇数の場合は工夫が必要
    ball_h, ball_w = ball_img.shape[0] // 2, ball_img.shape[1] // 2

    # スタジアムのサイズ
    stadium_h, stadium_w = stadium_img.shape[0], stadium_img.shape[1]

    # ボールの中心位置（中心座標)を初期ではスタジアムの中心に設定
    idx_h = stadium_h // 2
    idx_w = stadium_w // 2

    print(idx_h)


    while True:
        # スタジアムのコピーを作成
        stadium_copy = copy.deepcopy(stadium_img)

        # ボールの再配置
        stadium_copy[
            (idx_h - ball_h) : (idx_h + ball_h), (idx_w - ball_w) : (idx_w + ball_w)
        ] = ball_img

        # 結果画像の表示
        cv2.imshow("output", stadium_copy)

        # ボールを一回で動かす距離(ピクセル数)を決定
        x = 10

        # 終了オプション
        k = cv2.waitKey(1)
        if k == ord("q"):
            break
        # -----------以下記述-----------
        elif k == ord("w"):  # 上
            idx_h -= x
        elif k == ord("s"):  # 下
            idx_h += x
        elif k == ord("a"):  # 左
            idx_w -= x
        elif k == ord("d"):  # 右
            idx_w += x

        # ボールの位置が画面外に出ないように制限
        idx_h = max(ball_h, min(idx_h, stadium_h - ball_h))
        idx_w = max(ball_w, min(idx_w, stadium_w - ball_w))


    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
