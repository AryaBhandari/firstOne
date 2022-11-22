from django.urls import path
from .views import dashboard,changePImage,editProfile,editEducation,removeEducation,removeSkill,paidHistory
urlpatterns=[
    path('dashboard/',dashboard,name='studentdash'),
    path('changepimage/',changePImage,name='changepimage'),
    path('editprofile/<int:id>',editProfile,name='editprofile'),
    path('editeducation/<int:id>',editEducation,name='editeducation'),
    path('removeedu/<int:id>',removeEducation,name='removeeducation'),
    path('removeskill/<int:id>',removeSkill,name='removeskill'),
    path('paidhistory/<int:id>',paidHistory,name='paidhistory'),
]