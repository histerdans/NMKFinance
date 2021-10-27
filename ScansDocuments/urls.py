from django.urls import path

from .views import dashboard_page, load_items_doc, update_data_view_doc, delete_data_view_doc, report_doc, \
    create_view_doc, pdf_viewer

app_name = 'Document'
urlpatterns = [

    path('document/', create_view_doc, name='uploaded_file_url'),
    path('reportDoc/', report_doc, name='report_doc_url'),
    path('detail/<int:pk>', pdf_viewer, name='pdf_viewer_page'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('ajax/load-items_doc/', load_items_doc, name='ajax_load_items_doc'),
    path('<int:pk>', delete_data_view_doc, name='delete_item_url'),
    path('ajax/<int:pk>', update_data_view_doc, name='update_item_url'),
]
