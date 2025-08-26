from django.shortcuts import render
from django.http import HttpResponse
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