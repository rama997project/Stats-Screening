from django.urls import path

from . import views

urlpatterns = [
    path('', views.PortfolioScreen, name='PortfolioScreen'),
    path('about/', views.about, name="screen-about")

]