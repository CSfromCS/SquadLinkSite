from django.urls import path
from .views import SquadLinkUserLogInView, SquadLinkUserCreationView, SquadLinkUserView

app_name = 'UserProfile'

urlpatterns = [
    path('register/', SquadLinkUserCreationView.as_view(), name='register'),
    path('signin/', SquadLinkUserLogInView.as_view(), name='signin'),
    path('view', SquadLinkUserView.as_view(), name='view-profile')
]
