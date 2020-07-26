from django.shortcuts import render, redirect, HttpResponse
from time import strftime, gmtime
import random

def starting(request):
  request.session.flush()
  return render(request, "starting.html")

def index(request):
  if 'game' in request.POST:
    request.session['game'] = request.POST['game']
  if 'score' not in request.session:
    request.session['score'] = 0
  if 'messages' not in request.session:
    request.session['messages'] = []
  if 'name' not in request.session:
    request.session['name'] = 'Soey'
  if 'movecount' not in request.session:
    request.session['movecount'] = 0
  context = {
    'messages': request.session['messages'],
    'time': strftime("%m-%d-%Y %H:%M %p", gmtime()),
  }
  return render(request, "index.html", context)

def game_type(request):
  if request.session['game'] == "movegame":
    if request.session['movecount'] == 20:
      if request.session['score'] >= 275:
        request.session['message'].append("Winner Winner Chicken Dinner!")
      else:
        request.session['messages'].append('You suck LOL')
      request.session.save()
  if request.session['game'] == "goldgame":
    if request.session['score'] >= 1000000:
        request.session['messages'].append("winner Winner Chicken Dinner")
        request.session.save()
  return redirect('/')


def process_money(request):
  time = strftime("%m-%d-%Y %H:%M %p", gmtime())
  print("GOT POST INFO!")
  request.session['movecount'] += 1
  if request.method == "POST" or "GET":
    if 'farm' in request.POST:
      score = random.randint(10, 20)
      message = "Earned " + str(score) + " gold(s) from the farm! " + time
      print (f"Earned {score} from the farm!")
    elif 'cave' in request.POST:
      score = random.randint(5, 10)
      message = "Earned " + str(score) + " gold(s) from the cave! " + time
      print (f"Earned {score} from the cave!")
    elif 'house' in request.POST:
      score = random.randint(2, 5)
      message = "Earned " + str(score) + " gold(s) from the house! " + time
      print (f"Earned {score} from the house!")
    elif 'casino' in request.POST:
      score = random.randint(-50, 50)
      if score > 0:
          print (f"Earned {score} from the casino!")
          message = "Earned " + str(score) + \
              " gold(s) from a casino! " + time
      else:
          message = "Entered a casino and lost " + \
              str(score) + " gold(s)... Ouch... " + time
          print (f"Lost {score} from the casino ouchhh!")
    request.session['score'] += score
    print(request.session['score'])
  if request.session['score'] < 0:
    message = "HAHA.. start over!!"
  request.session['messages'].append(message)
  # print(request.session['messages'], sep="\n")
  request.session.save()
  # game_type(request)
  return redirect('/')


def reset(request):
  request.session.flush()
  return redirect("/")
