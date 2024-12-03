from django.contrib import admin
from django.urls import path
from generic.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', log),
    path('get_validCode_img/', get_valid_code_img),
    path('mathcaptcha/', captcha_view, name='mathcaptcha'),
]
