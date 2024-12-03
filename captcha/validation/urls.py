from django.urls import path
from validation.views import *
urlpatterns = [
    path('a/',Aview.as_view()),
    path('b/',Bview.as_view()),
    path('c/',Cview.as_view()),
    path('d/',Dview.as_view()),
    path('e/',Eview.as_view()),
    path('f/',Fview.as_view()),
    path('g/',Gview.as_view()),
]