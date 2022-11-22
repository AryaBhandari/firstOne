from django.urls import path
from .views import dashboard,changeStaffImage,editProfile
from student.views import paidHistory
urlpatterns=[
    path('changesimage/', changeStaffImage, name='changesimage'),
    path('dashboard/',dashboard, name='staffdash'),
    path('editprofile/<int:id>',editProfile, name='editstfprofile'),
    path('paidhistory/<int:id>',paidHistory,name='stfpaidhistory'),

]