from django.urls import path
from .views import signin,signout,signup,signupRequest,signupDetails,deleteUser,deleteSignupRequest,Dashboard,studentList,studentDetail
urlpatterns=[
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('signup/',signup,name='signup'),
    path('requests/', signupRequest, name='signuprequest'),
    path('signupdetails/<int:id>', signupDetails, name='signupdetails'),
    path('deleteuser/<int:id>', deleteUser, name='deleteuser'),
    path('deleterequest/<int:id>', deleteSignupRequest, name='deleterequest'),
    path('dashboard/<int:id>', Dashboard, name='dashboard'),
    path('students', studentList, name='studentlist'),
    path('studentdetail/<int:id>', studentDetail, name='studentdetail'),
]