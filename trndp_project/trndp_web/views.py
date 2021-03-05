from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from trndp_project.helpers import *
from collections import namedtuple
from django.db import connection
from urllib.parse import parse_qs
from trndp_project.mamdani_calc import *
import trndp_project.TNDP_Evaluator.Evaluator as Ev1
import trndp_project.TNDP_Evaluator.Evaluator2 as Ev2

now = timezone.now()
cursor = connection.cursor()
# import datetime
#
# now = datetime.datetime.now()

# Create your views here.
def empty(request):
    page = { "title": "empty", "sub": "" }
    return render(request, 'trndp_web/empty.html', { "currentTime": now, "page": page })

def home(request):
    page = { "title": "home", "sub": "" }
    cursor.execute("SELECT COUNT(id) total, SUM(IF(gender = 'Male', 1, 0)) malecnt, SUM(IF(gender = 'Female', 1, 0)) femalecnt, "
    "SUM(IF(coping_level = 'VH', 1, 0)) vhcnt, SUM(IF(coping_level = 'H', 1, 0)) hcnt, SUM(IF(coping_level = 'M', 1, 0)) mcnt, SUM(IF(coping_level = 'L', 1, 0)) lcnt, SUM(IF(coping_level = 'VL', 1, 0)) vlcnt "
    "FROM client")
    datax = dictfetchone(cursor)
    print(datax)
    if datax['malecnt']: 
        datax['percentage'] = (datax['malecnt'] / datax['total']) * 100;
    else:
        datax['percentage'] = None
    return render(request, 'trndp_web/home.html', { "currentTime": now, "page": page, "data": datax })

def list_report(request):
    page = { "title": "resources", "sub": "listreport" }
    if request.method == 'GET':
        if 'step' in request.GET and request.GET['step'] == "clienttable":
            cursor.execute("SELECT * FROM client")
            datax = dictfetchall(cursor)
            datay = list(map(cLink , datax))
            return JsonResponse({"data": datay })
        else:
            return render(request, 'trndp_web/list_report.html', { "currentTime": now, "page": page })
    elif request.method == 'POST':
        #Declare array of errorMsg
        errorMsg = []
        if request.POST['step'] == "delete":
            delid = parse_qs(decrypt(request.POST['delid']))
            cursor.execute("DELETE FROM client WHERE id = %s", delid["id"])
            if cursor.rowcount > 0:
                response = "Client record successfully deleted!"
            else:
                response = "No change detected. No record updated!"
            return JsonResponse({"success": True, "response": response})
        else:
            errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})



def client_form(request):
    page = { "title": "resources", "sub": "clientform" }
    if request.method == 'GET':
        return render(request, 'trndp_web/client_form.html', { "currentTime": now, "page": page })
    elif request.method == 'POST':
        #Declare array of errorMsg
        errorMsg = []
        if request.POST['step'] == "add":
            #Custom Validation
            Input = namedtuple('Input',['name','value'])
            fullname = request.POST['fullname']
            age = request.POST['age']
            gender = request.POST['gender']
            cognitive = request.POST['cognitive']
            social = request.POST['social']
            emotional = request.POST['emotional']
            spiritual = request.POST['spiritual']
            physical = request.POST['physical']
            inputlist = [
                Input("Fullname", fullname),
                Input("Age", age),
                Input("Gender", gender),
                Input("Cognitive", cognitive),
                Input("Social", social),
                Input("Emotional", emotional),
                Input("Spiritual", spiritual),
                Input("Physical", physical)
            ]
            errorMsg.extend(checkEmpty(inputlist))
            inputlist = [
                Input("Age", age),
                Input("Cognitive", cognitive),
                Input("Social", social),
                Input("Emotional", emotional),
                Input("Spiritual", spiritual),
                Input("Physical", physical)
            ]
            errorMsg.extend(checkDigit(inputlist))
            if int(request.POST['age']) < 0:
                errorMsg.append("Age cannot less than 0")
            #if no error
            if not errorMsg:
                cursor.execute("INSERT INTO client "
                "(fullname, age, gender, cognitive, social, emotional, spiritual, physical)"
                " VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s)", [fullname, int(age), gender, int(cognitive), int(social), int(emotional), int(spiritual), int(physical)])
                return JsonResponse({"success": True, "response": "Client successfully added!"})
        else:
            errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})

def view_report(request):
    page = { "title": "resources", "sub": "client_form" }
    if request.method == 'GET':
        delid = parse_qs(decrypt(request.GET['q']))
        cursor.execute("SELECT * FROM client WHERE id = %s", delid["id"])
        datax = dictfetchone(cursor)
        trndp = trndp_calc(datax)
        cursor.execute("UPDATE client SET coping_level = %s WHERE id = %s", [trndp['coping'], datax["id"]])
        link = "cog/"+str(datax["id"])+".png"
        return render(request, 'trndp_web/view_report.html', { "currentTime": now, "page": page, "data": datax, "link": link, "trndp": trndp })
    else:
        errorMsg = []
        errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})

