from django.conf.urls import url, include
from django.urls import path
from api.models import Profile
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from . import views

# Serializers define the API representation.
# class RequestSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Request
#         fields = ('name', 'message', 'created_at')

# class DoctorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ('first_name', 'last_name', 'specialty', 'gender')

# # ViewSets define the view behavior.
# class RequestViewSet(viewsets.ModelViewSet):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer

# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'requests', RequestViewSet)
# router.register(r'doctors', DoctorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sms', views.sms, name='sms'),
    path('patient/new', views.new_patient, name='patient'),
    path('patient', views.patient, name='patient'),
    path('doctor/patients', views.doctor_patients, name='doctor_patient'),
    path('doctor/patients/<int:request_id>', views.doctor_patients_detail, name='doctor_patients_detail'),
    path('', views.index, name='index'),
    path('profile/edit', views.update_profile, name='edit'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('request/<int:request_id>', views.detail, name='detail'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

