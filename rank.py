from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# 이미지 파일이 있는 디렉토리 경로
IMAGE_DIR = 'static/img/'

# 우승한 이미지의 경로
WINNER_IMAGE = 'static/img/winner.jpg'  # 예시 경로, 실제 경로로 대체해야 합니다.

@app.route('/')
def index():
    # 이미지 파일 목록을 가져오기
    image_files = os.listdir(IMAGE_DIR)
    # 이미지 파일 경로를 리스트에 저장
    images = [os.path.join(IMAGE_DIR, img) for img in image_files]
    # 이미지 파일을 무작위로 섞기
    random.shuffle(images)
    # 두 개의 이미지만 선택하여 전달
    image1 = images[0]
    image2 = images[1]
    return render_template('ranking.html', image1=image1, image2=image2, winner_image=WINNER_IMAGE)

if __name__ == '__main__':
    app.run(debug=True)
