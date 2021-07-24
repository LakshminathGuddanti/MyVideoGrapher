"""MyVideoGrapher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from init import views
from django.contrib.auth import views as vew


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('setupStudio/',views.setupStudio,name = 'setupStudio'),
    path('login/',vew.LoginView.as_view(template_name = 'init/studiologin.html'),name = "login"),
    path('logout/',vew.LogoutView.as_view(template_name = 'init/studiologout.html'), name = 'logout'),
    path('studioProfileInfo',views.studioProfileUpdate, name = 'studioProfileInfo'),
    path('addCam/',views.addCam,name = 'addCam'),
    path('editCamdetails/<int:id>/',views.editCamdetails,name = 'editCamdetails' ),
    path('viewProfile/<int:id>/',views.viewProfile,name = 'viewProfile'),
    path('userRegister/',views.userReg,name = 'userRegister'),
    path('passwordchange/',views.changepwd,name = 'passwordchange'),
    path('camView/<int:id>/',views.camview, name = 'camView'),
    path('deleteCam/<int:id>/',views.deleteCam, name = 'deleteCam'),
    path('orderform/<int:id>/',views.orderform,name = 'orderform'),
    path('myorders/',views.myorders,name = 'myorders'),
    path('viewCustOrder/<int:id>/',views.viewCustOrder,name = 'viewCustOrder'),
    path('mybookings/',views.mybookings,name = 'mybookings'),
]
