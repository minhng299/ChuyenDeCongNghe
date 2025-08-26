from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.views.generic import TemplateView
from django.views import View
import asyncio
# Create your views here.

def special_case_2003(request):
    # Handle the special case for the year 2003
    return HttpResponse("Special case for the year 2003")


def year_archive(request, year):
    # Handle the year archive view
    return HttpResponse(f"Year archive view for {year}")

def month_archive(request, year, month):
    # Handle the month archive view
    return HttpResponse(f"Month archive view for {year}-{month}")

def article_detail(request, year, month, slug):
    # Handle the article detail view
    return HttpResponse(f"Article detail view for {year}-{month} with slug: {slug}")


async def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

def my_view(request):
    # ...
    def foo():
        return False
    if foo():
        return HttpResponse(status=404)
    else:
        return HttpResponse(status=201)
    
    
class AboutView(TemplateView):
    template_name = "viewlayer/about.html"

class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")