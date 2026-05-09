from django.urls import path, include
from . import views


app_name = "api-v1"

urlpatterns = [
    #path('post/',PostList,name='Post-List'),
    path('post/',views.PostList.as_view(),name='Post-List'),
    path('post/<int:id>/',views.postDetail,name="post-detail"),
]