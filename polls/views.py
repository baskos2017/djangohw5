from django.shortcuts import get_object_or_404, render
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
from django.shortcuts import render, redirect
from .forms import ReviewForm

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_success')  
    else:
        form = ReviewForm()
    return render(request, 'polls/submit_review.html', {'form': form})

def review_success(request):
    return render(request, 'polls/review_success.html')
