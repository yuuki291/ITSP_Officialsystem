from django.shortcuts import render

# 後から変更


def login(request):
    return render(request, 'management/Login.html')


def user(request):
    return render(request, 'management/User.html')


def users(request):
    return render(request, 'management/Users.html')


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

