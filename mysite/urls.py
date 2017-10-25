from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),

]


#import debug_toolbar
#urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
