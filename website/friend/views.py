from django.http import HttpResponse

def BestFriend(request):
    return HttpResponse('<body bgcolor="green"> Hello you are my Best friend<br></body>')

def NormalFriend(request):
    return HttpResponse('<body bgcolor="red"> Hello you are my Normal friend<br></body>')

def Test3(request):
    return HttpResponse('<body bgcolor="red"> This is Test3 from Friend<br></body>')