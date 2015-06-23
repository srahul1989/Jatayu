from django.contrib import admin

# Register your models here.
from jatayuapp.models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "update"]
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)