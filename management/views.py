from django.shortcuts import render, redirect
from .models import MstCompanys, MstUsers


# 新規登録 後から削除
def sign_up(request):

    if request.method == 'POST':
        sign_up = MstUsers(UserName=request.POST['UserName'], Pass=request.POST['Pass'])
        sign_up.save()
        return redirect('management/Login.html')
    else:
        return render(request, 'management/Sign_up.html')


def login(request):
    return render(request, 'management/Login.html')


def user(request):
    return render(request, 'management/User.html')


# Login機能
def users(request):
    if request.method == 'POST':
        if MstUsers.objects.filter(UserName=request.POST['UserName'], Pass=request.POST['Pass']).exists():
            login = MstUsers.objects.get(UserName=request.POST['UserName'], Pass=request.POST['Pass'])
            return render(request, 'management/Users.html', {'login': login})
    else:
        context = {'msg': 'Invalid UserName or Pass'}
        return render(request, 'management/Login.html', context)


def companys(request):
    return render(request, 'management/Companys.html')


def company(request):
    return render(request, 'management/Company.html')


def companyinfo(request):
    return render(request, 'management/CompanyInfo.html')


def agreement(request):
    return render(request, 'management/Agreement.html')


def header(request):
    return render(request, 'management/Header.html')


def footer(request):
    return render(request, 'management/Footer.html')


def sitemap(request):
    return render(request, 'management/SiteMap.html')


def searchdialog(request):
    return render(request, 'management/SearchDialog.html')


def messagedialog(request):
    return render(request, 'management/MessageDialog.html')


def interviewhistory(request):
    return render(request, 'management/InterviewHistory.html')


def application(request):
    return render(request, 'management/Application.html')


def roster(request):
    return render(request, 'management/Roster.html')
