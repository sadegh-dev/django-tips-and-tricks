from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome/', views.home, name='my-welcome') ,
    path('welcome2/', views.Home2.as_view(), name='welcome-2') ,
    path('weblog/', include('blog.urls', namespace='weblog'))
    
]