from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('login/',views.login,name='login'),
    path('course/',views.Course,name='course'),
    path('create_course/',views.Course_Create,name='create_course'),
    path('del_course',views.Del_course,name='del_course'),
    path('edit_course/<int:id>/',views.Edit_course,name='edit_course'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.Profile,name='profile')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)