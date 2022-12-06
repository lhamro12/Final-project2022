from django.shortcuts import render
# Create your views here.
# Note: The stuff above this will already be in this file.
from django.http import HttpResponse

def index(request): 
   if request.method == 'POST': 
      iron_man = request.POST.get('1_1') 
      cap_america = request.POST.get('2_3') 
      scarlett_witch = request.POST.get('3_3')
      sokovia = request.POST.get('4_4')
      florence_pugh = request.POST.get('5_3')
      spiderman_far_from_home = request.POST.get('6_4')
      avengers_assemble = request.POST.get('7_3')
      cheeseburger = request.POST.get('8_3')
      agatha_harkness = request.POST.get('9_4')
      all_of_the_above = request.POST.get('10_4')
      listOfAnswers = [iron_man, cap_america, scarlett_witch, sokovia, florence_pugh, spiderman_far_from_home, avengers_assemble, cheeseburger, agatha_harkness, all_of_the_above]
      right_answers = "{}".format(len(list(filter(None,listOfAnswers))))
      return render(request, 'quizzes.html', { 'right_answers': right_answers}) 
   else:
      right_answers="0"
      return render(request, 'quizzes.html')
