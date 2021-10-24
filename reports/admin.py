from django.contrib import admin

from .models import ReportDecision
from .models import ReportType
from .models import ReportSubType
from .models import PostReport

admin.site.register(ReportDecision)
admin.site.register(ReportType)
admin.site.register(ReportSubType)
admin.site.register(PostReport)

