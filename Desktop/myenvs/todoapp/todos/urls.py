from django.conf.urls import url
from todos import views

urlpatterns =  [
	url(r'^$',views.index, name='index'),
	url(r'^create$',views.create, name='create'),
	url(r'^about$',views.about, name='about'),
	url(r'^contact$',views.contact, name='contact'),
	url(r'^save$',views.save, name='save'),
	url(r'^edit/todos/(\d+)$',views.edit, name='edit'),

]
