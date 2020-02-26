from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate, login, logout

from django.core import serializers


def auths(request):
    if request.method == "GET":
    	data = request.GET.copy()
    	username = data.get('id')
    	password = data.get('password')
    	user = authenticate(username=username, password=password)
    	if user:  
    		return JsonResponse({'result':True})
    	else: 
    		return JsonResponse({'result':False})
    	
    else:
    	return JsonResponse({'result':False})


@login_required
def submitPath(request):
    if request.method == "GET":
        data = request.GET.copy()

        username_id = data.get('id')

        driver = Driver.objects.get(user= request.user)
        departure = Location.objects.get(name=data.get('depart'))
        arrive = Location.objects.get(user=data.get('arrive'))
        date =  datetime.strptime(data.get('heure'), '%Y-%m-%d %H:%M:%S')        

        path = Path.objects.create(
            departure=departure, 
            arrive= arrive, 
            datedeparture = date
        )

        propose = Proposal.objects.create(
            driver= driver, 
            path = path
        )
        return JsonResponse({'result':True}) 
    
    else:
        return JsonResponse({'result':False})


@login_required
def searchPath(request):
    sending = []
    if request.method == "GET":
        data = request.GET.copy()
        departure = Location.objects.get(name=data.get('depart'))
        arrive = Location.objects.get(user=data.get('arrive'))
        time =  datetime.strptime(data.get('heure'), '%Y-%m-%d %H:%M:%S') 

        propositions = Proposal.objects.filter(
                path__departure = departure,
                path__arrive = arrive,
                path__datedeparture__gte = time - timedelta(hours=3), 
                path__datedeparture__lte = time + timedelta(hours=3)
        )
            
        propositions.filter(path__datedeparture__gte=timezone.now()).all()
        
        
        for proposal in propositions:
            values = {}
            values['depart'] = serializers.serialize('json', proposal.path.departure)
            values['arrive'] = serializers.serialize('json', proposal.path.arrive)
            values['nomConducteur'] = serializers.serialize('json', proposal.driver.user.username)
            values['telephone'] = serializers.serialize('json', proposal.driver.phone)
            values['heure'] = serializers.serialize('json', proposal.path.datedeparture)
            values['prix'] = ""

            sending.append(values)
    return JsonResponse({'trajets' : sending})


@login_required
def PassengerPath(request):
    sending = []
    if request.method == "GET":
        data = request.GET.copy()
        passengerprofil = Passenger.objects.filter(user=request.user)
        candidate_at = Candidate.objects.filter(passenger=passengerprofil,
                                                proposition__path__datedeparture__gte=timezone.now()).all()

        for candidate in candidate_at:
            values={}
            values['depart'] = serializers.serialize('json', candidate.proposition.path.departure)
            values['arrive'] = serializers.serialize('json', candidate.proposition.path.arrive)
            values['nomConducteur'] = serializers.serialize('json', candidate.proposition.driver.user.username)
            values['telephone'] = serializers.serialize('json', candidate.proposition.driver.phone)
            values['heure'] = serializers.serialize('json', candidate.proposition.path.datedeparture)
            values['prix'] = ""
            values['status'] = serializers.serialize('json', candidate.validate)

            sending.append(values)

    return JsonResponse({'trajets' : sending})



@login_required
def CancelPath(request):
    if request.method == "GET": 
        data = request.GET.copy()
        driver = Driver.objects.get(user= request.user)

        propositions = Proposal.objects.filter(
                driver = driver,
                path__departure = departure,
                path__arrive = arrive,
                path__datedeparture = time
        ).delete()

        return JsonResponse({'result' : True})

    return JsonResponse({'result' : False})


    
@login_required
def DriverPath(request):
    sending = []
    if request.method == "GET":
        data = request.GET.copy()
        driverprofil = Passenger.objects.filter(user=request.user)
        propositions = Proposal.objects.filter(driver=driverprofil,
                                                path__datedeparture__gte=timezone.now()).all()

        for proposition in propositions:
            values={}
            values['depart'] = serializers.serialize('json', proposition.path.departure)
            values['arrive'] = serializers.serialize('json', proposition.path.arrive)
            values['nomConducteur'] = serializers.serialize('json', proposition.driver.user.username)
            values['telephone'] = serializers.serialize('json', proposition.driver.phone)
            values['heure'] = serializers.serialize('json', proposition.path.datedeparture)
            values['prix'] = ""

            sending.append(values)

    return JsonResponse({'trajets' : sending})

