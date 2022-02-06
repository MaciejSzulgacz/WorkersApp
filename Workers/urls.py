from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.views.static import serve

from WorkersApp.views import HomeView, WorkerCreateView, WorkerDetailView, WorkerListView, WorkerUpdateView, \
    WorkerDeleteView, download_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('create/', WorkerCreateView.as_view(), name='worker-create'),
    path('list/', WorkerListView.as_view(), name='worker-list'),
    path('detail/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    path('update/<int:pk>/', WorkerUpdateView.as_view(), name='worker-update'),
    path('delete/<int:pk>/', WorkerDeleteView.as_view(), name='worker-delete'),
    path('workers-csv/', download_report, name='workers-csv')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
