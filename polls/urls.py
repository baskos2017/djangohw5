from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('review_success/', views.review_success, name='review_success'),
]
