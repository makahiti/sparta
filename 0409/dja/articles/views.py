from django.shortcuts import render

# Create your views here.
def index(request):
    # 127.0.0.1:8000/articles/로 요청이 왔을 때, 응답을 처리해 주는 함수다.


    # 응답: articles폴더 밑에 있는 index.html 을 사용해서 사용자에게 결과 화면을 보여주겠다.
    return render(request,"articles/index.html")