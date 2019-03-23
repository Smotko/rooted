"""rooted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("question/<int:question_id>/upvote", views.upvote),
    path("question/<int:question_id>/downvote", views.downvote),
    path("question/<int:question_id>", views.list_question),
    path("<str:language_type>/question/", views.post_question),
    path("<str:language_type>/questions/", views.list_questions),
    path("<str:language_type>/answer/<int:question_id>", views.post_answer),
    path("", views.index),
]
