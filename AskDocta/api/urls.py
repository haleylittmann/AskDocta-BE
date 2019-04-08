from django.conf.urls import url, include
from django.urls import path
from api.models import Request, Doctor
from rest_framework import routers, serializers, viewsets
from django.contrib import admin

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
    path('request', views.index, name='index'),
    path('', views.index, name='index'),
    path('profile/edit', views.update_profile, name='edit'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('request/<int:request_id>', views.detail, name='detail')
]
