from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('factors/', views.factors, name='factors'),
    path('<model>_help/<id>/', views.factors, name='grid_help'),
    path('<model>_factorhelp/<id>/', views.factor_help, name='factor_help'),
    path('technologies/', views.technologies, name='technologies'),
    path('techs_selected/', views.techs_selected, name='techs_selected'),
    path('technologies/<id>/help/', views.technologies_help, name='technologies_help'),
    path('choice/<tech_id>/', views.tech_choice, name='tech_choice'),
    path('pdf/<filename>', views.pdf, name='pdf'),
    path('solution/', views.solution, name='solution'),
    path('choose_meta/<criterion_id>/',views.choose_meta, name='choose_meta'),
    path('reset_all/', views.reset_all, name='reset_all'),
    path('reset_techs/', views.reset_techs, name='reset_techs'),
    path('toggle_button/<btn_name>/', views.toggle_button, name='toggle_button'),
    path('init/', views.init, name='init'),
]