def list_trndp(request):
    page = { "title": "home", "sub": "" }
    if request.method == 'GET':
        if 'step' in request.GET and request.GET['step'] == "solutiontable":
            cursor.execute("SELECT * FROM network")
            datax = dictfetchall(cursor)
            datay = list(map(formatDate , datax))
            datay = list(map(cLink , datay))
            return JsonResponse({"data": datay })
        else:
            return render(request, 'trndp_web/list_trndp.html', { "currentTime": now, "page": page })
    elif request.method == 'POST':
        #Declare array of errorMsg
        errorMsg = []
        if request.POST['step'] == "delete":
            delid = parse_qs(decrypt(request.POST['delid']))
            cursor.execute("DELETE FROM network WHERE id = %s", delid["id"])
            if cursor.rowcount > 0:
                response = "TRNDP record successfully deleted!"
            else:
                response = "No change detected. No record updated!"
            return JsonResponse({"success": True, "response": response})
        else:
            errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})


def input(request):
    page = { "title": "input", "sub": "" }
    if request.method == 'GET':
        return render(request, 'trndp_web/input.html', { "currentTime": now, "page": page })
    elif request.method == 'POST':
        #Declare array of errorMsg
        errorMsg = []
        if request.POST['step'] == "add":
            #Custom Validation
            Input = namedtuple('Input',['name','value'])
            popsize = request.POST['popsize']
            mutationrate = request.POST['mutationrate']
            eliterate = request.POST['eliterate']
            maxnode = request.POST['maxnode']
            numroute = request.POST['numroute']
            weighta = request.POST['weighta']
            weightb = request.POST['weightb']
            weightc = request.POST['weightc']
            gen = request.POST['gen']
            networktype = request.POST['network']
            algorithmtype = request.POST['algorithm']
            inputlist = [
                Input("Population Size", popsize),
                Input("Mutation Rate", mutationrate),
                Input("Elite Rate", eliterate),
                Input("Maximum Number of Node", maxnode),
                Input("Number of Route", numroute),
                Input("Weight of Short Travelling Path", weighta),
                Input("Weight of Number of Transfer", weightb),
                Input("Weight of Total Network Length", weightc),
                Input("Max Generation", gen)
            ]
            errorMsg.extend(checkEmpty(inputlist))
            inputlist = [
                Input("Population Size", popsize),
                Input("Maximum Number of Node", maxnode),
                Input("Number of Route", numroute),
                Input("Max Generation", gen)
            ]
            errorMsg.extend(checkDigit(inputlist))
            # if int(request.POST['age']) < 0:
            #     errorMsg.append("Age cannot less than 0")
            #if no error
            if not errorMsg:
                if algorithmtype == "GA1":
                    Ev1.POP_SIZE = int(popsize)
                    Ev1.NUM_ROUTE = int(numroute)
                    Ev1.MUTATION_RATE = float(mutationrate)
                    Ev1.MAX_NODE = int(maxnode)
                    Ev1.ELITE_RATIO = int(float(eliterate)*100)
                    Ev1.W_SHORTPATH = float(weighta)
                    Ev1.W_TRANSFER = float(weightb)
                    Ev1.W_CO = float(weightc)
                    Ev1.MAX_GEN = int(gen)
                    if networktype == "Mumford0":
                        Ev1.NETWORK_TYPE = "mumford0"
                        Ev1.NUM_NODE = 30
                    elif networktype == "Mumford1":
                        Ev1.NETWORK_TYPE = "mumford1"
                        Ev1.NUM_NODE = 70
                    elif networktype == "Mumford2":
                        Ev1.NETWORK_TYPE = "mumford2"
                        Ev1.NUM_NODE = 110
                    elif networktype == "Mumford3":
                        Ev1.NETWORK_TYPE = "mumford3"
                        Ev1.NUM_NODE = 127
                    elif networktype == "Rivera":
                        Ev1.NETWORK_TYPE = "rivera1"
                        Ev1.NUM_NODE = 84
                    else:
                        Ev1.NETWORK_TYPE = "mandl1"
                        Ev1.NUM_NODE = 15
                else:
                    Ev2.POP_SIZE = int(popsize)
                    Ev2.NUM_ROUTE = int(numroute)
                    Ev2.MUTATION_RATE = float(mutationrate)
                    Ev2.MAX_NODE = int(maxnode)
                    Ev2.ELITE_RATIO = int(float(eliterate)*100)
                    Ev2.W_SHORTPATH = float(weighta)
                    Ev2.W_TRANSFER = float(weightb)
                    Ev2.W_CO = float(weightc)
                    Ev2.MAX_GEN = int(gen)
                    if networktype == "Mumford0":
                        Ev2.NETWORK_TYPE = "mumford0"
                        Ev2.NUM_NODE = 30
                    elif networktype == "Mumford1":
                        Ev2.NETWORK_TYPE = "mumford1"
                        Ev2.NUM_NODE = 70
                    elif networktype == "Mumford2":
                        Ev2.NETWORK_TYPE = "mumford2"
                        Ev2.NUM_NODE = 110
                    elif networktype == "Mumford3":
                        Ev2.NETWORK_TYPE = "mumford3"
                        Ev2.NUM_NODE = 127
                    elif networktype == "Rivera":
                        Ev2.NETWORK_TYPE = "rivera1"
                        Ev2.NUM_NODE = 84
                    else:
                        Ev2.NETWORK_TYPE = "mandl1"
                        Ev2.NUM_NODE = 15

                cursor.execute("INSERT INTO network "
                "(algorithm, type, population, mutation_rate, elite_rate, max_node, route_num, short_tw, transfer_w, network_w, max_gen)"
                " VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [networktype, algorithmtype, int(popsize), float(mutationrate), float(eliterate), int(maxnode), int(numroute), float(weighta), float(weightb), float(weightc), int(gen)])
                currentid = cursor.lastrowid 
                try:
                    if algorithmtype == "GA1":
                        Ev1.resetNetwork()
                        Ev1.createNetwork()
                        res = Ev1.gaEval(currentid)
                    else:
                        Ev1.resetNetwork()
                        Ev2.createNetwork()
                        res = Ev2.gaEval(currentid)
                    cursor.execute("UPDATE network SET date = now(), route = %s, d0 = %s, d1 = %s, d2 = %s, dun = %s, att = %s, network_cost = %s, time = %s, best_gen = %s, total_time = %s WHERE id = %s", [res["route"], res["d0"], res["d1"], res["d2"], res["dun"], res["att"], res["network"], res["time"], res["gen"], res["totaltime"], currentid])
                except:
                    cursor.execute("DELETE FROM network WHERE id = %s", [currentid])
                    errorMsg.append("Parameter input is insufficient for solution")
                    return JsonResponse({"success": False, "response": errorMsg})
                return JsonResponse({"success": True, "response": "TRNDP successfully added!", "link": encrypt("id="+str(currentid))})
        else:
            errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})

