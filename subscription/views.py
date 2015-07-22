from django.shortcuts import render
from subscription.forms import SubscriptionForm


def home(request):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.send()
        return render(request, 'feedback.html')
    else:
        form = SubscriptionForm()
        context = {
            'form': form
        }
        return render(request, 'form.html', context)