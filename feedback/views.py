from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.db.models import Avg, Count

def submit_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "feedback/thank_you.html")
    else:
        form = FeedbackForm()
    return render(request, "feedback/feedback_form.html", {'form': form})

def admin_dashboard(request):
    feedbacks = Feedback.objects.all().order_by('-submitted_at')
    avg_rating = Feedback.objects.aggregate(Avg('rating'))['rating__avg'] or 0
    total_feedback = feedbacks.count()
    rating_distribution = Feedback.objects.values('rating').annotate(count=Count('rating')).order_by('-rating')

    return render(request, "feedback/admin_dashboard.html", {
        'feedbacks': feedbacks,
        'avg_rating': round(avg_rating, 2),
        'total_feedback': total_feedback,
        'rating_distribution': rating_distribution,
    })