from django.shortcuts import render, redirect
from .models import MstCompanys, MstUsers, UserDetails


# 新規登録 後から削除
def sign_up(request):
    if request.method == 'POST':
        sign_up = MstUsers(UserName=request.POST['UserName'], Pass=request.POST['Pass'])
        sign_up.save()
        return redirect('management/Login.html')
    else:
        return render(request, 'management/Sign_up.html')


# ログイン
def login(request):
    if request.method == 'POST':
        if MstUsers.objects.filter(UserName=request.POST['UserName'], Pass=request.POST['Pass']).exists():
            login = MstUsers.objects.get(UserName=request.POST['UserName'], Pass=request.POST['Pass'])
            return render(request, 'management/User.html', {'login': login})
    else:
        context = {'msg': 'Invalid UserName or Pass'}
        return render(request, 'management/Login.html', context)


# ユーザ詳細の登録
def user(request):
    if request.method == 'POST':
        users = UserDetails(User_Name=request.POST['User_Name'],
                            User_Name_Kana=request.POST['User_Name_Kana'],
                            Gender=request.POST['Gender'],
                            Birthday=request.POST['Birthday'],
                            Type_Of_Contract=request.POST['Type_Of_Contract'],
                            Affiliation_Department=request.POST['Affiliation_Department'],
                            Affiliation_Section=request.POST['Affiliation_Section'],
                            Position=request.POST['Position'],
                            Notices=request.POST['Notices'],
                            )
        users.save()
        return render(request, 'management/Users.html')
    else:
        return render(request, 'management/User.html')


# ユーザ一覧
def users(request):
    # 一覧表示するデータベースを後から変更
    user_list = UserDetails.objects.all()
    # 値一覧を取得
    user_dict = {'users': user_list}
    # ディクショナリーの形で設定
    return render(request, 'management/Users.html', context=user_dict)


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
