from django.urls import path, re_path

from items.views import CreateItemAPIView, GetItemAPIView, ListItemsAPIView, UpdateItemAPIView, DeleteItemAPIView

urlpatterns = [
    path('create/', CreateItemAPIView.as_view(), name='create-item'),
    path('', ListItemsAPIView.as_view(), name='list-item'),
    re_path(r'(?P<pk>\d+)/$', GetItemAPIView.as_view(), name='get-items'),
    re_path(r'update/(?P<pk>\d+)/$', UpdateItemAPIView.as_view(), name='update-items'),
    re_path(r'delete/(?P<pk>\d+)/$', DeleteItemAPIView.as_view(), name='delete-items'),
]
