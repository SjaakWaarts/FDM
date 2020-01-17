"""
Definition of urls for FDM.
"""

from datetime import datetime
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app.forms import BootstrapAuthenticationForm
import app.views
import app.api
import app.basket_ds

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.contrib import auth

urlpatterns = [
    # Examples:
    path('', app.views.home, name='home'),

    path('retrieve', app.views.retrieve_view, name='retrieve'),
    path('learn', app.views.learn_view, name='learn'),
    path('predict', app.views.predict_view, name='predict'),

    path('generate', app.views.generate_view, name='generate'),
    re_path(r'^experiment/(?P<experiment_id>[A-Z0-9]+)$', app.views.generate_experiment_view, name='experiment'),

    path('basket', app.views.basket_view, name='basket'),
    path('api/basket_pollresults', app.basket_ds.basket_pollresults_api, name='api/basket_pollresults'),
    re_path(r'^basket_experiment/(?P<basket_id>[A-Z0-9]+)$', app.views.basket_experiment_view, name='basket_experiment'),
    re_path(r'^api/basket_experiment_api/(?P<basket_id>[A-Z0-9]+)$', app.basket_ds.basket_experiment_api, name='api/basket_experiment_api'),

    path('explore', app.views.explore_view, name='explore'),
    path('explore/explore_compfreq', app.views.explore_compfreq_view, name='explore/explore_compfreq'),
    path('explore/explore_e2esubm', app.views.explore_e2esubm_view, name='explore/explore_e2esubm'),
    path('explore/orderbook', app.views.explore_orderbook_view, name='explore/orderbook'),

    path('genesis', app.views.genesis_view, name='genesis'),

    path('api/e2equery_compfreq', app.api.e2equery_compfreq_api, name='api/e2equery_compfreq'),
    path('api/e2equery_e2esubm', app.api.e2equery_e2esubm_api, name='api/e2equery_e2esubm'),
    path('api/e2equery_orderbook', app.api.e2equery_orderbook_api, name='api/e2equery_orderbook'),

    path('contact', app.views.contact, name='contact'),
    path('about', app.views.about, name='about'),

    # Registration URLs
    path('accounts/register/', app.views.register, name='register'),
    path('accounts/register_complete/', app.views.registrer_complete, name='register_complete'),
    #path('login/', auth_views.login, name='login'),
    #path('logout/', auth_views.logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # path('admin/', include(admin.site.urls)),
    ]
