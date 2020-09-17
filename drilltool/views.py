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

    	fr = float(request.POST['flowrate'])
    	mw = float(request.POST['mudweight'])
    	dep = float(request.POST['welld'])
    	dpl = float(request.POST['drillpipel'])
    	cl = float(request.POST['casingl'])
    	dcl = float(request.POST['drillcollarl'])    	
    	odp = float(request.POST['drillpipeo'])  
    	idp = float(request.POST['drillpipei'])
    	odc = float(request.POST['drillcollaro'])
    	idc = float(request.POST['drillcollari'])
    	cs = float(request.POST['casingsize'])
    	hs = float(request.POST['holesize']) 


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

    	if Answer == "Herschel Buckley Model" or "Ostwald de Wal Model":
    		x = 1

    		Vp = fr / (2.45 * idp**2)
    		Vc = fr / (2.45 * idc**2)

    		Rnp =(((89100*mw*Vp**(2-flbhi))/cindxi)*((0.0416*idp/3+(1/flbhi))**flbhi))

    		fricP = (1/(1.8*math.log(Rnp/6.9)))**2
    		Pidp = fricP*dpl*mw*Vp**2/(25.8*idp)

    		Rnc = (((89100*mw*Vc**(2-flbhi))/cindxi)*((0.0416*idc/3+(1/flbhi))**flbhi))
    		fricC = (1/(1.8*math.log(Rnc/6.9)))**2
    		Pidc = fricP*dcl*mw*Vc**2/(25.8*idc)


    		Vpca = fr / (2.45 * (cs**2-odp**2))
    		Vpha = fr / (2.45 * (hs**2-odp**2))
    		Vca = fr / (2.45 * (hs**2-odc**2))

    		Rnpca=((109000*mw*Vpca**(2-flbho))/cindxo)*(((0.0208*(cs-odp)))/(2+(1/flbho)))**flbho
    		Padpc = (cl*cindxo*Vpca**flbho)/(144000*(cs-odp)**(1+flbho))*(2+(1/flbho)/0.0208)**flbho
    		Rnpha=((109000*mw*Vpha**(2-flbho))/cindxo)*(((0.0208*(hs-odp)))/(2+(1/flbho)))**flbho
    		dphl = dpl - cl
    		Padph = (dphl*cindxo*Vpha**flbho)/(144000*(hs-odp)**(1+flbho))*(2+(1/flbho)/0.0208)**flbho

    		Rnca=((109000*mw*Vca**(2-flbho))/cindxo)*(((0.0208*(hs-odc)))/(2+(1/flbho)))**flbho
    		Padc = (dcl*cindxo*Vca**flbho)/(144000*(hs-odc)**(1+flbho))*(2+(1/flbho)/0.0208)**flbho

    		tip = Pidp + Pidc
    		tap = Padpc + Padph + Padc
    		ecd = ((tap)/(0.052*dep))+mw
    		tpl = tip + tap


    		hhp = 0.65*(tpl/0.35)
    		hhpd =(((fr**2)*mw)/(hhp*7430*(0.95**2)))**(1/4)
    		hhpbs = (32*hhpd)/(3)**(1/2)

    		jif = 0.47*(tpl/0.53)
    		jifd =(((fr**2)*mw)/(jif*7430*(0.95**2)))**(1/4)
    		jifbs = (32*jifd)/(3)**(1/2)

    		tpph = tpl + hhp
    		tppj = tpl + jif    		
    	else:
    		x = 0
    		pv = PV
    		yp = YLP
    		Vap = fr / (2.45 * idp**2)
    		Vcp = (1.08 * pv + 1.08 * (pv**2 + 9.3*mw*idp**2*yp)**0.5)/(mw * idp)
    		if Vap > Vcp:
    			Rnp = 2970*mw*Vap*idp/pv
    			fricP = (1/(1.8*math.log(Rnp/6.9)))**2
    			Pidp = fricP*dpl*mw*Vap**2/(25.8*idp)
    		else:
    			Pidp = (dpl/(300*idp))*(yp + ((pv*Vap)/(5*idp)))

    		Vac = fr / (2.45 * idc**2)
    		Vcc = (1.08 * pv + 1.08 * (pv**2 + 9.3*mw*idc**2*yp)**0.5)/(mw * idc)
    		if Vac > Vcc:
    			Rnc = 2970*mw*Vac*idc/pv
    			fricC = (1/(1.8*math.log(Rnc/6.9)))**2
    			Pidc = fricC*dcl*mw*Vac**2/(25.8*idc)
    		else:
    			Pidc = (dpl/(300*idc))*(yp + ((pv*Vac)/(5*idc)))

    		Vaca = fr / (2.45 * (hs**2-odc**2))
    		Vcca = (1.08 * pv + 1.08 * (pv**2 + 9.3*mw*(hs-odc)**2*yp)**0.5)/(mw * idc)
    		if Vaca > Vcca:
    			Rnca = 2970*mw*Vaca*(hs-odc)/pv
    			fricCa = (1/(1.8*math.log(Rnca/6.9)))**2
    			Pdca = fricCa*dcl*mw*Vaca**2/(25.8*(hs-odc))
    		else:
    			Pdca = (dcl/(300*(hs-odc)))*(yp + ((pv*Vaca)/(5*(hs-odc))))

    		Vapha = fr / (2.45 * (hs**2-odp**2))
    		Vcpha = (1.08 * pv + 1.08 * (pv**2 + 9.3*mw*(hs-odp)**2*yp)**0.5)/(mw * idc)
    		dphl = dpl - cl
    		if Vapha > Vcpha:
    			Rnpha = 2970*mw*Vapha*(hs-odp)/pv
    			fricPha = (1/(1.8*math.log(Rnpha/6.9)))**2
    			Pdpha = fricCa*dphl*mw*Vapha**2/(25.8*(hs-odp))
    		else:
    			Pdpha = (dphl/(300*(hs-odc)))*(yp + ((pv*Vapha)/(5*(hs-odp))))

    		Vapca = fr / (2.45 * (cs**2-odp**2))
    		Vcpca = (1.08 * pv + 1.08 * (pv**2 + 9.3*mw*(cs-odp)**2*yp)**0.5)/(mw * idc)
    		if Vapca > Vcpca:
    			Rnpca = 2970*mw*Vapca*(cs-odp)/pv
    			fricPca = (1/(1.8*math.log(Rnpca/6.9)))**2
    			Pdpca = fricCa*dphl*mw*Vaca**2/(25.8*(cs-odp))
    		else:
    			Pdpca = (dphl/(300*(cs-odc)))*(yp + ((pv*Vapca)/(5*(cs-odp))))

    		tip = Pidp + Pidc
    		tap = Pdca + Pdpha + Pdpca
    		ecd = ((tap)/(0.052*dep))+mw
    		tpl = tip + tap


    		hhp = 0.65*(tpl/0.35)
    		hhpd =(((fr**2)*mw)/(hhp*7430*(0.95**2)))**(1/4)
    		hhpbs = (32*hhpd)/(3)**(1/2)

    		jif = 0.47*(tpl/0.53)
    		jifd =(((fr**2)*mw)/(jif*7430*(0.95**2)))**(1/4)
    		jifbs = (32*jifd)/(3)**(1/2)

    		tpph = tpl + hhp
    		tppj = tpl + jif    

    	ECD = round(ecd, 3)
    	TPL = round(tpl, 2)
    	TIP = round(tip, 2)
    	TAP = round(tap, 2)
    	HHPBS = round(hhpbs, 2)
    	JIFBS = round(jifbs, 2)
    	TPPH = round(tpph, 2)
    	TPPJ = round(tppj, 2)		
    return render(request, "drill.html", {'result':res, 'model':Answer, 'SR':SR, 'S':S, 
    	'BP':BP0, 'PL':PL0, 'YP':YP0, 's':x, 'ecd':ECD, 'tpl':TPL, 'tip':TIP, 'tap':TAP,
    	'hhpbs':HHPBS, 'jifbs':JIFBS, 'tpph':TPPH, 'tppj':TPPJ})

