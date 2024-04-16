import xlwt
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
# from .models import Survey, Question, Choice, AnswerOption, UserResponse
from .models import UserResponse
from .views import dashboard
from django.urls import path
from django.contrib.auth.models import User

# Register your models here
# admin.site.register(Survey)
# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(AnswerOption)
admin.site.register(UserResponse)

class UserResponseAdmin(admin.ModelAdmin):
    list_per_page = 15  # This sets the number of records per page to 15
    
    list_display = (
        'id', 'first_name', 'last_name', 'date', 'staff_name', 'sex',
        'doh_employee', 'team_acronym', 'bureau_service_region_acronym',
        'activity_name', 'expectation', 'statement1_rating', 'statement2_rating',
        'statement3_rating', 'statement4_rating', 'statement5_rating',
        'statement6_rating', 'quality', 'comments', 'view_link'
    )
    list_filter = ('date', 'team_acronym', 'bureau_service_region_acronym')
    search_fields = ('first_name', 'last_name', 'staff_name')

    def view_link(self, obj):
        url = reverse('admin:survey_userresponse_change', args=[obj.id])
        return format_html(f'<a href="{url}">View</a>')

    view_link.short_description = 'View Link'

    actions = ['export_to_excel']

    def export_to_excel(self, request, queryset):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=user_responses.xls'

        # Create Excel file
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('User Responses')

        # Write headers
        row_num = 0
        columns = [
            'ID', 'First Name', 'Last Name', 'Date', 'Staff Name', 'Sex',
            'DOH Employee', 'Team Acronym', 'Bureau/Region Acronym', 
            'Activity Name', 'Expectation', 'Statement1 Rating', 
            'Statement2 Rating', 'Statement3 Rating', 'Statement4 Rating',
            'Statement5 Rating', 'Statement6 Rating', 'Quality', 'Comments'
        ]

        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Write data
        for obj in queryset:
            row_num += 1
            row = [
                obj.id, obj.first_name, obj.last_name, obj.date, obj.staff_name,
                obj.sex, obj.doh_employee, obj.team_acronym, 
                obj.bureau_service_region_acronym, obj.activity_name, 
                obj.expectation, obj.statement1_rating, obj.statement2_rating,
                obj.statement3_rating, obj.statement4_rating, 
                obj.statement5_rating, obj.statement6_rating, obj.quality, 
                obj.comments
            ]
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

    export_to_excel.short_description = _('Export selected records to Excel')


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(dashboard), name='dashboard'),
        ]
        return custom_urls + urls

custom_admin_site = CustomAdminSite(name='custom_admin')

custom_admin_site.register(UserResponse, UserResponseAdmin)

custom_admin_site.register(User)



