from django.urls import path
from factors.views import ActivityCreateAPIView,GetMyActivity

urlpatterns = [
    path('create/', ActivityCreateAPIView.as_view(), name='create_activity'),
    path('my_activity/',GetMyActivity.as_view(), name="get_my_activity")
]
