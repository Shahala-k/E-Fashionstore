from django.urls import path
from frontapp import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('aboutuspage/',views.aboutuspage,name="aboutuspage"),
    path('shoppage/',views.shoppage,name="shoppage"),
    path('blogpagee/',views.blogpagee,name="blogpagee"),
    path('prod/<itemcatg>',views.prod,name="prod"),
    path('productsingle/<int:dataid>/',views.productsingle,name="productsingle"),
    path('savecontactpage/',views.savecontactpage,name="savecontactpage"),
    path('userloginpage/',views.userloginpage,name="userloginpage"),
    path('saveuserlogin/',views.saveuserlogin,name="saveuserlogin"),
    path('custemerlogin/',views.custemerlogin,name="custemerlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('savecartpage/',views.savecartpage,name="savecartpage"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('deletecartitem/<int:dataid>/',views.deletecartitem,name="deletecartitem"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
    path('saveuserdetails/',views.saveuserdetails,name="saveuserdetails")
]