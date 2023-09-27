
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index_page,name='index'),
    path('register_page/',views.register_page,name='register'),
    path('about/',views.about_us,name='about'),
    path('contact/',views.contact_page,name='contact'),
    path('category/',views.category,name='category'),
    path('products/<str:name>/',views.product,name='products'),
    path('search',views.search_view,name='search'),
    path('search1',views.search_view1,name='search1'),
    path('add',views.add_view,name='add'),
    path('remove_item/', views.remove_item, name='remove_item'),
    path('viewcart',views.view_cart,name='viewcart'),
    path('cart/', views.admin_cart_view, name='admin_cart'),
]
