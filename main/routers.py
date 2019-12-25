from rest_framework.routers import DefaultRouter


from newapp.apiviews import (
    CastViewSet,
    MovieViewSet,
    DirectorViewSet
)
router = DefaultRouter()

router.register('movie' , MovieViewSet, basename='movie')
router.register('cast' , CastViewSet , basename='cast')
router.register('director' , DirectorViewSet , basename='director')

urlpatterns = router.urls

