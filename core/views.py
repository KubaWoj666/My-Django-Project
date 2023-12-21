from django.shortcuts import render



def home_view(request):


    context={
        "message": "opa"
    }
    return render(request,  "core/home.html", context )
