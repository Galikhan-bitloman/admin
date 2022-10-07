from django.contrib import admin

from .models import Api_Users, Api_News, Api_Qaas, Api_Aboutus, Api_Analyses, Api_Appointments, Api_Results, \
                    Api_Reviews, Api_Contacts, Api_Notifications, Api_Promotions



@admin.register(Api_Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'lastname', 'firstname', 'email', 'phone_number')
    list_per_page = 20
    list_filter = ('username', 'lastname', 'firstname')

@admin.register(Api_News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'date')
    list_per_page = 20
    list_filter = ('title', 'date')

@admin.register(Api_Qaas)
class QaAsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_per_page = 20
    list_filter = ('question', 'answer')

@admin.register(Api_Aboutus)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    list_per_page = 20
    list_filter = ('title',)

@admin.register(Api_Analyses)
class AnalysesAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'research_id', 'biomaterial', 'research_time')
    list_per_page = 20
    list_filter = ('biomaterial',)

@admin.register(Api_Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('title_appointment', 'date', 'time', 'apiuser')

@admin.register(Api_Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('title_result', 'isready')
    list_per_page = 20
    list_filter = ('isready',)

@admin.register(Api_Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'date')
    list_per_page = 20
    list_filter = ('firstname', 'date')


@admin.register(Api_Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number', 'map')
    list_per_page = 10
    list_filter = ('address', 'phone_number')

@admin.register(Api_Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('title_notification', 'date', 'result', 'apiuser')
    list_per_page = 20
    list_filter = ('date', 'apiuser',)
@admin.register(Api_Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 20
    list_filter = ('title',)
