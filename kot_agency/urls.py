"""kot_agency URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from kot_agency import settings
from kot_location import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('kot/add', views.kot_add),
    path('kot/<int:id>/delete/', views.kot_delete),
    path('kot/<int:id>', views.kot_details, name="kot-details"),
    path('kot/<int:id>/update', views.kot_update),
    path('kot_list/', views.kot_list),
    path('owner/<int:id>/offers', views.kot_offers),
    path('renter/offers', views.renter_favorite_offers),
    path('kot/validation_list/', views.kot_validation_list),
    path('kot/<int:id>/check/', views.kot_check),
    path('login/', views.login_user),
    path('register/', views.register_user),
    path('logout/', views.logout_user)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
