from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmployeesView, EmployeeDetailsView
from .views import DepartmentsView, DepartmentDetailsView

urlpatterns = {
    url(r'^departments/?$', DepartmentsView.as_view(), name='departments'),
    url(
        r'^departments/(?P<pk>[0-9]+)/?$',
        DepartmentDetailsView.as_view(),
        name='department_details'
    ),
    url(r'^employees/?$', EmployeesView.as_view(), name='employees'),
    url(
        r'^employees/(?P<pk>[0-9]+)/?$',
        EmployeeDetailsView.as_view(),
        name='employee_details'
    )
}

urlpatterns = format_suffix_patterns(urlpatterns)
