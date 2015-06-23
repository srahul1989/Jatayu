from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def home(request):
    title = "My Title %s" % (request.user)
    if request.method == "POST":
        print request.POST
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print instance.email
        print instance.timestamp
    context = {
        "template_title": title,
        "form": form
    }
    return render(request, "basic.html", context)

def homepage(request):
    return render(request, "homepage.html", {})

