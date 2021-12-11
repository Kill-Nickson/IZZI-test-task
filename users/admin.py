import uuid
from io import BytesIO, StringIO
from datetime import datetime
import csv

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.conf.urls import url

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'first_name', 'last_name', 'birth_date', 'date_joined')

    fieldsets = (
        ('Main', {
            'fields': (
                'first_name',
                'last_name',
                'birth_date',
                'date_joined',
                'order')
        }),
    )

    change_list_template = "admin/users_change_list.html"

    def get_urls(self):
        urls = super(CustomUserAdmin, self).get_urls()
        custom_urls = [
            url('import/', self.process_import, name='process_import'),
        ]
        return custom_urls + urls

    def process_import(self, request):
        if request.FILES.get('myfile'):
            my_file = request.FILES['myfile']
            filename = BytesIO(my_file.read())
            data = filename.read().decode('utf-8')
            rows = data.split('\n')[1:]
            for r in rows:
                if r == '':
                    break
                user_fields = r.split(',')
                new_user = CustomUser()
                new_user.first_name = user_fields[0]
                new_user.last_name = user_fields[1]
                new_user.birth_date = datetime.strptime(user_fields[2], '%Y/%m/%d')
                new_user.date_joined = datetime.strptime(user_fields[3], '%Y/%m/%d')
                new_user.username = uuid.uuid4()
                new_user.save()
        return HttpResponseRedirect("../")
