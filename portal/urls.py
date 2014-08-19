from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

from two_factor.views import (LoginView,
                              PhoneDeleteView, PhoneSetupView, DisableView,
                              BackupTokensView, SetupCompleteView, SetupView,
                              ProfileView, QRGeneratorView)

from portal.permissions import teacher_verified

js_info_dict = {
    'packages': ('conf.locale',),
}

two_factor_patterns = [
    url(r'^account/login/$', 'portal.views.custom_2FA_login', name='login'),
    url(r'^account/two_factor/setup/$', SetupView.as_view(), name='setup'),
    url(r'^account/two_factor/qrcode$', QRGeneratorView.as_view(), name='qr'),
    url(r'^account/two_factor/setup/complete/$', SetupCompleteView.as_view(), name='setup_complete'),
    url(r'^account/two_factor/backup/tokens/$', teacher_verified(BackupTokensView.as_view()), name='backup_tokens'),
    url(r'^account/two_factor/$', teacher_verified(ProfileView.as_view()), name='profile'),
    url(r'^account/two_factor/disable/$', teacher_verified(DisableView.as_view()), name='disable'),
]

urlpatterns = patterns('',

    url(r'^teach/$', 'portal.views.teach'),
    url(r'^play/$', 'portal.views.play'),
    url(r'^about/$', TemplateView.as_view(template_name='portal/about.html'), name='about'),
    url(r'^help/$', TemplateView.as_view(template_name='portal/help-and-support.html'), name='help'),
    url(r'^contact/$', 'portal.views.contact', name='contact'),
    url(r'^terms/$', TemplateView.as_view(template_name='portal/terms.html'), name='terms'),
    url(r'^map/$', 'portal.views.schools_map'),
    url(r'^locked_out/$', TemplateView.as_view(template_name='portal/locked_out.html'), name='locked_out'),

    url(r'^$', TemplateView.as_view(template_name='portal/home.html'), name='home'),
    url(r'^logout/$', 'portal.views.logout_view'),
    url(r'^teach/school/fuzzy_lookup$', 'portal.views.organisation_fuzzy_lookup'),
    url(r'^teach/school/manage/$', 'portal.views.organisation_manage'),
    url(r'^teach/school/leave/$', 'portal.views.organisation_leave'),
    url(r'^teach/school/kick/(?P<pk>[0-9]+)/$', 'portal.views.organisation_kick'),
    url(r'^teach/school/toggle_admin/(?P<pk>[0-9]+)/$', 'portal.views.organisation_toggle_admin'),
    url(r'^teach/school/allow_join/(?P<pk>[0-9]+)/$', 'portal.views.organisation_allow_join'),
    url(r'^teach/school/deny_join/(?P<pk>[0-9]+)/$', 'portal.views.organisation_deny_join'),
    url(r'^teach/home/$', 'portal.views.teacher_home'),
    url(r'^teach/lesson_plans/$', 'portal.views.teacher_lesson_plans'),
    url(r'^teach/account/$', 'portal.views.teacher_edit_account'),
    url(r'^teach/account/disable_2FA/(?P<pk>[0-9]+)/$', 'portal.views.teacher_disable_2FA'),
    url(r'^teach/classes/$', 'portal.views.teacher_classes'),
    url(r'^teach/class/(?P<access_code>[A-Z0-9]+)/$', 'portal.views.teacher_class'),
    url(r'^teach/class/move/(?P<access_code>[A-Z0-9]+)/$', 'portal.views.teacher_move_class'),
    url(r'^teach/class/edit/(?P<access_code>[A-Z0-9]+)/$', 'portal.views.teacher_edit_class'),
    url(r'^teach/class/delete/(?P<access_code>[A-Z0-9]+)/$', 'portal.views.teacher_delete_class'),
    url(r'^teach/class/student/reset/(?P<pk>[0-9]+)/$', 'portal.views.teacher_student_reset'),
    url(r'^teach/class/student/edit/(?P<pk>[0-9]+)/$', 'portal.views.teacher_edit_student'),
    url(r'^teach/class/(?P<access_code>[A-Z0-9]+)/print_reminder_cards/$', 'portal.views.teacher_print_reminder_cards'),
    url(r'^teach/class/(?P<access_code>[A-Z0-9]+)/students/move/$', 'portal.views.teacher_move_students'),
    url(r'^teach/class/(?P<access_code>[A-Z0-9]+)/students/move/disambiguate/$', 'portal.views.teacher_move_students_to_class'),
    url(r'^teach/class/(?P<access_code>[A-Z0-9]+)/students/delete/$', 'portal.views.teacher_delete_students'),
    url(r'^teach/class/(?P<access_code>[A-Z0-9]+)/students/dismiss/$', 'portal.views.teacher_dismiss_students'),
    url(r'^teach/student/accept/(?P<pk>[0-9]+)/$','portal.views.teacher_accept_student_request'),
    url(r'^teach/student/reject/(?P<pk>[0-9]+)/$','portal.views.teacher_reject_student_request'),
    url(r'^play/details/$', 'portal.views.student_details'),
    url(r'^play/account/$', 'portal.views.student_edit_account'),
    url(r'^play/join/$', 'portal.views.student_join_organisation'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^user/$', 'portal.views.current_user'),
    url(r'^user/verify_email/(?P<token>[0-9a-f]+)/$', 'portal.views.verify_email'),


    url(r'^user/password/reset/student/$',
        'portal.views.student_password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="student_password_reset"),
    url(r'^user/password/reset/teacher/$',
        'portal.views.teacher_password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="teacher_password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'portal.views.password_reset_check_and_confirm',
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),


    url(r'^', include(two_factor_patterns, 'two_factor')),
)
