from django.contrib import admin


from accounts.models import Sponsee, School, Reason, Sponser

admin.site.register(Sponsee)
admin.site.register(School)
admin.site.register(Reason)
admin.site.register(Sponser)
