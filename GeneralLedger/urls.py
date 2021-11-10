from django.urls import path

from .views import report_gl, summary_gl, dashboard_page, create_view_gl, load_items, \
    delete_data_view, \
    update_data_view, export_excel_view, export_pdf_view, export_csv_view, create_view_dept_gl, load_dept_items, \
    load_items_station, load_summary_items

app_name = 'GeneralLedger'
urlpatterns = [

    path('newGL/', create_view_gl, name='newGL'),
    path('newDeptGL/', create_view_dept_gl, name='newDeptGL'),
    path('reportGL/', report_gl, name='reportGL'),
    path('excelL/', export_excel_view, name='export_excel_url'),
    path('csv/', export_csv_view, name='export_csv_url'),
    path('pdf/', export_pdf_view, name='export_pdf_url'),
    path('summaryGL/', summary_gl, name='summaryGL'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('ajax/load-items/', load_items, name='ajax_load_items'),
    path('ajax/load-items-summary/<int:pk>', load_summary_items, name='summary_item_url'),
    path('ajax/load-items-dept/', load_dept_items, name='ajax_load_dept_items'),
    path('ajax/load-items-station/', load_items_station, name='ajax_load_items_sta_url'),
    path('<int:pk>', delete_data_view, name='delete_item_url'),
    path('ajax/<int:pk>', update_data_view, name='update_item_url'),
    # path('dashboard/', add_new_GL, name='dashboard'),
]
