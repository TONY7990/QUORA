from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('new/', views.new_question, name='new_question'),
    # path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
    path('question/<int:question_id>/edit/', views.edit_question, name='edit_question'),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path('answer/<int:answer_id>/edit/', views.edit_answer, name='edit_answer'),
    path('question/<int:pk>/edit/',views.edit_question, name='edit_question'),
    path('answer/<int:answer_id>/delete/', views.delete_answer, name='delete_answer'),
     path('question/<int:question_id>/submit-answer/', views.submit_answer, name='submit_answer'),

]
