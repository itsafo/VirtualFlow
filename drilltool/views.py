from django.shortcuts import render
from .forms import ReinforcementForm
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

def ref(request):
    # One good old style of programming functions
    # Define your context variable, then render
    return render(request, "ref.html", {})

def blog(request):
    # One good old style of programming functions
    # Define your context variable, then render
    return render(request, "blog-index.html", {})   

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


def BRF(request):
    # One good old style of programming functions
    # Define your context variable, then render

    if request.method == 'POST':
        # Pass the form data to the form class
        details = ReinforcementForm(request.POST)

        # In the 'form' class the clean function 
        # is defined, if all the data is correct 
        # as per the clean function, it returns true 
        if details.is_valid():       
            db = float(request.POST['bnpd'])
            dh = float(request.POST['hnpd'])
            c = float(request.POST['ch'])

            # ===Coding for header pipe thickness table===
            h_thick = float(request.POST['h_thick'])
            # NPS 1/2
            if dh  == 0.125:
                dh = 0.405
                if h_thick == 1 or h_thick  == 2:
                    th = 0.035
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.049
                elif h_thick == 6:
                    th = 0.057
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.068*0.875
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.095
                th = th * 0.875
            # NPS 1/4
            if dh  == 0.25:
                dh = 0.54
                if h_thick == 1 or h_thick  == 2:
                    th = 0.049
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.065
                elif h_thick == 6:
                    th = 0.073
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.088*0.875
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.119
                th = th * 0.875
            # NPS 3/8
            if dh  == 0.375:
                dh = 0.675
                if h_thick == 1 or h_thick  == 2:
                    th = 0.049
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.065
                elif h_thick == 6:
                    th = 0.073
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.091*0.875
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.126
                th = th * 0.875
            # NPS 1/2
            if dh  == 0.5:
                dh = 0.84
                if h_thick == 1 or h_thick  == 2:
                    th = 0.065
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.083
                elif h_thick == 6:
                    th = 0.095
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.109
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.147
                elif h_thick == 15:
                    th = 0.188
                elif h_thick == 18:
                    th = 0.294
                th = th * 0.875
            # NPS 3/4
            if dh  == 0.75:
                dh = 1.05
                if h_thick == 1 or h_thick  == 2:
                    th = 0.065
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.083
                elif h_thick == 6:
                    th = 0.095
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.113
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.154
                elif h_thick == 15:
                    th = 0.219
                elif h_thick == 18:
                    th = 0.308
                th = th * 0.875
            # NPS 1
            if dh  == 1:
                dh = 1.315
                if h_thick == 1 or h_thick  == 2:
                    th = 0.065
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.109
                elif h_thick == 6:
                    th = 0.114
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.133
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.179
                elif h_thick == 15:
                    th = 0.250
                elif h_thick == 18:
                    th = 0.358
                th = th * 0.875
            # NPS 1 1/4
            if dh  == 1.125:
                dh = 1.66
                if h_thick == 1 or h_thick  == 2:
                    th = 0.065
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.109
                elif h_thick == 6:
                    th = 0.117
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.140
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.191
                elif h_thick == 15:
                    th = 0.250
                elif h_thick == 18:
                    th = 0.382
                th = th * 0.875
            # NPS 1 1/2
            if dh  == 1.5:
                dh = 1.9
                if h_thick == 1 or h_thick  == 2:
                    th = 0.065
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.109
                elif h_thick == 6:
                    th = 0.125
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.145
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.200
                elif h_thick == 15:
                    th = 0.281
                elif h_thick == 18:
                    th = 0.4
                th = th * 0.875
            # NPS 2
            if dh  == 2:
                dh = 2.375
                if h_thick == 1 or h_thick  == 2:
                    th = 0.065
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.109
                elif h_thick == 6:
                    th = 0.125
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.154
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.218
                elif h_thick == 15:
                    th = 0.344
                elif h_thick == 18:
                    th = 0.436
                th = th * 0.875
            # NPS 2 1/2
            if dh  == 2.5:
                dh = 2.875
                if h_thick == 1 or h_thick  == 2:
                    th = 0.083
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.12
                elif h_thick == 6:
                    th = 0.188
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.203
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.276
                elif h_thick == 13:
                    th = 0.3
                elif h_thick == 15:
                    th = 0.375
                elif h_thick == 18:
                    th = 0.552
                th = th * 0.875
            # NPS 3
            if dh  == 3:
                dh = 3.5
                if h_thick == 1 or h_thick  == 2:
                    th = 0.083
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.12
                elif h_thick == 6:
                    th = 0.188
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.216
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.3
                elif h_thick == 13:
                    th = 0.35
                elif h_thick == 15:
                    th = 0.438
                elif h_thick == 18:
                    th = 0.6
                th = th * 0.875
            # NPS 3 1/2
            if dh  == 3.5:
                dh = 4
                if h_thick == 1 or h_thick  == 2:
                    th = 0.083
                elif h_thick == 3 or h_thick  == 4 or h_thick  == 5:
                    th = 0.12
                elif h_thick == 6:
                    th = 0.188
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.226
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.318
                elif h_thick == 18:
                    th = 0.636
                th = th * 0.875
            # NPS 4
            if dh  == 4:
                dh = 4.5
                if h_thick == 1 or h_thick  == 2:
                    th = 0.083
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.12
                elif h_thick == 6:
                    th = 0.188
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.237
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.337
                elif h_thick == 13:
                    th = 0.437
                elif h_thick == 15:
                    th = 0.531
                elif h_thick == 18:
                    th = 0.674
                th = th * 0.875
            # NPS 4 1/2
            if dh  == 4.5:
                dh = 5
                if h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.247
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.355
                elif h_thick == 18:
                    th = 0.71
                th = th * 0.875
            # NPS 5
            if dh  == 5:
                dh = 5.563
                if h_thick == 1 or h_thick  == 2:
                    th = 0.109
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.134
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.258
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.375
                elif h_thick == 13:
                    th = 0.5
                elif h_thick == 15:
                    th = 0.625
                elif h_thick == 18:
                    th = 0.75
                th = th * 0.875
            # NPS 6
            if dh  == 6:
                dh = 6.625
                if h_thick == 1 or h_thick  == 2:
                    th = 0.109
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.134
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.280
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.432
                elif h_thick == 13:
                    th = 0.562
                elif h_thick == 15:
                    th = 0.719
                elif h_thick == 18:
                    th = 0.864
                th = th * 0.875
            # NPS 7
            if dh  == 7:
                dh = 7.625
                if h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.301
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 18:
                    th = 0.875
                th = th * 0.875
            # NPS 8
            if dh  == 8:
                dh = 8.625
                if h_thick == 1 or h_thick  == 2:
                    th = 0.109
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.148
                elif h_thick == 5:
                    th = 0.250
                elif h_thick == 6:
                    th = 0.277
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.322
                elif h_thick == 9:
                    th = 0.406
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 0.593
                elif h_thick == 13:
                    th = 0.719
                elif h_thick == 14:
                    th = 0.812
                elif h_thick == 15:
                    th = 0.906
                elif h_thick == 18:
                    th = 0.875
                th = th * 0.875
            # NPS 9
            if dh  == 9:
                dh = 9.625
                if h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.342
                elif h_thick == 10 or h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                th = th * 0.875
            # NPS 10
            if dh  == 10:
                dh = 10.75
                if h_thick == 1 or h_thick  == 2:
                    th = 0.134
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.165
                elif h_thick == 5:
                    th = 0.250
                elif h_thick == 6:
                    th = 0.307
                elif h_thick == 7 or h_thick  == 8 or h_thick  == 16:
                    th = 0.365
                elif h_thick == 9:
                    th = 0.5
                elif h_thick == 10:
                    th = 0.594
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 0.718
                elif h_thick == 13:
                    th = 0.843
                elif h_thick == 14:
                    th = 1
                elif h_thick == 15:
                    th = 1.125
                th = th * 0.875
            # NPS 10
            if dh  == 12:
                dh = 12.75
                if h_thick == 1 or h_thick  == 2:
                    th = 0.156
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.180
                elif h_thick == 5:
                    th = 0.250
                elif h_thick == 6:
                    th = 0.330
                elif h_thick == 7:
                    th = 0.406
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick == 9:
                    th = 0.562
                elif h_thick == 10:
                    th = 0.687
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 0.843
                elif h_thick == 13:
                    th = 1
                elif h_thick == 14:
                    th = 1.125
                elif h_thick == 15:
                    th = 1.312
                th = th * 0.875
            # NPS 14
            if dh  == 14:
                dh = 14
                if h_thick == 1 or h_thick  == 2:
                    th = 0.156
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.250
                elif h_thick == 5:
                    th = 0.312
                elif h_thick == 6:
                    th = 0.375
                elif h_thick == 7:
                    th = 0.437
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick == 9:
                    th = 0.593
                elif h_thick == 10:
                    th = 0.750
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 0.937
                elif h_thick == 13:
                    th = 1.093
                elif h_thick == 14:
                    th = 1.25
                elif h_thick == 15:
                    th = 1.406
                th = th * 0.875
            # NPS 16
            if dh  == 16:
                dh = 16
                if h_thick == 1 or h_thick  == 2:
                    th = 0.165
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.250
                elif h_thick == 5:
                    th = 0.312
                elif h_thick == 6:
                    th = 0.375
                elif h_thick == 7:
                    th = 0.5
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick == 9:
                    th = 0.656
                elif h_thick == 10:
                    th = 0.843
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 1.031
                elif h_thick == 13:
                    th = 1.218
                elif h_thick == 14:
                    th = 1.437
                elif h_thick == 15:
                    th = 1.594
                th = th * 0.875
            # NPS 18
            if dh  == 18:
                dh = 18
                if h_thick == 1 or h_thick  == 2:
                    th = 0.165
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.250
                elif h_thick == 5:
                    th = 0.312
                elif h_thick == 6:
                    th = 0.437
                elif h_thick == 7:
                    th = 0.562
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick == 9:
                    th = 0.75
                elif h_thick == 10:
                    th = 0.927
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 1.156
                elif h_thick == 13:
                    th = 1.375
                elif h_thick == 14:
                    th = 1.562
                elif h_thick == 15:
                    th = 1.781
                th = th * 0.875
            # NPS 20
            if dh  == 20:
                dh = 20
                if h_thick == 1 or h_thick  == 2:
                    th = 0.188
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.250
                elif h_thick == 5:
                    th = 0.375
                elif h_thick == 6:
                    th = 0.5
                elif h_thick == 7:
                    th = 0.593
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick == 9:
                    th = 0.812
                elif h_thick == 10:
                    th = 1.031
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 1.28
                elif h_thick == 13:
                    th = 1.5
                elif h_thick == 14:
                    th = 1.75
                elif h_thick == 15:
                    th = 1.968
                th = th * 0.875
            # NPS 22
            if dh  == 22:
                dh = 22
                if h_thick == 1 or h_thick  == 2:
                    th = 0.188
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.250
                elif h_thick == 5:
                    th = 0.375
                elif h_thick == 6:
                    th = 0.5
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick == 9:
                    th = 0.875
                elif h_thick == 10:
                    th = 1.125
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 1.375
                elif h_thick == 13:
                    th = 1.625
                elif h_thick == 14:
                    th = 1.875
                elif h_thick == 15:
                    th = 2.125
                th = th * 0.875
            # NPS 24
            if dh  == 24:
                dh = 24
                if h_thick == 1 or h_thick  == 2:
                    th = 0.218
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.250
                elif h_thick == 5:
                    th = 0.375
                elif h_thick == 6:
                    th = 0.562
                elif h_thick  == 7:
                    th = 0.687
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick == 9:
                    th = 0.968
                elif h_thick == 10:
                    th = 1.218
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                elif h_thick == 12:
                    th = 1.531
                elif h_thick == 13:
                    th = 1.812
                elif h_thick == 14:
                    th = 2.062
                elif h_thick == 15:
                    th = 2.343
                th = th * 0.875
            # NPS 26
            if dh  == 26:
                dh = 26
                if h_thick == 3 or h_thick  == 4:
                    th = 0.312
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                th = th * 0.875
            # NPS 28
            if dh  == 28:
                dh = 28
                if h_thick == 3 or h_thick  == 4:
                    th = 0.312
                elif h_thick == 6:
                    th = 0.625
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                th = th * 0.875
            # NPS 30
            if dh  == 30:
                dh = 30
                if h_thick == 1 or h_thick  == 2:
                    th = 0.250
                elif h_thick == 3 or h_thick  == 4:
                    th = 0.312
                elif h_thick == 6:
                    th = 0.625
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                th = th * 0.875
            # NPS 32
            if dh  == 32:
                dh = 32
                if h_thick == 3 or h_thick  == 4:
                    th = 0.312
                elif h_thick == 6:
                    th = 0.625
                elif h_thick == 7:
                    th = 0.688
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                th = th * 0.875
            # NPS 34
            if dh  == 34:
                dh = 34
                if h_thick == 3 or h_thick  == 4:
                    th = 0.312
                elif h_thick == 6:
                    th = 0.625
                elif h_thick == 7:
                    th = 0.688
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                th = th * 0.875
            # NPS 36
            if dh  == 36:
                dh = 36
                if h_thick == 3 or h_thick  == 4:
                    th = 0.312
                elif h_thick  == 8 or h_thick  == 16:
                    th = 0.375
                elif h_thick  == 11 or h_thick  == 17:
                    th = 0.5
                th = th * 0.875
            # NPS 40
            if dh  >= 40:
                if h_thick == 16:
                    th = 0.375
                elif h_thick == 17:
                    th = 0.5
                elif h_thick == 18:
                    th = 1
                th = th * 0.875


            # ===Coding for branch pipe thickness table===
            b_thick = float(request.POST['b_thick'])
            # NPS 1/2
            if db  == 0.125:
                db = 0.405
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.035
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.049
                elif b_thick == 6:
                    Tb = 0.057
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.068*0.875
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.095
                Tb = Tb * 0.875
            # NPS 1/4
            if db  == 0.25:
                db = 0.54
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.049
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.065
                elif b_thick == 6:
                    Tb = 0.073
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.088*0.875
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.119
                Tb = Tb * 0.875
            # NPS 3/8
            if db  == 0.375:
                db = 0.675
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.049
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.065
                elif b_thick == 6:
                    Tb = 0.073
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.091*0.875
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.126
                Tb = Tb * 0.875
            # NPS 1/2
            if db  == 0.5:
                db = 0.84
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.065
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.083
                elif b_thick == 6:
                    Tb = 0.095
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.109
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.147
                elif b_thick == 15:
                    Tb = 0.188
                elif b_thick == 18:
                    Tb = 0.294
                Tb = Tb * 0.875
            # NPS 3/4
            if db  == 0.75:
                db = 1.05
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.065
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.083
                elif b_thick == 6:
                    Tb = 0.095
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.113
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.154
                elif b_thick == 15:
                    Tb = 0.219
                elif b_thick == 18:
                    Tb = 0.308
                Tb = Tb * 0.875
            # NPS 1
            if db  == 1:
                db = 1.315
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.065
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.109
                elif b_thick == 6:
                    Tb = 0.114
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.133
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.179
                elif b_thick == 15:
                    Tb = 0.250
                elif b_thick == 18:
                    Tb = 0.358
                Tb = Tb * 0.875
            # NPS 1 1/4
            if db  == 1.125:
                db = 1.66
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.065
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.109
                elif b_thick == 6:
                    Tb = 0.117
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.140
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.191
                elif b_thick == 15:
                    Tb = 0.250
                elif b_thick == 18:
                    Tb = 0.382
                Tb = Tb * 0.875
            # NPS 1 1/2
            if db  == 1.5:
                db = 1.9
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.065
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.109
                elif b_thick == 6:
                    Tb = 0.125
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.145
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.200
                elif b_thick == 15:
                    Tb = 0.281
                elif b_thick == 18:
                    Tb = 0.4
                Tb = Tb * 0.875
            # NPS 2
            if db  == 2:
                db = 2.375
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.065
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.109
                elif b_thick == 6:
                    Tb = 0.125
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.154
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.218
                elif b_thick == 15:
                    Tb = 0.344
                elif b_thick == 18:
                    Tb = 0.436
                Tb = Tb * 0.875
            # NPS 2 1/2
            if db  == 2.5:
                db = 2.875
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.083
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.12
                elif b_thick == 6:
                    Tb = 0.188
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.203
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.276
                elif b_thick == 13:
                    Tb = 0.3
                elif b_thick == 15:
                    Tb = 0.375
                elif b_thick == 18:
                    Tb = 0.552
                Tb = Tb * 0.875
            # NPS 3
            if db  == 3:
                db = 3.5
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.083
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.12
                elif b_thick == 6:
                    Tb = 0.188
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.216
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.3
                elif b_thick == 13:
                    Tb = 0.35
                elif b_thick == 15:
                    Tb = 0.438
                elif b_thick == 18:
                    Tb = 0.6
                Tb = Tb * 0.875
            # NPS 3 1/2
            if db  == 3.5:
                db = 4
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.083
                elif b_thick == 3 or b_thick  == 4 or b_thick  == 5:
                    Tb = 0.12
                elif b_thick == 6:
                    Tb = 0.188
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.226
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.318
                elif b_thick == 18:
                    Tb = 0.636
                Tb = Tb * 0.875
            # NPS 4
            if db  == 4:
                db = 4.5
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.083
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.12
                elif b_thick == 6:
                    Tb = 0.188
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.237
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.337
                elif b_thick == 13:
                    Tb = 0.437
                elif b_thick == 15:
                    Tb = 0.531
                elif b_thick == 18:
                    Tb = 0.674
            
            ## ERROR! NPS 4.5 and 5 takes the value of NPS 4
            # NPS 4 1/2
            if db  == 4.51:
                db = 5
                if b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.247
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.355
                elif b_thick == 18:
                    Tb = 0.71
                Tb = Tb * 0.875
            # NPS 4 1/2
            if db == 5.1:
                db = 5.563
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.109
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.134
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.258
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.375
                elif b_thick == 13:
                    Tb = 0.5
                elif b_thick == 15:
                    Tb = 0.625
                elif b_thick == 18:
                    Tb = 0.75
                Tb = Tb * 0.875
            ## EROR SECTION END ===============

            # NPS 6
            if db  == 6:
                db = 6.625
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.109
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.134
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.280
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.432
                elif b_thick == 13:
                    Tb = 0.562
                elif b_thick == 15:
                    Tb = 0.719
                elif b_thick == 18:
                    Tb = 0.864
                Tb = Tb * 0.875
            # NPS 7
            if db  == 7:
                db = 7.625
                if b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.301
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 18:
                    Tb = 0.875
                Tb = Tb * 0.875
            # NPS 8
            if db  == 8:
                db = 8.625
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.109
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.148
                elif b_thick == 5:
                    Tb = 0.250
                elif b_thick == 6:
                    Tb = 0.277
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.322
                elif b_thick == 9:
                    Tb = 0.406
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 0.593
                elif b_thick == 13:
                    Tb = 0.719
                elif b_thick == 14:
                    Tb = 0.812
                elif b_thick == 15:
                    Tb = 0.906
                elif b_thick == 18:
                    Tb = 0.875
                Tb = Tb * 0.875
            # NPS 9
            if db  == 9:
                db = 9.625
                if b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.342
                elif b_thick == 10 or b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                Tb = Tb * 0.875
            # NPS 10
            if db  == 10:
                db = 10.75
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.134
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.165
                elif b_thick == 5:
                    Tb = 0.250
                elif b_thick == 6:
                    Tb = 0.307
                elif b_thick == 7 or b_thick  == 8 or b_thick  == 16:
                    Tb = 0.365
                elif b_thick == 9:
                    Tb = 0.5
                elif b_thick == 10:
                    Tb = 0.594
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 0.718
                elif b_thick == 13:
                    Tb = 0.843
                elif b_thick == 14:
                    Tb = 1
                elif b_thick == 15:
                    Tb = 1.125
                Tb = Tb * 0.875
            # NPS 10
            if db  == 12:
                db = 12.75
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.156
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.180
                elif b_thick == 5:
                    Tb = 0.250
                elif b_thick == 6:
                    Tb = 0.330
                elif b_thick == 7:
                    Tb = 0.406
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick == 9:
                    Tb = 0.562
                elif b_thick == 10:
                    Tb = 0.687
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 0.843
                elif b_thick == 13:
                    Tb = 1
                elif b_thick == 14:
                    Tb = 1.125
                elif b_thick == 15:
                    Tb = 1.312
                Tb = Tb * 0.875
            # NPS 14
            if db  == 14:
                db = 14
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.156
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.250
                elif b_thick == 5:
                    Tb = 0.312
                elif b_thick == 6:
                    Tb = 0.375
                elif b_thick == 7:
                    Tb = 0.437
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick == 9:
                    Tb = 0.593
                elif b_thick == 10:
                    Tb = 0.750
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 0.937
                elif b_thick == 13:
                    Tb = 1.093
                elif b_thick == 14:
                    Tb = 1.25
                elif b_thick == 15:
                    Tb = 1.406
                Tb = Tb * 0.875
            # NPS 16
            if db  == 16:
                db = 16
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.165
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.250
                elif b_thick == 5:
                    Tb = 0.312
                elif b_thick == 6:
                    Tb = 0.375
                elif b_thick == 7:
                    Tb = 0.5
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick == 9:
                    Tb = 0.656
                elif b_thick == 10:
                    Tb = 0.843
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 1.031
                elif b_thick == 13:
                    Tb = 1.218
                elif b_thick == 14:
                    Tb = 1.437
                elif b_thick == 15:
                    Tb = 1.594
                Tb = Tb * 0.875
            # NPS 18
            if db  == 18:
                db = 18
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.165
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.250
                elif b_thick == 5:
                    Tb = 0.312
                elif b_thick == 6:
                    Tb = 0.437
                elif b_thick == 7:
                    Tb = 0.562
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick == 9:
                    Tb = 0.75
                elif b_thick == 10:
                    Tb = 0.927
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 1.156
                elif b_thick == 13:
                    Tb = 1.375
                elif b_thick == 14:
                    Tb = 1.562
                elif b_thick == 15:
                    Tb = 1.781
                Tb = Tb * 0.875
            # NPS 20
            if db  == 20:
                db = 20
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.188
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.250
                elif b_thick == 5:
                    Tb = 0.375
                elif b_thick == 6:
                    Tb = 0.5
                elif b_thick == 7:
                    Tb = 0.593
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick == 9:
                    Tb = 0.812
                elif b_thick == 10:
                    Tb = 1.031
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 1.28
                elif b_thick == 13:
                    Tb = 1.5
                elif b_thick == 14:
                    Tb = 1.75
                elif b_thick == 15:
                    Tb = 1.968
                Tb = Tb * 0.875
            # NPS 22
            if db  == 22:
                db = 22
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.188
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.250
                elif b_thick == 5:
                    Tb = 0.375
                elif b_thick == 6:
                    Tb = 0.5
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick == 9:
                    Tb = 0.875
                elif b_thick == 10:
                    Tb = 1.125
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 1.375
                elif b_thick == 13:
                    Tb = 1.625
                elif b_thick == 14:
                    Tb = 1.875
                elif b_thick == 15:
                    Tb = 2.125
                Tb = Tb * 0.875
            # NPS 24
            if db  == 24:
                db = 24
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.218
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.250
                elif b_thick == 5:
                    Tb = 0.375
                elif b_thick == 6:
                    Tb = 0.562
                elif b_thick  == 7:
                    Tb = 0.687
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick == 9:
                    Tb = 0.968
                elif b_thick == 10:
                    Tb = 1.218
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                elif b_thick == 12:
                    Tb = 1.531
                elif b_thick == 13:
                    Tb = 1.812
                elif b_thick == 14:
                    Tb = 2.062
                elif b_thick == 15:
                    Tb = 2.343
                Tb = Tb * 0.875
            # NPS 26
            if db  == 26:
                db = 26
                if b_thick == 3 or b_thick  == 4:
                    Tb = 0.312
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                Tb = Tb * 0.875
            # NPS 28
            if db  == 28:
                db = 28
                if b_thick == 3 or b_thick  == 4:
                    Tb = 0.312
                elif b_thick == 6:
                    Tb = 0.625
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                Tb = Tb * 0.875
            # NPS 30
            if db  == 30:
                db = 30
                if b_thick == 1 or b_thick  == 2:
                    Tb = 0.250
                elif b_thick == 3 or b_thick  == 4:
                    Tb = 0.312
                elif b_thick == 6:
                    Tb = 0.625
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                Tb = Tb * 0.875
            # NPS 32
            if db  == 32:
                db = 32
                if b_thick == 3 or b_thick  == 4:
                    Tb = 0.312
                elif b_thick == 6:
                    Tb = 0.625
                elif b_thick == 7:
                    Tb = 0.688
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                Tb = Tb * 0.875
            # NPS 34
            if db  == 34:
                db = 34
                if b_thick == 3 or b_thick  == 4:
                    Tb = 0.312
                elif b_thick == 6:
                    Tb = 0.625
                elif b_thick == 7:
                    Tb = 0.688
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                Tb = Tb * 0.875
            # NPS 36
            if db  == 36:
                db = 36
                if b_thick == 3 or b_thick  == 4:
                    Tb = 0.312
                elif b_thick  == 8 or b_thick  == 16:
                    Tb = 0.375
                elif b_thick  == 11 or b_thick  == 17:
                    Tb = 0.5
                Tb = Tb * 0.875
            # NPS 40
            if db  >= 40:
                if b_thick == 16:
                    Tb = 0.375
                elif b_thick == 17:
                    Tb = 0.5
                elif b_thick == 18:
                    Tb = 1
                Tb = Tb * 0.875


            # If this condition is not satisfied
            # "Tb not referenced" error occurs
            B = float(request.POST['BAngle'])
            d1 = (db - 2*(Tb-c))/math.sin(math.radians(B))
            d2 = (Tb - c) + (th-c) + d1/2
            if d2 > d1:
                d2 = d2
            else:
                d2 = d1
            # min header and branch pressure design thickness
            BMaterial = float(request.POST['BranchMaterial'])
            Temp = float(request.POST['temp'])
            Sb = float(request.POST['BStress'])
            Sh = float(request.POST['HStress'])
            if Temp < 1500:
                W = 1
            else:
                W = 0.5
            Y = 0.4
            HeadMaterial = int(request.POST['HeadMaterial'])
            BranchConstruction = int(request.POST['BranchConstruction'])
            HeadConstruction = int(request.POST['HeadConstruction'])
            if HeadConstruction or BranchConstruction == 1:
                Eh = Eb = 1
            elif HeadConstruction or BranchConstruction == 2:
                Eh = Eb = 0.95
            elif HeadConstruction or BranchConstruction == 3:
                Eh = Eb = 0.85
            elif HeadConstruction or BranchConstruction == 4:
                Eh = Eb = 0.6
            P = float(request.POST['BRpsi'])
            # Min header pressure design thickness
            thp = (P * dh)/(2*((Sh*W*Eh)+(P*Y)))
            # Min branch pressure design thickness
            tbp = (P * db)/(2*((Sb*W*Eb)+(P*Y)))
            # thp = 0.1251969
            # Required reinforcement area  
            A1 = thp * d1 * (2 - math.sin(math.radians(B))) 
            # Area resulting from excess thickness in header pipe 
            A2 = (2*d2 - d1)*(th - thp - c) 
            # Height of reinforcement zone outside run pipe 
            # Minimum and available thicknss of header
            Trm = float(request.POST['min_r'])
            Trm_unit = str(request.POST['min_r_unit'])
            Tra = float(request.POST['avail_r'])
            Tra_unit = str(request.POST['avail_r_unit'])
            if Trm_unit == "mm":
                Tr = Trm/25.4
            elif Trm_unit == inch:
                Tr = Trm
            L41 = 2.5 * (th - c)
            L42 = 2.5*(Tb - c) + Tr 
            if L41 < L42:
                L4 = L41
            else:
                L4 = L42
            # Area resulting from excess thickness in branch pipe
            A3 = 2*L4*(Tb - tbp - c)/math.sin(math.radians(B))
            d1 = round(d1, 2)

            return render(request, "index.html", {'test':d1, 'test1':thp, 'test2':A1})
        
        else:
            # Redirect back to the same page if the data
            # was invalid
            return render(request, "index.html", {'form':details})
    else:
        form = ReinforcementForm()
        return render(request, "index.html", {'form':form})
