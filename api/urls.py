from django.urls import path, include, re_path
from . import views #. means current folder

# URL conf
urlpatterns = [
    path('files/', views.FileReadView.as_view()),
    path('files/<int:id>/', views.FileReadView.as_view()),
    path('files/upload/',  views.FileWriteView.as_view()),
    path('files/delete/<int:id>/',  views.FileWriteView.as_view()),
    path('files/download/<int:id>/', views.FileDownloadView.as_view()),
]
