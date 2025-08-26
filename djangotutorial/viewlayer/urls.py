from django.urls import path

from . import views

urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    path("current_datetime/", views.current_datetime),
    path("my_view/", views.my_view),
    path("about/", views.AboutView.as_view()),
    path("async/", views.AsyncView.as_view()),
]