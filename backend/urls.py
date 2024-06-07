from django.urls import path
from backend import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('category/', views.category, name="category"),
    path('display_cate/', views.display_cate, name="display_cate"),
    path('save_cate/', views.save_cate, name="save_cate"),
    path('edit_cate/<int:cateid>/', views.edit_cate, name="edit_cate"),
    path('update_cate/<int:cateid>/', views.update_cate, name="update_cate"),
    path('delete_cate/<int:cateid>/', views.delete_cate, name="delete_cate"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('product_page/', views.product_page, name="product_page"),
    path('save_product/', views.save_product, name="save_product"),
    path('display_products/', views.display_products, name="display_products"),
    path('edit_products/<int:proid>/', views.edit_products, name="edit_products"),
    path('update_pro/<int:proid>/', views.update_pro, name="update_pro"),
    path('delete_pro/<int:proid>/', views.delete_pro, name="delete_pro"),


]