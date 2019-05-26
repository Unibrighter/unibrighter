from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # index, detail, result, vote
    path('<int: question_id>/', views.detail, name = 'detail'),
    path('<int: question_id>/result/', views.results, name = 'result'),
    path('<int: question_id>/vote/', views.vote, name = 'vote')
]