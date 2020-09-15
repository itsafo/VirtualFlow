from django.shortcuts import render
import math
from sklearn.metrics import mean_squared_error, r2_score
# , get_object_or_404, redirect
# from django.template import loader
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # One good old style of programming functions
    # Define your context variable, then render
    return render(request, "index.html", {})


# +++++++++++++++ CALCULATION FUNCTIONS ++++++++++++++
def drill(request):
    # One good old style of programming functions
    # Define your context variable, then render
    if request.method == 'POST':
    	a = 600
    	b = 300
    	c = 200
    	d = 100 
    	e = 6
    	f = 3

    	a2 = round(a * 1.7032, 0)
    	b2 = round(b * 1.7032, 0)
    	c2 = round(c * 1.7032, 0)
    	d2 = round(d * 1.7032, 0)
    	e2 = round(e * 1.7032, 0)
    	f2 = round(f * 1.7032, 0)

    	a11 = int(request.POST['num1'])
    	b11 = int(request.POST['num2'])
    	c11 = int(request.POST['num3'])
    	d11 = int(request.POST['num4'])
    	e11 = int(request.POST['num5'])
    	f11 = int(request.POST['num6'])	

    	a3 = a11 * 5.1
    	b3 = b11 * 5.10
    	c3 = c11 * 5.10
    	d3 = d11 * 5.1
    	e3 = e11 * 5.10
    	f3 = f11 * 5.10

    	T = int(request.POST['temp'])
    	P = int(request.POST['psi'])

    	a4 = a3*(2.74*math.exp(-0.0064*T+(0.1*10**-4)*P))
    	b4 = b3*(2.74*math.exp(-0.0064*T+(0.1*10**-4)*P))
    	c4 = c3*(2.74*math.exp(-0.0064*T+(0.1*10**-4)*P))
    	d4 = d3*(2.74*math.exp(-0.0064*T+(0.1*10**-4)*P))
    	e4 = e3*(2.74*math.exp(-0.0064*T+(0.1*10**-4)*P))
    	f4 = f3*(2.74*math.exp(-0.0064*T+(0.1*10**-4)*P))

    	a5 = a3*(1.95*math.exp(-0.0038*T+(0.5*10**-4)*P))
    	b5 = b3*(1.95*math.exp(-0.0038*T+(0.5*10**-4)*P))
    	c5 = c3*(1.95*math.exp(-0.0038*T+(0.5*10**-4)*P))
    	d5 = d3*(1.95*math.exp(-0.0038*T+(0.5*10**-4)*P))
    	e5 = e3*(1.95*math.exp(-0.0038*T+(0.5*10**-4)*P))
    	f5 = f3*(1.95*math.exp(-0.0038*T+(0.5*10**-4)*P))

    	v = a11 - b11
    	y = b11 - v
    	v1 = v * 5.1
    	y1 = y * 5.1
    	BP1 = y1 + v1 / 479 * a2
    	BP2 = y1 + v1 / 479 * b2
    	BP3 = y1 + v1 / 479 * c2
    	BP4 = y1 + v1 / 479 * d2
    	BP5 = y1 + v1 / 479 * e2
    	BP6 = y1 + v1 / 479 * f2

    	nn = 3.32 * math.log(a4/b4, 10)
    	Kk = 100 * a4 / a2 ** nn

    	n = 0.5 * math.log(b4/f4, 10)
    	K = 100 * b4 / b2 ** n

    	PL1 = (K/100) * a2 ** n
    	PL2 = (K/100) * b2 ** n
    	PL3 = (K/100) * c2 ** n
    	PL4 = (K/100) * d2 ** n
    	PL5 = (K/100) * e2 ** n
    	PL6 = (K/100) * f2 ** n
    	y3 = 2 * f4 - (e4)

    	nn1 = 3.32 * math.log((a4 - y3) / (b4 - y3), 10)
    	Kk1 = 100 * ((a4 - y3) / (a2 ** nn1))

    	n1 = 0.5 * math.log((b4 - y3) / (f4 - y3), 10)
    	K1 = 100 * ((b4 - y3) / (b2 ** n1))

    	YP1 =  y3 + (K1 / 100) * a2 ** n1
    	YP2 =  y3 + (K1 / 100) * b2 ** n1
    	YP3 =  y3 + (K1 / 100) * c2 ** n1
    	YP4 =  y3 + (K1 / 100) * d2 ** n1
    	YP5 =  y3 + (K1 / 100) * e2 ** n1
    	YP6 =  y3 + (K1 / 100) * f2 ** n1
    	S = [f4, e4, d4, c4, b4, a4]
    	BP0 = [BP6, BP5, BP4, BP3, BP2, BP1]
    	PL0 = [PL6, PL5, PL4, PL3, PL2, PL1]
    	YP0 = [YP6, YP5, YP4, YP3, YP2, YP1]
    	SR = [f2, e2, d2, c2, b2, a2]
    	BP = r2_score(S, BP0)
    	PL = r2_score(S, PL0)
    	YP = r2_score(S, YP0)

    	if BP > PL and BP > YP:
    		Rsquare = BP
    		Answer = "Bingham Fluid"
    		flbhi = 0
    		cindxi = 0
    		flbho = 0
    		cindxo = 0
    		PV = v
    		YLP = y
    	elif PL > BP and PL > YP:
    		Rsquare = PL
    		Answer = "Ostwald de Wal Model"
    		flbhi = nn
    		cindxi = Kk
    		flbho = n
    		cindxo = K
    		PV = v
    		YLP = y
    	elif YP > BP and YP > PL:
    		Rsquare = YP
    		Answer = "Herschel Buckley Model"
    		flbhi = nn1
    		cindxi = Kk1
    		flbho = n1
    		cindxo = K1
    		PV = v
    		YLP = y

    	res = round(Rsquare, 3)
    	ans = Answer
    return render(request, "drill.html", {'result':res, 'model':ans, 'SR':SR, 'S':S, 
    	'BP':BP0, 'PL':PL0, 'YP':YP0})

