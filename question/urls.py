from django.conf.urls import url

from . import views

	
urlpatterns = [
    # ex: /question/
    url(r'^$', views.index, name='index'),
    # ex: /question/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    
  

  

]