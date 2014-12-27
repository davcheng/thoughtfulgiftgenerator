from django.shortcuts import render, get_object_or_404
from blog.models import GiftIdea, GifteeDataForm
from django.http import HttpResponseRedirect
from django.db.models import Q

def index(request):
	return render(request, 'blog/index.html')

# 	return render(request, 'blog/results.html')
def submit(request):
	return render(request, 'blog/index.html')

def results(request):
    if request.GET: # If the form has been submitted...
    	gifteeDataForm = GifteeDataForm
        gifteeDataForm.gender = request.GET.get('gender')
    	gifteeDataForm.age = request.GET.get('age')
        gifteeDataForm.price = request.GET.get('price')
    	gifteeDataForm.tech_flag = request.GET.get('tech_flag')
    	gifteeDataForm.fitness_flag = request.GET.get('fitness_flag')
    	gifteeDataForm.travel_flag = request.GET.get('travel_flag')
    	gifteeDataForm.fashion_flag = request.GET.get('fashion_flag')
    	gifteeDataForm.music_flag = request.GET.get('music_flag')
        gifteeDataForm.home_flag = request.GET.get('home_flag')
        # if gender was answerd:
        if request.GET.get('gender'):
            if request.GET.get('age'):
                if request.GET.get('price'):
                    gift_idea_result = GiftIdea.objects.filter(
                        Q(tech_flag=gifteeDataForm.tech_flag) | 
                        Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                        Q(travel_flag=gifteeDataForm.travel_flag) | 
                        Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                        Q(music_flag=gifteeDataForm.music_flag) |
                        Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_gender=gifteeDataForm.gender, target_age=gifteeDataForm.age, price=gifteeDataForm.price).order_by('-upvote')
                else:
                    gift_idea_result = GiftIdea.objects.filter(
                        Q(tech_flag=gifteeDataForm.tech_flag) | 
                        Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                        Q(travel_flag=gifteeDataForm.travel_flag) | 
                        Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                        Q(music_flag=gifteeDataForm.music_flag) |
                        Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_gender=gifteeDataForm.gender, target_age=gifteeDataForm.age).order_by('-upvote')
            else:
                gift_idea_result = GiftIdea.objects.filter(
                    Q(tech_flag=gifteeDataForm.tech_flag) | 
                    Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                    Q(travel_flag=gifteeDataForm.travel_flag) | 
                    Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                    Q(music_flag=gifteeDataForm.music_flag) |
                    Q(home_flag=gifteeDataForm.home_flag)).filter(published=True, target_gender=gifteeDataForm.gender).order_by('-upvote')
        else:
            gift_idea_result = GiftIdea.objects.filter(
                Q(tech_flag=gifteeDataForm.tech_flag) | 
                Q(fitness_flag=gifteeDataForm.fitness_flag) | 
                Q(travel_flag=gifteeDataForm.travel_flag) | 
                Q(fashion_flag=gifteeDataForm.fashion_flag) | 
                Q(music_flag=gifteeDataForm.music_flag) |
                Q(home_flag=gifteeDataForm.home_flag)).filter(published=True).order_by('-upvote')
        
        # TODO: add age, price, and categories
        gift_idea_secondary_results = gift_idea_result[1:4]
        gift_idea_result = gift_idea_result[:1]
        # gift_idea_result = GiftIdea.objects.filter(Q(tags__icontains = search_term) | Q(description__icontains= search_term)).order_by('-likes')[:5]
        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results, 'gifteeDataForm': gifteeDataForm}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')

def random(request):
    if request.GET: # TODO: eliminate duplicates
        gift_idea_results = GiftIdea.objects.filter(published=True).order_by('?')
        gift_idea_secondary_results = gift_idea_results[1:4]
        gift_idea_result = gift_idea_results[:1]

        # generate random with more scalable method since order_by('?')[:X] does not scale well?
        # last = GiftIdea.objects.count() - 1
        # index1 = randint(0, last)
        # index2 = randint(0, last - 1)
        # if index2 == index1: index2 = last
        # MyObj1 = MyModel.objects.all()[index1]
        # MyObj2 = MyModel.objects.all()[index2]

        # gift_idea_result = GiftIdea.objects.filter(Q(tags__icontains = search_term) | Q(description__icontains= search_term)).order_by('-likes')[:5]
        return render(request, 'blog/results.html', { 'gift_idea_result': gift_idea_result, 'gift_idea_secondary_results': gift_idea_secondary_results}) # Redirect after POST    # if request.POST: # If the form has been submitted...
    return render(request, 'blog/index.html')