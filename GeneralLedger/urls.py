from django.urls import path

from .views import new_GL, report_GL, summary_GL, dashboard_page, add_new_GL

app_name = 'GeneralLedger'
urlpatterns = [

    path('newGL/', add_new_GL, name='newGL'),
    path('reportGL/', report_GL, name='reportGL'),
    path('summaryGL/', summary_GL, name='summaryGL'),
    path('dashboard/', dashboard_page, name='dashboard'),
    # path('dashboard/', add_new_GL, name='dashboard'),
]
