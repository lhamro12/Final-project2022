from django.shortcuts import render
# Create your views here.
# Note: The stuff above this will already be in this file.
from django.http import HttpResponse

def index(request):
   right_answers= "0"
   if request.method == 'POST':
      endgame = request.POST.get('1_1')
      captain_america_civil_war = request.POST.get('2_3')
      spiderman_homecoming = request.POST.get('3_4')
      thor_the_dark_world = request.POST.get('4_2')
      guardians_of_the_galaxy_volume_2 = request.POST.get('5_2')
      shuri = request.POST.get('6_3')
      tchalla = request.POST.get('7_1')
      captain_america = request.POST.get('8_4')
      antman = request.POST.get('9_1')
      doctor_strange = request.POST.get('10_1')
      listOfAnswers= [endgame, captain_america_civil_war, spiderman_homecoming, thor_the_dark_world, guardians_of_the_galaxy_volume_2,
                      shuri, tchalla, captain_america, antman, doctor_strange]
      right_answers = "{}".format(len(list(filter(None,listOfAnswers))))
      return render(request, 'quizzes2.html', { 'right_answers': right_answers})
   else:
      right_answers="0"
      return render(request, 'quizzes2.html')
