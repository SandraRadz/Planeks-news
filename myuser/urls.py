from django.urls import path

from myuser.views import LogInView, logout_view, SignUpView, activate_view

urlpatterns = [
    path('login/', LogInView.as_view(), name='user-log-in'),
    path('logout/', logout_view, name='user-log-out'),
    path('signup/', SignUpView.as_view(), name='user-sign-up'),
    path('activate/<uidb64>/<token>', activate_view, name='activate')
]