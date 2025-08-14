from django.contrib import admin
from django.db.models import Avg
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'rating', 'submitted_at')
    list_filter = ('rating', 'submitted_at')
    search_fields = ('name', 'email', 'comments')

    def changelist_view(self, request, extra_context=None):
        # Add average rating to context
        avg_rating = Feedback.objects.aggregate(avg=Avg('rating'))['avg']
        extra_context = extra_context or {}
        extra_context['avg_rating'] = round(avg_rating or 0, 2)
        return super().changelist_view(request, extra_context=extra_context)
