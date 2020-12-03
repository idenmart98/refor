from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LinkForm
from .models import Links

# Create your views here.


def test_view(request):
    if request.method == 'POST':
        if not Links.objects.filter(old_link=request.POST['link']):
            Links.objects.create(
                old_link=request.POST['link'])
    form = LinkForm()
    links = Links.objects.all().order_by("-id")
    return render(request, "my_app/test.html", context={"form":form, "links":links })

def redirect_view(request, new_link):
    link = Links.objects.filter(new_linl=new_link).last()
    return HttpResponseRedirect(link.old_link)

