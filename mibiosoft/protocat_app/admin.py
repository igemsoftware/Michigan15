from django.contrib import admin
from .models import Protocol



class ProtocolAdmin(admin.ModelAdmin):
    class Meta:
        model = Protocol


admin.site.register(Protocol, ProtocolAdmin)