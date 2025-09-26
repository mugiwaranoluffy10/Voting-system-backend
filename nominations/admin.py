from django.contrib import admin
from .models import Category, Nomination, Payment, JuryReview

admin.site.register(Category)
admin.site.register(Nomination)
admin.site.register(Payment)
admin.site.register(JuryReview)
