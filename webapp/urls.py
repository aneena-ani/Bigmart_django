from django.urls import path
from webapp import views


urlpatterns=[
        path('',views.homepage,name="home"),
        path('about/',views.aboutpage,name="about"),
        path('contact/', views.contactpage, name="contact"),
        path('ourproducts/', views.ourproducts, name="ourproducts"),
        path('savecontact/', views.savecontact, name="savecontact"),
        path('contactdata/', views.contactdata, name="contactdata"),
        path('deletedata/<int:conid>/', views.deletedata, name="deletedata"),
        path('pro_filtered/<cat_name>/', views.pro_filtered, name="pro_filtered"),
        path('singleproduct/<int:proid>/', views.singleproduct, name="singleproduct"),
        path('reg_page/', views.reg_page, name="reg_page"),
        path('save_reg/', views.save_reg, name="save_reg"),
        path('userlogin/', views.userlogin, name="userlogin"),
        path('userlogout/', views.userlogout, name="userlogout"),
        path('save_cart/',views.save_cart,name="save_cart"),
        path('cart_page/', views.cart_page, name="cart_page"),
        path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),
        path('userlogin_page/',views.userlogin_page,name="userlogin_page"),




]