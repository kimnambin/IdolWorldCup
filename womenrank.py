from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Flask 앱 초기화
app = Flask(__name__)

# SQLite 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///womenrank.db'
db = SQLAlchemy(app)

# 데이터 모델 정의
class WomenRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imageName = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(80), nullable=False)
   

# 데이터베이스 생성
with app.app_context():
    db.create_all()

# 메인 페이지 라우팅
@app.route('/')
def index():
    # SQLite에서 데이터 가져오기
    womenranks = WomenRank.query.all()
    return render_template('womentest.html', womenranks=WomenRank)

# 파일 업로드 처리 라우팅
@app.route('/upload', methods=['POST'])
def upload():
    return "파일 업로드 완료!!"

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)
