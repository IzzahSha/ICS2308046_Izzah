from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path("view/",views.view, name='view'),
    path("dbstudent/", views.dbstudent, name='dbstudent'),
    path("dbbook/", views.dbbook, name = 'dbbook'),
    path("dbborrow/",views.dbborrow, name= 'dbborrow'),
    path("course/",views.course, name='course'),
    path("newmentor/",views.newmentor, name='newmentor'),
    path("search_course/", views.search_course, name="search_course"),
    path("course/update_course/<str:code>",views.update_course, name='update_course'),
    path("course/update_course/save_update_course/<str:code>",views.save_update_course, name='save_update_course'),
    path("course/delete_course/<str:code>", views.delete_course, name='delete_course'),
]