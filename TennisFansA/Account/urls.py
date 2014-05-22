from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
	url(r'^Register/$', 'Account.views.Register'),
	url(r'^Register_Success/$', 'Account.views.Register_Success'),
	url(r'^Login/$', 'Account.views.Login'),
	url(r'^Login_Success/$', 'Account.views.Login_Success'),
	url(r'^auth/$', 'Account.views.auth_view'),
	url(r'^Login_Failure/$', 'Account.views.Login_Failure'),

)
