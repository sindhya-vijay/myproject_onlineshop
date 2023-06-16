from django.urls import path
from myapp import views

urlpatterns = [

    path('homepage/', views.homepage, name="homepage"),
    path('category_page/', views.category_page, name="category_page"),
    path('category_data/', views.category_data, name="category_data"),
    path('Display_category/', views.Display_category, name="Display_category"),
    path('Edit_category/<int:dataid>/', views.Edit_category, name="Edit_category"),
    path('Update_category/<int:dataid>/', views.Update_category, name="Update_category"),
    path('Delete_category/<int:dataid>/', views.Delete_category, name="Delete_category"),
    path('Add_product/', views.Add_product, name="Add_product"),
    path('productdata/', views.productdata, name="productdata"),
    path('productdisplay/', views.productdisplay, name="productdisplay"),
    path('Edit_product/<int:dataid>/', views.Edit_product, name="Edit_product"),
    path('Update_product/<int:dataid>/', views.Update_product, name="Update_product"),
    path('Delete_product/<int:dataid>/', views.Delete_product, name="Delete_product"),
    path('Loginpage/', views.Loginpage, name="Loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('contact_display/', views.contact_display, name="contact_display")

]

