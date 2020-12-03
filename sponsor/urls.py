from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

from accounts.viewsets import (
    UserViewSet,
    SchoolViewSet,
    ReasonViewSet,
    SponserViewSet,
    SponseeListViewSet,
    SponseeReasonViewSet
)
from accounts.views import (
    CreateSponseeView,
    CreateSponserView,
    MyTokenObtainPairView,
    add_sponsorship
)

router = DefaultRouter()
router.register('reasons', SponseeReasonViewSet, basename="reasons")
router.register('sponsees', SponseeListViewSet, basename="sponsees")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/createsponsee/', CreateSponseeView.as_view()),
    path('api/createsponser/', CreateSponserView.as_view()),
    # view for sponsees
    path(
        'myreason/',
        ReasonViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'post': 'create',
            'patch': 'partial_update'
        })
    ),
    # view for sponsors and staff
    # path(
    #     'reasons/<int:pk>',
    #     SponseeReasonViewSet.as_view({'get': 'retrieve'})
    # ),
    # view for sponsees
    path(
        'myschool/',
        SchoolViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'post': 'create',
        })
    ),
    # view for sponsors and staff
    path(
        'schools/',
        SchoolViewSet.as_view({'get': 'list', 'get': 'retrieve'})
    ),
    # view for sponsees
    path(
        'mysponseeprofile/',
        SponseeListViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update'
        })),
    # view for sponsors and staff
    path(
        'sponsees/',
        SponseeListViewSet.as_view({
            'get': 'list',
            # 'get': 'retrieve',
        })),
    # views for sponsors and staff and sponsees
    path(
        'myuserprofile/',
        UserViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update'
        })),
    path(
        'api/token/',
        MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'addsponsorship/<str:username>',
        add_sponsorship,
        name='add_sponsorship'
    ),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
