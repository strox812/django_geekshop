from django.urls import path
from adminapp import views as adminapp



app_name = 'adminapp'


urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.user_read, name='user_read'),
    path('users/update/<pk>', adminapp.user_update, name='user_update'),
    path('users/delete/<pk>', adminapp.user_delete, name='user_delete'),

    # path('', adminapp., name=''),
    # path('', adminapp., name=''),
    # path('', adminapp., name=''),
    # path('', adminapp., name=''),
    #
    # path('', adminapp., name=''),
    # path('', adminapp., name=''),
    # path('', adminapp., name=''),
    # path('', adminapp., name=''),
]