#from django.contrib import admin
from django.urls import path
from .views import signupview ,loginview,listview,detailview,CreateClass,logoutview,evaluationview
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/',signupview, name='signup'),
    path('login/',loginview,name='login'),
    path('list/',listview,name='list'),
    path('detail/<int:pk>/',detailview,name='detail'),
    path('create/',CreateClass.as_view,name='create'),
    path('logout/',logoutview,name='logout'),
    path('evaluation/<int:pk>',evaluationview,name='evaluation'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

"""
urlpatterns = [
    path('admin/',admin.site.urls),
]

+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


"""