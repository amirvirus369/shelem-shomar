from django.shortcuts import redirect, render
from .models import main,game
from django.utils import timezone
from .Calculations import  calcul_with,calcul_without
from shelem import forms
from django.contrib.auth import login,logout
from account.models import CustomUser
# Create your views here.
def shelem_main(request,id):
    main_game = main.objects.get(id=id)
    if main_game.finished:
      duration = main_game.finished - main_game.created
    else:
      duration = timezone.now() - main_game.created
    time = str(duration).split('.')[0]
    if request.method == 'POST':
        team = request.POST.get('team')
        score_buy = int(request.POST.get('bidValue')or 0)
        score_hand = int(request.POST.get('scoreValue'))
        def check1165():
            numm = max(main_game.team_ma, main_game.team_ona)
            if numm >= 1165:
                main_game.finished = timezone.now()
                main_game.status = True
                main_game.save()
                return True
            return False
        res = calcul_with(team,score_hand,score_buy)
        main_game.team_ma += res['ma']
        main_game.team_ona += res['ona']
        main_game.save()
        game.objects.create(main=main_game,
                            emtiaz_dast=res['emtiaz_dast'],
                            buyer=res['buyer'],
                            color=res['color'],
                            emtiaz_ma=res['emtiaz_ma'],
                            emtiaz_ona=res['emtiaz_ona'],
                            yasa=res['yasa'],
                            team_ma=main_game.team_ma,
                            team_ona=main_game.team_ona,
                            edit=res['edit'],
                            sh=res['sh'])
        if check1165():
            return redirect('shelem_main:win_shelem',main_game.id)
        return redirect('shelem_main:main_shelem_url',main_game.id)
        
    num = max(main_game.team_ma, main_game.team_ona) - min(main_game.team_ma, main_game.team_ona)
    return render(request,'index.html',{'main':main_game,'num':num,'time':time})



def shelem_joker(request,id):
    main_game = main.objects.get(id=id)
    if main_game.finished:
      duration = main_game.finished - main_game.created
    else:
      duration = timezone.now() - main_game.created
    time = str(duration).split('.')[0]
    if request.method == 'POST':
        team = request.POST.get('team')
        score_buy = int(request.POST.get('bidValue')or 0)
        score_hand = int(request.POST.get('scoreValue'))
        def check1165():
            numm = max(main_game.team_ma, main_game.team_ona)
            if numm >= 1400:
                main_game.finished = timezone.now()
                main_game.status = True
                main_game.save()
                return True
            return False
        res = calcul_without(team,score_hand,score_buy)
        main_game.team_ma += res['ma']
        main_game.team_ona += res['ona']
        main_game.save()
        game.objects.create(main=main_game,
                            emtiaz_dast=res['emtiaz_dast'],
                            buyer=res['buyer'],
                            color=res['color'],
                            emtiaz_ma=res['emtiaz_ma'],
                            emtiaz_ona=res['emtiaz_ona'],
                            yasa=res['yasa'],
                            team_ma=main_game.team_ma,
                            team_ona=main_game.team_ona,
                            edit=res['edit'],
                            sh=res['sh'])
        if check1165():
            return redirect('shelem_main:win_shelem',main_game.id)
        return redirect('shelem_main:shelem_joker',main_game.id)
        
    num = max(main_game.team_ma, main_game.team_ona) - min(main_game.team_ma, main_game.team_ona)
    return render(request,'index2.html',{'main':main_game,'num':num,'time':time})



def win_shelem(request,id):
    main_game = main.objects.get(id=id)
    timee = main_game.finished - main_game.created 
    time = str(timee).split('.')[0]
    num = max(main_game.team_ma, main_game.team_ona) - min(main_game.team_ma, main_game.team_ona)
    return render(request,'win.html',{'main':main_game,'num':num,'time':time})


def history(request):
    main_game = main.objects.filter(user=request.user).order_by('-created')
    return render(request,'history.html',{'main':main_game})


def delete_last_cart(request,id):
    main_game = main.objects.get(id=id)
    game_last = game.objects.filter(main=main_game).last()
    main_game.team_ma -= game_last.emtiaz_ma
    main_game.team_ona -= game_last.emtiaz_ona
    main_game.save()
    game_last.delete()
    return redirect('shelem_main:main_shelem_url',main_game.id)




def edit_game(request,id):
    main_game = main.objects.get(id=id)
    if request.method == 'POST':
        team_ma = int(request.POST.get('bidValue'))
        team_ona = int(request.POST.get('scoreValue'))
        def check1165():
            numm = max(main_game.team_ma, main_game.team_ona)
            if numm >= 1165:
                main_game.finished = timezone.now()
                main_game.status = True
                main_game.save()
                return True
            return False
        main_game.team_ma = team_ma
        main_game.team_ona = team_ona
        main_game.save()
        game.objects.create(main=main_game,buyer =4 ,emtiaz_dast=0,color=4,emtiaz_ma=team_ma,emtiaz_ona=team_ona,team_ma=main_game.team_ma,team_ona=main_game.team_ona,yasa=False,edit=True,sh=False)
        if check1165():
            return redirect('shelem_main:win_shelem',main_game.id)
        return redirect('shelem_main:main_shelem_url',main_game.id)
    

def edit_game_joker(request,id):
    main_game = main.objects.get(id=id)
    if request.method == 'POST':
        team_ma = int(request.POST.get('bidValue'))
        team_ona = int(request.POST.get('scoreValue'))
        def check1165():
            numm = max(main_game.team_ma, main_game.team_ona)
            if numm >= 1400:
                main_game.finished = timezone.now()
                main_game.status = True
                main_game.save()
                return True
            return False
        main_game.team_ma = team_ma
        main_game.team_ona = team_ona
        main_game.save()
        game.objects.create(main=main_game,buyer =4 ,emtiaz_dast=0,color=4,emtiaz_ma=team_ma,emtiaz_ona=team_ona,team_ma=main_game.team_ma,team_ona=main_game.team_ona,yasa=False,edit=True,sh=False)
        if check1165():
            return redirect('shelem_main:win_shelem',main_game.id)
        return redirect('shelem_main:shelem_joker',main_game.id)


def register(request):
    if request.user.is_authenticated:
        return redirect('shelem_main:type')
    form = forms.Register()
    if request.method == 'POST':
        form = forms.Register(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user,create = CustomUser.objects.get_or_create(phone_number=data['phone_number'],defaults={'full_name':data['full_name'],'avatar':data['avatar']})
            print(data['full_name'])
            login(request,user,backend='account.authentication.PhoneAuthBackend')
            return redirect('shelem_main:type')
        print(form.errors)
    return render(request,'reg.html',{'form':form})



def game_type(request):
    if request.method == 'POST':
        g = request.POST.get('game_mode')
        if g == 'without_joker':
            game_new = main.objects.create(user=request.user,joker=False)
            return redirect('shelem_main:main_shelem_url',game_new.id)
        elif g == 'with_joker':
            game_new = main.objects.create(user=request.user,joker=True)
            return redirect('shelem_main:shelem_joker',game_new.id)

    return render(request,'type.html')


def del_table(request,id):
    main_game = main.objects.get(id=id)
    main_game.delete()
    return redirect('shelem_main:history')