from django.urls import path
from crafts_likes import views

urlpatterns = [
    path('likes/', views.LikesList.as_view()),
    path('like/<int:post_id>', views.like,name='like'),
    path('unlike/<int:post_id>', views.unlike,name='unlike')
]