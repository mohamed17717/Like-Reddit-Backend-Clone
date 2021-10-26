from django.contrib import admin

from reports.models import (
  ReportDecision,
  ReportType,
  ReportSubType,
  PostReport,
)

admin.site.register(ReportDecision)
admin.site.register(ReportType)
admin.site.register(ReportSubType)
admin.site.register(PostReport)

