from django.shortcuts import redirect

def calcul_with(team,score_hand,score_buy):
    if team == 'us':
        if score_buy == 0 or score_buy is None:
            if score_hand == 0:
                return{
                    'ona':0,
                    'ma':330,
                    'emtiaz_dast':330,
                    'emtiaz_ona':0,
                    'emtiaz_ma':330,
                    'buyer':0,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }
            else:
                return{
                    'ona':score_hand,
                    'ma':-330,
                    'emtiaz_dast':-330,
                    'emtiaz_ona':score_hand,
                    'emtiaz_ma':-330,
                    'buyer':0,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }

        s = score_buy + 100 
        if score_hand >= 90:
            wm = s * 2
            return {
                'ona':+score_hand,
                'ma':-wm,
                'emtiaz_dast':s,
                'emtiaz_ma':-wm,
                'emtiaz_ona':score_hand,
                'buyer':0,
                'color':2,
                'yasa':True,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand >=170 :
            return {
                'ma':-s,
                'ona':+score_hand,
                'emtiaz_dast':s,
                'emtiaz_ma':-s,
                'emtiaz_ona':score_hand,
                'buyer':0,
                'color':2,
                'yasa':False,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand < 170 :
            w = 165 - score_hand
            return {
                'ma':w,
                'ona':score_hand,
                'emtiaz_dast':s,
                'emtiaz_ma': w,
                'emtiaz_ona':score_hand,
                'buyer':0,
                'color':3,
                'yasa':False,
                'edit':False,
                    'sh':False

            }
    elif team == 'them':
        s = score_buy + 100 
        if score_buy == 0 or score_buy is None:
            if score_hand == 0:
                return{
                    'ona':330,
                    'ma':0,
                    'emtiaz_dast':330,
                    'emtiaz_ona':330,
                    'emtiaz_ma':0,
                    'buyer':1,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }
            else:
                return{
                    'ona':-330,
                    'ma':score_hand,
                    'emtiaz_dast':-330,
                    'emtiaz_ona':-330,
                    'emtiaz_ma':score_hand,
                    'buyer':1,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }

        if score_hand >= 90:
            wm = s * 2
            return {
                'ona':-wm,
                'ma':+score_hand,
                'emtiaz_dast':s,
                'emtiaz_ma':score_hand,
                'emtiaz_ona':-wm,
                'buyer':1,
                'color':2,
                'yasa':True,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand >=170 :
            return {
                'ma':+score_hand,
                'ona':-s,
                'emtiaz_dast':s,
                'emtiaz_ma':score_hand,
                'emtiaz_ona':-s,
                'buyer':1,
                'color':2,
                'yasa':False,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand < 170 :
            w = 165 - score_hand
            return {
                'ma':score_hand,
                'ona':w,
                'emtiaz_dast':s,
                'emtiaz_ma': score_hand,
                'emtiaz_ona':w,
                'buyer':1,
                'color':3,
                'yasa':False,
                'edit':False,
                    'sh':False

            }
    else:
        return redirect('shelem_main:history')



########################################### JOKER ########################################################


def calcul_without(team,score_hand,score_buy):
    if team == 'us':
        s = score_buy + 100 
        if score_buy == 0 or score_buy is None:
            if score_hand == 0:
                return{
                    'ona':0,
                    'ma':400,
                    'emtiaz_dast':400,
                    'emtiaz_ona':0,
                    'emtiaz_ma':400,
                    'buyer':0,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }
            else:
                return{
                    'ona':score_hand,
                    'ma':-400,
                    'emtiaz_dast':-400,
                    'emtiaz_ona':score_hand,
                    'emtiaz_ma':-400,
                    'buyer':0,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }

        elif score_hand >= 125:
            wm = s * 2
            return {
                'ona':+score_hand,
                'ma':-wm,
                'emtiaz_dast':s,
                'emtiaz_ma':-wm,
                'emtiaz_ona':score_hand,
                'buyer':0,
                'color':2,
                'yasa':True,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand >=205 :
            return {
                'ma':-s,
                'ona':+score_hand,
                'emtiaz_dast':s,
                'emtiaz_ma':-s,
                'emtiaz_ona':score_hand,
                'buyer':0,
                'color':2,
                'yasa':False,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand < 205 :
            w = 200 - score_hand
            return {
                'ma':w,
                'ona':score_hand,
                'emtiaz_dast':s,
                'emtiaz_ma': w,
                'emtiaz_ona':score_hand,
                'buyer':0,
                'color':3,
                'yasa':False,
                'edit':False,
                    'sh':False

            }
    elif team == 'them':
        s = score_buy + 100 
        if score_buy == 0 or score_buy is None:
            if score_hand == 0:
                return{
                    'ona':400,
                    'ma':0,
                    'emtiaz_dast':400,
                    'emtiaz_ona':400,
                    'emtiaz_ma':0,
                    'buyer':1,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }
            else:
                return{
                    'ona':-400,
                    'ma':score_hand,
                    'emtiaz_dast':-400,
                    'emtiaz_ona':-400,
                    'emtiaz_ma':score_hand,
                    'buyer':1,
                    'color':5,
                    'yasa':False,
                    'edit':False,
                    'sh':True
                }

        if score_hand >= 125:
            wm = s * 2
            return {
                'ona':-wm,
                'ma':+score_hand,
                'emtiaz_dast':s,
                'emtiaz_ma':score_hand,
                'emtiaz_ona':-wm,
                'buyer':1,
                'color':2,
                'yasa':True,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand >=205 :
            return {
                'ma':+score_hand,
                'ona':-s,
                'emtiaz_dast':s,
                'emtiaz_ma':score_hand,
                'emtiaz_ona':-s,
                'buyer':1,
                'color':2,
                'yasa':False,
                'edit':False,
                    'sh':False
            }
        elif s + score_hand < 205 :
            w = 200 - score_hand
            return {
                'ma':score_hand,
                'ona':w,
                'emtiaz_dast':s,
                'emtiaz_ma': score_hand,
                'emtiaz_ona':w,
                'buyer':1,
                'color':3,
                'yasa':False,
                'edit':False,
                    'sh':False,

            }
    else:
        return redirect('shelem_main:history')
        

