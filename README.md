# IdolWorldCup

2023년 09월 02일
메인 화면 구성 
16강 화면 - 이미지 랜덤으로 업로드 
팝업창 - 라운드 선택하도록 (근데 이건 안됨)

해야할 것 : 
        16강에서 선택한 이미지들이 8강에서 업로드되야함
        16강에서 선택할 때 마다 (8-1)(8-2)... 이런식으로 되야함
        팝업창이 뜰 수 있도록 
        
        

2023년 09월 18일
팝업창 구성 완료
16강 / 8강 / 4강 텍스트 변경 + 중복되지 않게 랜덤 이미지가 뜨도록 함

해야할 것:
        4강 먼저 구현해보고 있는데 선택한 이미지 중 하나가 뜨질 않음
        디자인 깔끔하게 하기 (이건 마지막에 하면 될 듯)
        버튼 클릭시 임펙트나 소리넣기 (이것도 마지막에)
        
        일승이형이 랭킹부분 구현해줘으면 좋겠음 (넘 어렵나 ㅜㅜ)
        
        
2023년 09월 20일
성공한 게 없음...
4강 1->2로 넘어가지는 건 성공했으나 여기서 고른 이미지가 결승전에서 뜨질 않고 랜덤으로 뜸...
셀릭이미지 0이 작동이 안하는듯
4강을 다 선택하면 결승 페이지로 넘어가지게 구현하거나 셀릭한 이미지가 뜨도록 수정해야할듯 ㅜㅜ 
근데 안되는 걸 어카냐
        
        
        
        
        
        
        디자인 이뻐서 나중에 참고하기 
        /*<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>이상형 월드컵 4강</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }

        h1 {
            background-color: #007bff;
            color: #fff;
            padding: 10px;
        }

        #tournament {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }

        .match {
            margin-bottom: 20px;
            background-color: #fff;
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            font-size: 18px;
            margin-bottom: 10px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            margin: 5px;
            cursor: pointer;
        }

        #winner {
            margin-top: 20px;
            font-size: 24px;
        }
    </style> /*