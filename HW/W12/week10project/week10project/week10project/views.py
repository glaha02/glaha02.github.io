from django.shortcuts import render

def home(request):
    return render(request, 'phone.html', {})


from django.http import HttpResponse

def ccu410125015_function(request):
    user=request.GET['UserName']
    mail=request.GET['UserMail']
    return HttpResponse(user + ', 你輸入的email是' + mail)
