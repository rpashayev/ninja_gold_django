from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# Create your views here.
def start_page(request):
    return render(request,'start.html')

def start(request):
    request.session['gold_target'] = int(request.POST['gold_target'])
    request.session['move_target'] = int(request.POST['move_target'])
    return redirect('/game')

def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['ninja_movements'] = 0
        request.session['left_movements'] = request.session['move_target']
        request.session['log'] = f'Welcome to the Game! {datetime.now().strftime("%b %d, %Y %I:%M %p")}'
    return render(request, 'index.html')

def process_money(request):
    if request.session['ninja_movements'] < request.session['move_target'] and request.session['total_gold'] < request.session['gold_target']:
        activity = randomize(request)
        request.session['total_gold'] += activity['value']
        request.session['ninja_movements'] += 1
        request.session['left_movements'] -= 1
        request.session['log'] = activity['log'] + request.session['log']
        request.session['color'] = activity['color']
    
    return redirect('/game')

def randomize(request):
    gain = 'earned'
    color = 'text-success'
    min = -50
    max = 50
    if request.POST['property'] == 'farm':
        min = 10
        max = 20
    elif request.POST['property'] == 'cave':
        min = 5
        max = 10
    elif request.POST['property'] == 'house':
        min = 2
        max = 5
        
    value = randint(min, max)
    if value < 0:
        gain = 'lost'
        color = 'text-danger'
    log_text = f'<p class="mb-0 {color}">Dojo entered {request.POST["property"].title()} and {gain} {value} golds @ {datetime.now().strftime("%b %d, %Y %I:%M %p")} </p>'
    activity = {
        'value': value,
        'log': log_text,
        'color': color
    }
    return activity

def clear(request):
    request.session.clear()
    return redirect('/')