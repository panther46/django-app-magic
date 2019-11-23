from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from magicdb.models import Card
from magicdb.forms import Card_action
from magicdb.forms import Check
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    page = request.GET['page']

    user = request.user

    dic={"1":{"page_start":0,"page_end":20},
        "2":{"page_start":20,"page_end":40},
        "3":{"page_start":40,"page_end":60},
        "4":{"page_start":80,"page_end":100},
        "5":{"page_start":120,"page_end":140},
        "6":{"page_start":140,"page_end":160},
        "7":{"page_start":160,"page_end":180},
        "8":{"page_start":180,"page_end":200},
        "9":{"page_start":200,"page_end":220},
        "10":{"page_start":220,"page_end":240},
        "11":{"page_start":240,"page_end":260},
        "12":{"page_start":260,"page_end":280},
        "13":{"page_start":280,"page_end":300},
        "14":{"page_start":300,"page_end":320}}

    cards_user = Card.objects.filter(owned_by=user.id)

    numbers = [element.number for element in cards_user]

    all_entries = Card.objects.all().order_by('number')[dic[page]["page_start"]:\
                 dic[page]["page_end"]]

    form = Check()

    return render(request, 'index.html', {"card" : all_entries, "user":user, "owned" : numbers, "form" : form, "page" : page})

@login_required
def single_card(request):

    form = Card_action()

    if request.method == "GET":

        card_number = request.GET['card_number']

        cards_user = Card.objects.filter(owned_by = request.user.id)

        numbers = [element.number for element in cards_user]

        card = Card.objects.get(number=card_number)

        return render(request, 'single_card.html',{"form":form, "card":card, "owned":numbers})

@login_required
def not_mine(request):

    not_mine = Card.objects.filter(owned_by = request.user.id)

    return render(request, 'index.html', {"card": not_mine})

@login_required
def mine(request):

    mine = Card.objects.filter(owned_by=request.user.id)

    return render(request, 'index.html', {"card": mine})

@login_required
def check(request):

    form = Check()

    list = []

    if request.method == "POST":

        form=Check(request.POST or None)

        if form.is_valid():

            list_numbers = form.cleaned_data['card_numbers'].split(",")

            numbers_ = [element.number for element in Card.objects.filter(owned_by=request.user.id)]

            for number in list_numbers:

                try:

                    list.append(Card.objects.get(number=number))

                except Card.DoesNotExist:

                    #logging de que la carta no se ha encontrado

                    pass
    
    return render(request, "check.html", {"query":list, "form":form,"owned":numbers_, "check":numbers})

@login_required
def i_got_it(request):

    if request.method=="POST":

        card_number = request.POST['card_number']

        card = Card.objects.get(number = card_number)

        users = [request.user]

        if request.POST.get("own"): card.owned_by.add(user) 

        elif request.POST.get("not_own"): card.owned_by.remove(user)

        card.save()

        return HttpResponseRedirect("/index/card"+ "?card_number=%s" % card_number)

@login_required
def bulk_insert_or_remove(request):

    list=[]

    saved = False

    if request.method == "POST":

        list_numbers = request.POST['cards_owned'].split(",")

        user = request.user

        for number in list_numbers:

            try:

                card = Card.objects.get(number=number)

            except Card.DoesNotExist:

                #Se realiza logging del error

                continue

            if request.POST.get("own"): card.owned_by.add(user)

            if request.POST.get("not_own"): card.owned_by.remove(user)

            list.append(card)
         
    return redirect("/index?page=1")
