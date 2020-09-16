from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="pizza-index"),
    path('pizzas/<int:pizza_id>', views.show, name='adoption-show'),
    #path('404', views.NotFound, name='404-not-found')
]

handler500 = views.handle500
handler404 = views.handle404