from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index-page'),
    path('register-user/', register_user, name='register-user'),
    path('login-user/', login_user, name='login-user'),
    path('logout-user/', logout_user, name='logout-user'),
    path('add-post/', add_post, name='add-post'),
    path('add-business/', create_business, name='add-business'),
    path('add-hood/', create_neigborhood, name='add-hood'),
    path('delete-business/<int:id>', delete_business, name='delete-business'),
    path('delete-hood/<int:id>', delete_neighborhood, name='delete-hood'),
    path('find-business/', find_business, name='find-business'),
    # path('view-project/<int:id>', view_project, name='view-project'),
    path('profile/', my_profile, name='profile'),
    # path('project-list/', project_list, name='project-list'),
    # path('user-list/', user_list, name='user-list'),
]