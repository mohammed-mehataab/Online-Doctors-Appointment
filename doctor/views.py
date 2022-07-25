from django.shortcuts import render, redirect
from rest_framework.views import APIView 
from rest_framework.response import Response

from patient.models import Patient
from . models import Doctors, Avail
from . forms import DoctorForm, AvailForm
import json
# Create your views here.

class Auth(APIView): 
    
    def get(self, request):
        response = {}
        get_data = Doctors.objects.all()
        payload = []
        try:
            for data in get_data: 
                payload.append({
                    "id": data.id,
                    "name": data.name, 
                    "specialization":data.specialization, 
                    "profile_pic": f"http://127.0.0.1:8000/images/{data.profilepic}"
                })

            response['data'] = payload
            response['message'] = "success"
            return Response(response)
        except Exception as e:
            return Response({"message":"failed"})

    def post(self, request): 
        response = {}
        data = request.data 
        checking = data.get("token")
        if data['message'] == "history":
            response = {}
            obj = Avail.objects.filter(email = data['email'])
            payload = [] 
            for i in obj:
                    payload.append({
                    "doctor_name":i.name,
                    "email":i.email,
                    "time":i.time,
                    'patient_name':i.patientname,
                    "issue":i.issue
                    })
            response['data'] = payload
            return Response(response)
    
        if data['message'] == "spec":
            payload = []
            get_data = Doctors.objects.filter(specialization=data['spec'])
            try:
                for data in get_data: 
                    payload.append({
                    "id": data.id,
                    "name": data.name, 
                    "specialization":data.specialization, 
                    "profile_pic": f"http://127.0.0.1:8000/images/{data.profilepic}"
                    })

                response['data'] = payload
                response['message'] = "success"
                return Response(response)
            except Exception as e:
                return Response({"message":"failed"})



        if checking == "signup":
            email = data.get("email")
            obj = DoctorForm(data = request.data)
            try:
                check = Doctors.objects.filter(email = email)
            except:
                pass
            try:
                if len(check) >= 1:
                    response['message'] = "account exists"
                    return Response(response)
                if obj.is_valid():
                    response['message'] = 200 
                    obj.save()
                    return Response(response)
                return Response(obj.errors())
            except Exception as e:
                return Response(obj.errors())
    
        email = data.get("email")
        password = data.get("password")
        try:
            obj = Doctors.objects.get(email = email)
            if obj.email == email and obj.password == password:
                response = {}
                response['message'] = 200 
                response['name'] = obj.name 
                response['email'] = obj.email
                return Response(response)
            return Response({"message":"invalid credentials"})
        except Exception as e:
            return Response({"message":"invalid credentials"}) 
        


Auth = Auth.as_view()



def single(request,pk):
    get_data = Doctors.objects.get(id = pk)



    time = json.loads(get_data.time)
    li = [] 
    for i in time.values():
        li.append(i)

    context = {'data':get_data, 'time':li}
    if request.method == "POST":
        try:
            data = AvailForm(data = request.POST)
            main_data = request.POST['email']
            change_time = request.POST['time']
        
            if data.is_valid():
                data.save()
            
            for i in Avail.objects.all():
                get_data = Doctors.objects.get(email = main_data)
                get_timing = json.loads(get_data.time)
                # context = {}
                try:
                    del(get_timing[change_time])
                except:
                    pass

                get_data.time = json.dumps(get_timing)
                get_data.save(update_fields=['time'])
                return redirect("http://127.0.0.1:5501/frontend/patienthome.html")
                # context['gas'] = get_timing
                # pass
            # return render(request, 'doctor/main.html', context)
        except:
            pass
    return render(request, 'doctor/main.html', context)



class History(APIView):
    def post(self, request):
        response = {}
        data = request.data
        email = data['email']
        get_data = Patient.objects.get(email = "yacoob@gmail.com")
        get_data = get_data.name
        # get_data = get_data.avail.objects.all()
        
        payload = []
        try:
            # for data in get_data: 
            #     payload.append({
            #         "patient_name": data.patient, 
            #         "doctor_name":data.name,
            #         "email":data.email, 
            #         "specialization":data.specialization,
            #         "time":data.time 
            #         # "profile_pic": f"http://localhost:8000/images/{data.profilepic}",
            #     })

            response['main'] = json.dumps(get_data)
            response['message'] = "success"
            return Response(data)
        except Exception as e:
            return Response({"message":"failed"})
History = History.as_view()


class Main(APIView):
    def post(self, request):
        response = {}
        data = request.data
        email = data['email']
        try:
            obj = Doctors.objects.get(email = email)
            response['user_name'] = obj.name 
            response['user_spec'] = obj.specialization
            response['user_email'] = obj.email 
            response['img'] = f"http://127.0.0.1:8000/images/{obj.profilepic}"
            return Response(response)
        except: 
            return Response({"message":"failed"})
        

Main = Main.as_view()