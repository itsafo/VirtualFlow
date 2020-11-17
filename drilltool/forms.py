from django import forms


class ReinforcementForm(forms.Form):
	HeadMaterial = forms.IntegerField()
	hnpd = forms.IntegerField()
	hnpd_unit = forms.CharField()
	h_thick = forms.FloatField()	
	ch = forms.FloatField()
	h_ca_unit = forms.CharField()
	HStress = forms.FloatField()
	h_s_unit = 	forms.CharField()
		
	bnpd = forms.IntegerField()


	HeadMaterial = forms.IntegerField()
