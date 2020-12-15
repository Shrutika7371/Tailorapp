from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('newu', views.newu, name='newu'),
    path('olduc/<int:pk>', views.olduc, name='olduc'),
    path('showc/<int:pk>', views.showc, name='showc'),
    path('newforms', views.newforms, name='newforms'),
    path('searchrt', views.searchrt, name='searchrt'),
    path('searchnav', views.searchnav, name='searchnav'),
    path('reorder', views.reorder, name='reorder'),
    path('completeup/<int:pk>', views.completeup, name='completeup'),
    path('updateform/<int:pk>', views.updateform, name='updateform'),
    path('updatesubmit', views.updatesubmit, name='updatesubmit'),
    path('delcust/<int:pk>', views.delcust, name='delcust'),
    path('export', views.export_xls, name='export'),
    path('dologin', views.dologin, name='dologin'),
    path('logout', views.logout_view , name='logout')
]