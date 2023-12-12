#from django.conf.urls import url
from django.urls import re_path as url
from . import views
app_name='predict_1'
urlpatterns=[
url(r'^(?P<pk>\d+)$',views.PredictRisk_1,name='predict_1')
]
