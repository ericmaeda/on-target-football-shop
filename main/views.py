from django.shortcuts import render

# Create your views here.
def show_main(request) :
    delivery = {
        "appname":"On Target",
        "name":"Erico Putra Bani Mahendra",
        "class":"PBP E",
    }
    return render(request, "main.html", delivery)
