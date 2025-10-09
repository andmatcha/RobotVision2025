import cv2
import numpy as np


# 画像をランダムに切り取るコードをかく
# 画像は配列として読み込まれるので，
# 画像の切り取りは，配列の一部を取り出せばできる．
def random_crop(img_path):
    # 画像の読み込み
    img = cv2.imread(img_path)

    # ランダムに128 x 128のサイズの画像を切り出して表示する
    h = img.shape[0]
    w = img.shape[1]
    top = np.random.randint(0, h - 128)
    left = np.random.randint(0, w - 128)
    crop_img = img[top : top + 128, left : left + 128]

    # 画像をランダムに左右上下反転させる
    if np.random.rand() > 0.5:
        crop_img = cv2.flip(crop_img, 1)  # 左右反転
    if np.random.rand() > 0.5:
        crop_img = cv2.flip(crop_img, 0)  # 上下反転

    return crop_img


if __name__ == "__main__":
    img_path = "./keio.png"
    random_crop(img_path)
