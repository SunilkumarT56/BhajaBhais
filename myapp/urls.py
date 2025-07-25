from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('legacy',views.legacy , name='legacy'),
    path('legacy_more',views.legacy_more , name='legacy-more'),
    path('particular_legacy/<legacy_id>',views.particular_legacy , name='particular-legacy'),
    path('faculty',views.faculty,name='faculty'),
    path('students',views.students , name='students'),
    path('galary',views.galary,name='galary'),
    path('viewmore_galary',views.viewmore_galary,name='viewmore-galary'),
    path('sponcers',views.sponcers, name='sponcers'),
    path('sponcers', views.js_download_page, name='js_download'),
    path('contact' , views.contact , name='contact'),
    path('part_group/<group_id>',views.part_group, name='part-group'),
    path('first',views.first,name='first'),
    path('second',views.second,name='second'),
    path('third',views.third , name='third'),
    path('fourth',views.fourth , name='fourth'),
]