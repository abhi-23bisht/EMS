from django.urls import path
from .views import *

urlpatterns = [
    path('home/',view_home),
    path('add-emp/',view_add_emp),
    path('del-emp/<int:id>/',view_delete_emp),
    path('update-emp/<int:id>/',view_update_emp),
    path('signup/',view_signup),
    path('login/',view_login),
]
