# ライブラリのインポート
import cv2
import numpy as np


def filtering(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSVによる上限、下限の設定　 ([Hue, Saturation, Value])
    hsvLower = np.array([6, 0, 0])  # 下限
    hsvUpper = np.array([23, 150, 155])  # 上限

    # HSVからマスクを作成
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)

    # medianblurを用いてノイズ成分を除去
    blur_mask = cv2.medianBlur(hsv_mask, ksize=3)
    return hsv_mask, blur_mask


def main():
    cap = cv2.VideoCapture(1)

    # 実行
    while True:
        # Webカメラのフレーム取得
        ret, frame = cap.read()
        cv2.imshow("camera", frame)

        hsv_mask, blur_mask = filtering(frame)
        cv2.imshow("hsv_mask", hsv_mask)
        cv2.imshow("mask_with_medianblur", blur_mask)

        # 終了オプション
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
