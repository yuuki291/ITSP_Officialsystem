from django.conf.urls import url
from . import views

# 後から変更
urlpatterns = [
    url("Sign_up", views.sign_up, name='sign_up'),
    url("Login", views.login, name='login'),
    url("Users", views.users, name='users'),
    url("User", views.user, name='user'),
    url("Companys", views.companys, name='companys'),
    url("Company", views.company, name='company'),
    url("CompanyInfo", views.companyinfo, name='companyinfo'),
    url("Agreement", views.agreement, name='agreement'),
    url("Header", views.header, name='header'),
    url("Footer", views.footer, name='footer'),
    url("SiteMap", views.sitemap, name='sitemap'),
    url("SearchDialog", views.searchdialog, name='searchdialog'),
    url("MessageDialog", views.messagedialog, name='messagedialog'),
    url("InterviewHistory", views.interviewhistory, name='interviewhistory'),
    url("Application", views.application, name='application'),
    url("Roster", views.roster, name='roster')
]