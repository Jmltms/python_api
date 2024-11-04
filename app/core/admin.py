"""
Django admin customization.
"""
import csv
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.models import LogEntry
from django.http import HttpResponse
from core import models


class ExportCsvMixin:

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Dispostion'
        ] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow(
                [getattr(obj, field) for field in field_names]
            )
            print(row)

        return response

    export_as_csv.short_description = "Export Selected"


class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    ]

    readonly_fields = (
        'content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )
    search_fields = [
        'object_id',
        'object_repr',
        'change_message'
    ]

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


class UserAdmin(BaseUserAdmin):

    ordering = ['id']
    list_display = ['first_name', 'last_name', 'email', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal Info'), {
            'fields': (
                'first_name',
                'middle_name',
                'last_name',
            )}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Important dates'), {'fields': ('last_login',)},
        ),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'first_name',
                'first_name',
                'last_name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'employee_id',
        'email',
        'status',
        'type'
    ]

    raw_id_fields = ['user']

    search_fields = [
        'user__first_name',
        'user__last_name',
    ]

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email


class IndustryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'field'
    ]
    search_fields = [
        'name',
    ]


class UserInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'address'
    ]
    search_fields = [
        'first_name',
        'last_name',
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_code',
        'name',
        'stock_on_hand',
        'price',
        'description'
    ]
    search_fields = [
        'prouct_code',
        'name',
    ]


class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product',
        'user',
        'quantity',
        'total'
    ]
    search_fields = [
        'prouct__name',
    ]


class UserStockAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'stock_holder',
        'invested',
        'stock_value'
    ]


admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
admin.site.register(models.UserStock, UserStockAdmin)
