#from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy

# Flask 앱 초기화
#app = Flask(__name__)

# SQLite 데이터베이스 설정
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manrank.db'
#db = SQLAlchemy(app)

# 데이터 모델 정의
#class ManRank(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #imageName = db.Column(db.String(255), nullable=False)
    #name = db.Column(db.String(80), nullable=False)
   

# 데이터베이스 생성
#with app.app_context():
 #   db.create_all()

# 메인 페이지 라우팅
#@app.route('/')
#def index():
    # SQLite에서 데이터 가져오기
 #   manranks = ManRank.query.all()
  #  return render_template('mantest.html', manranks=manranks)

# 파일 업로드 처리 라우팅
#@app.route('/upload', methods=['POST'])
#def upload():
 #   return "파일 업로드 완료!!"

# 앱 실행
#if __name__ == '__main__':
 #   app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# 라우트 설정
@app.route('/')
def index():
    # 아이돌 데이터
    idols = [
        {'id': 1, 'name': '갓세븐 진영', 'image': '/static/img/mm01.jpg'},
        {'id': 2, 'name': 'EXO 백현', 'image': '/static/img/mm02.jpg'},
        # 나머지 아이돌 데이터도 추가
    ]
    return render_template('mantest.html', idols=idols)

if __name__ == '__main__':
    app.run(debug=True)



