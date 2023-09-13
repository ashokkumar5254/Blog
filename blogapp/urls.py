from django.urls import path
#from blogapp import views
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('detail_page/<int:pk>',views.detail_page,name='detail_page'),
    path('detail_editpage/<int:pk>',views.detail_editpage,name='detail_editpage'),
    path('delete/<int:pk>',views.delete_view,name='delete')

]
