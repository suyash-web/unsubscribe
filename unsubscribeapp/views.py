from django.shortcuts import render
from unsubscribeapp.models import Unsubscribe
from datetime import datetime
from django.contrib import messages

# Create your views here.
def unsubscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        un_sub = Unsubscribe(email=email, desc=desc, date=datetime.today())
        un_sub.save()
        messages.success(request, "You have been unsubscribed!")
    return render(request, "index.html")