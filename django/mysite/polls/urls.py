
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path( 'graph', views.graph, name="graph"),
    path('BCG',views.bcg, name ="bcg"),
    path('DTP1',views.DTP1, name ="DTP1"),
    path('DTP3',views.DTP3, name ="DTP3"),
    path('HepB3',views.HepB3, name ="HepB3"),
    path('HepBB',views.HepBB, name ="HepBB"),
    path('Hib3',views.Hib3, name ="Hib3"),
    path('IPV1',views.IPV1, name ="IPV1"),
    path('MCV1',views.MCV1, name ="MCV1"),
    path('MCV2',views.MCV2, name ="MCV2"),
    path('PCV3',views.PCV3, name ="PCV3"),
    path('Pol3',views.Pol3, name ="Pol3"),
    path('ROTAC',views.ROTAC, name ="ROTAC"),
    path('YFV',views.YFV, name ="YFV")
    


]
