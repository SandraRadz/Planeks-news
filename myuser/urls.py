from django.urls import path

from myuser.views import LogInView, logout_view, SignUpView

urlpatterns = [
    path('login/', LogInView.as_view(), name='user-log-in'),
    path('logout/', logout_view, name='user-log-out'),
    path('signup/', SignUpView.as_view(), name='user-sign-up')
]