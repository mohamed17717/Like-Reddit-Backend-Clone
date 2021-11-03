from django.urls import path

from rest_framework import routers


from reports.views import (
  ReportType_ApiView,
  ReportSubType_ApiView,

  PostReport_UserReport_Apiview,

  PostReport_ListReports_ApiView,
  ReportDecision_ListDecision_ApiView,

  PostReport_UpdateDecision_Apiview,
)

app_name = 'reports'
router = routers.SimpleRouter()

router.register(r'report-types', ReportType_ApiView)
router.register(r'sub-report-types', ReportSubType_ApiView)


urlpatterns = [
  path('p/<int:post_id>/report/', PostReport_UserReport_Apiview.as_view(), name='post-report'),
  path('r/list/', PostReport_ListReports_ApiView.as_view(), name='list-reports'),
  path('r/decision/list/', ReportDecision_ListDecision_ApiView.as_view(), name='list-report-decisions'),

  path('r/<int:pk>/update-decision/', PostReport_UpdateDecision_Apiview.as_view(), name='update-report-decision'),

] + router.urls



