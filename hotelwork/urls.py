from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('login',LoginView.as_view(),name = 'login'),
    path('maneeger/dashaboard',DashaboardView.as_view(),name = 'dashaboard'),
    path('maneeger/addcategory',AddCategoryView.as_view(),name = 'add_category'),
    path('maneeget/addroom',AddRoomView.as_view(),name='add_room'),
    path('allroom',AllRoomView.as_view(),name="all_room"),
    path('allcategory',AllCategoryView.as_view(),name ='all_category'),
    path('avalablesingleroom',AvalableRooms.as_view(),name ='avalablerooms'),
    path('rantedrooms', RantedRooms.as_view(), name="rantedroom"),
    path('checkout_user_details',Checkout_user_details.as_view(),name="checkout_user_details"),
    path('maneeger/checkin/<int:pk>/',CheckinView.as_view(),name='checkinuser'),
    path('maneeger/checkout/<int:pk>/',CheckoutView.as_view(),name ='checkout'),
    path('logout',LogoutView.as_view(),name="logout"),

    #################### emplyee manage ########################

    path('addemplyee',AddEmplyeeView.as_view(),name="add_emplyee"),
    path('addemplyeecategory',AddEmplyeeCategory.as_view(),name="add_emplyee_category"),
    path('allcurrentemplyee',AllCurrentEmplyee.as_view(),name="all_current_emplyee"),
    path('allemplyeerecord',AllEmplyeeRecords.as_view(),name="all_emplyee_record"),
    path('emplyee_details/<int:pk>', EmplyeeDetailsView.as_view(), name="emplyee_details"),
    path('removeemplyee/<int:pk>/',RemoveEmplyeeView.as_view(),name='remove_emplyee'),
    path('updatecategory/<int:pk>/',UpdateRoomCategoryView.as_view(),name="updateroomcategory"),


]
