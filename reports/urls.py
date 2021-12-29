from django.urls import path

from rest_framework import routers

from reports.views.user_views import (
  PostReport_UserReport_Apiview,
  ReportType_UserList_ApiView,
  ReportSubType_UserList_ApiView,

  ReportSubType_UserListOnType_ApiView
)
from reports.views.admin_views import (
  ReportType_ApiView,
  ReportSubType_ApiView,
  PostReport_ListReports_ApiView,
  ReportDecision_ListDecision_ApiView,
  PostReport_UpdateDecision_Apiview,
)


app_name = 'reports'
router = routers.SimpleRouter()

router.register(r'admin/report/type', ReportType_ApiView, basename='admin-report-type')
router.register(r'admin/report/sub-type', ReportSubType_ApiView)


urlpatterns = [
  path('report/type/list/', ReportType_UserList_ApiView.as_view(), name='list-reports-type'),
  path('report/sub-type/list/', ReportSubType_UserList_ApiView.as_view(), name='list-reports-sub-types'),
  path('report/<int:type_id>/sub-type/list/', ReportSubType_UserListOnType_ApiView.as_view(), name='list-reports-sub-types-by-category'),

  path('post/<int:post_id>/report/<int:type_id>/', PostReport_UserReport_Apiview.as_view(), name='post-report'),

  path('admin/report/list/', PostReport_ListReports_ApiView.as_view(), name='list-reports'),
  path('admin/report/decision/list/', ReportDecision_ListDecision_ApiView.as_view(), name='list-report-decisions'),
  path('admin/report/<int:report_id>/decision/warn/', PostReport_UpdateDecision_Apiview.as_view(), name='update-report-decision-warn'),
  path('admin/report/<int:report_id>/decision/dangerous/', PostReport_UpdateDecision_Apiview.as_view(), name='update-report-decision-dangerous'),
  path('admin/report/<int:report_id>/decision/safe/', PostReport_UpdateDecision_Apiview.as_view(), name='update-report-decision-safe'),
  path('admin/report/<int:report_id>/decision/pending/', PostReport_UpdateDecision_Apiview.as_view(), name='update-report-decision-pending'),

] + router.urls



