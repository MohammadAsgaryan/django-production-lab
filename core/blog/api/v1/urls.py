from django.urls import path, include
from .views import *


app_name = "api-v1"

urlpatterns = [
    path('post/',PostList,name='Post-List'),
    path('post/<int:id>/',postDetail,name="post-detail"),
]