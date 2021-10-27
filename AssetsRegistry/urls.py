from django.urls import path

from .views import dashboard_page, load_items_asset, update_data_view, delete_data_view, report_asset, summary_asset, \
    create_view_asset, load_table_items_asset, load_items_dept_asset

app_name = 'AssetsRegistry'
urlpatterns = [

    path('newAR/', create_view_asset, name='newAR'),
    path('reportAR/', report_asset, name='reportAR'),
    path('summaryAR/', summary_asset, name='summaryAR'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('ajax/load-items/', load_items_asset, name='ajax_load_items_asset'),
    path('ajax/load-items-dept/', load_items_dept_asset, name='ajax_load_items_dept_asset'),
    path('ajax/load-items-table/', load_table_items_asset, name='ajax_table_load_items_asset'),
    path('<int:pk>', delete_data_view, name='delete_item_url'),
    path('ajax/<int:pk>', update_data_view, name='update_item_url'),
]
