# ライブラリのインポート
import cv2
import numpy as np


# テキスト表示を追加する関数
def add_text(frame, text, position):
    cv2.putText(
        frame,
        text=text,
        org=position,
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.8,
        color=(0, 255, 255),
        thickness=2,
        lineType=cv2.LINE_AA,
    )


def circle_labeling(frame, color, min_area=1000, max_area=250000, min_circularity=0.8):
    # frame: 入力画像
    # color: 検出する色 blue/green/pink
    # min_area: 検出対象の最小面積
    # max_area: 検出対象の最大面積
    # min_circularity: 検出対象の最小円形度（0-1の範囲、1が完全な円）

    # 色の範囲
    # HSVRange["blue"]["lower"]で値を取り出せる
    HSVRange = {
        "blue": {"lower": np.array([100, 50, 50]), "upper": np.array([120, 255, 255])},
        "green": {"lower": np.array([50, 50, 50]), "upper": np.array([80, 255, 255])},
        "pink": {"lower": np.array([160, 50, 50]), "upper": np.array([170, 255, 255])},
    }

    # BGR→HSV変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # HSVによる上限、下限の設定
    if color not in HSVRange:
        raise ValueError("Invalid color. Choose from 'blue', 'green', or 'pink'.")
    # HSVからマスクを作成
    hsv_mask = cv2.inRange(hsv, HSVRange[color]["lower"], HSVRange[color]["upper"])
    # ノイズ成分を除去
    blur_mask = cv2.medianBlur(hsv_mask, ksize=3)
    # ラベリング処理
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blur_mask)

    # すべてのラベルをチェック（背景ラベル0を除く）
    if nlabels <= 1:
        return frame

    for label in range(1, nlabels):
        # ラベルの面積を取得
        area = stats[label, cv2.CC_STAT_AREA]

        # 面積のフィルタリング
        if area < min_area or area > max_area:
            continue

        # 該当ラベルのマスクを作成
        label_mask = (labels == label).astype(np.uint8) * 255

        # 輪郭を検出
        contours, _ = cv2.findContours(
            label_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        if not contours:
            continue

        # 最小外接円を取得
        (circle_x, circle_y), radius = cv2.minEnclosingCircle(contours[0])

        # 円形度を計算: 実面積 / 外接円の面積
        # 完全な円なら1.0、細長い形状なら小さな値になる
        circle_area = np.pi * (radius**2)
        circularity = area / circle_area if circle_area > 0 else 0

        # 円形度のフィルタリング
        if circularity < min_circularity:
            continue

        center = (int(circle_x), int(circle_y))
        radius = int(radius)

        # フレームに円を描画
        cv2.circle(frame, center, radius, (0, 0, 255), 3)
        # 中心点を描画（塗りつぶし）
        cv2.circle(frame, center, 10, (255, 200, 0), -1)

        # テキスト表示位置（円の右下）
        text_x = center[0] + int(radius * 0.8)
        text_y = center[1] + int(radius * 0.8)

        # テキスト情報を表示（円形度も追加）
        add_text(frame, f"Color: {color}", (text_x, text_y))
        add_text(frame, f"Center X: {center[0]}", (text_x, text_y + 30))
        add_text(frame, f"Center Y: {center[1]}", (text_x, text_y + 60))
        add_text(frame, f"Radius: {radius}", (text_x, text_y + 90))
        add_text(frame, f"Circularity: {circularity:.2f}", (text_x, text_y + 120))

    return frame


def main():
    cap = cv2.VideoCapture(1)

    # 実行
    while True:
        # -----------以下記述-----------

        # circle描画はURL参照→(http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html)
        # circle描画の ”引数:線幅” を -1 に設定することで塗り潰しが可能(円の中心点の描画に必要!)

        # Webカメラのフレーム取得
        ret, frame = cap.read()

        circle_labeling(frame, "blue")
        circle_labeling(frame, "green")
        circle_labeling(frame, "pink")
        cv2.imshow("camera", frame)

        # 終了オプション
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    # カメラリリース、windowの開放
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
