from django.urls import path
from .views import GradeViewSet

urlpatterns = [
    path('grades/', GradeViewSet.as_view({
        'get':'list',
        'post':'create'

        })),
    path('grades/<str:id>', GradeViewSet.as_view({
        'get': 'retrieve'
    }))
]