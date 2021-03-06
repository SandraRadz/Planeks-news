from django.urls import path

from news.views import NewsList, NewDetail, CreateNew, thanks_view

urlpatterns = [
    path('', NewsList.as_view(), name='news-list'),
    path('new/<int:pk>', NewDetail.as_view(), name='new-item'),
    path('new/create-new', CreateNew.as_view(), name='create-new'),
    path('new/thanks', thanks_view, name='thanks-view')
]