def output(request):
    page = { "title": "empty", "sub": "" }
    if request.method == 'GET':
        delid = parse_qs(decrypt(request.GET['q']))
        cursor.execute("SELECT * FROM network WHERE id = %s", delid["id"])
        datax = dictfetchone(cursor)
        link = "network/"+str(datax["id"])+".png"
        outputtext = ""
        outputtext += f"Network Type: {datax['type']}\n"
        outputtext += f"Algorithm Used: {datax['algorithm']}\n"
        outputtext += f"Population: {datax['population']}\n"
        outputtext += "Mutation Rate: %.2f\n" % datax['mutation_rate']
        outputtext += "Elite Rate: %.2f\n" % datax['elite_rate']
        outputtext += f"Maximum Number of Nodes: {datax['max_node']}\n"
        outputtext += f"Number of Route: {datax['route_num']}\n"
        outputtext += "Weight of Short Travelling Path: %.2f\n" % datax['short_tw']
        outputtext += "Weight of Number of Transfer: %.2f\n" % datax['transfer_w']
        outputtext += "Weight of Total Network Length: %.2f\n" % datax['network_w']
        outputtext += f"Max Generation: {datax['max_gen']}\n"

        outputtext2 = ""
        outputtext2 = datax["route"]
        outputtext2 += "d0: %.2f%%\n" % datax["d0"]
        outputtext2 += "d1: %.2f%%\n" % datax["d1"]
        outputtext2 += "d2: %.2f%%\n" % datax["d2"]
        outputtext2 += "dun: %.2f%%\n" % datax["dun"]
        outputtext2 += "ATT: %.2f Minutes\n" % datax["att"]
        outputtext2 += f"Network Cost: {datax['network_cost']} Minutes\n"

        outputtext3 = ""
        outputtext3 += "Time: %.2f Seconds\n" % datax["time"]
        outputtext3 += f"Generation: {datax['best_gen']}\n"
        outputtext3 += "Total Time: %.2f Seconds\n" % datax["total_time"]
        return render(request, 'trndp_web/output.html', { "currentTime": now, "page": page, "data": datax, "link": link, 'outputtext': outputtext, 'outputtext2': outputtext2, 'outputtext3': outputtext3,  })
    else:
        errorMsg = []
        errorMsg.append("Request Error")
        return JsonResponse({"success": False, "response": errorMsg})
    
    # outputtext = ""
    # outputtext2 = ""
    # f = open(f"trndp_project/TNDP_Evaluator/eval.txt", "r")
    # for line in f:
    #     outputtext += line
    # f.close()
    # f = open(f"trndp_project/TNDP_Evaluator/comp.txt", "r")
    # for line in f:
    #     outputtext2 += line
    # f.close()
    # return render(request, 'trndp_web/output.html', { "currentTime": now, "page": page, 'outputtext': outputtext, 'outputtext2': outputtext2 })