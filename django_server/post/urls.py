from . import views
from django.urls import path
app_name="post"

urlpatterns = [
	path('create/', views.CreatePost, name='create'),
	path('', views.Index, name='post_list'),

	]

