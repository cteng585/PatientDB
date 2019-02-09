import datetime
import itertools
import os
# TODO
# Come up with some sort of alert system? Maybe a way to email? HTTP format for patients?

# TODO:
# 1) Figure out a way to edit the patient comments in an intuitive manner.
#	Should be able to view the note, delete the note, edit the note
# 2) Create list of cardiotoxic drugs (Appendix 2 HCM Protocol)
# 3) Create list of Oral SoC drugs
# 4) Make a wrapper for user inputs to handle bool vs int vs datetime vs string
# 5) Make a way to pull a specific patient subset
# 6) Export to TSV/CSV
# 7) Import from TSV/CSV
# 8) Make prescreening work
class Patient(object):
	def __init__(self, name, age, sex, SBP, DBP, NYHA, LVEF, dateECHO, pastToxicCV, NTproBNP, language, 
					LVIDd=None, height=None, CAD=None, percentStenosis=None, hypertrophicCM=None, amyloidosis=None,
						sarcoidosis=None, congenitalHD=None, Asian=None, 
					lastHospitalHF=None, malignancies=None, stageCKD=None, HDSupport=None, afib=None, NIV=None, 
						lastACS=None, lastStroke=None, lastTIA=None, lastCardiacIntervention=None, 
						lastDeviceInsertion=None, valvularDisease=None, infiltrativeCM=None, myocarditis=None, 
						pericarditis=None, severeVArrhythmia=None, antiarrhythmics=None, symptomBrady=None, eGFR=None, 
						TBL=None, ALT=None, AST=None, severeComorbid=None, majorTransplant=None,
					weight=None, IVSd=None, restLVOTPG=None, valsalvaLVOTPG=None, postExerciseLVOTPG=None, O2Saturation=None, 
						QTcF=None, CPETCapable=None, RER=None, exerciseLimited=None, aorticValveStenosis=None, Fabry=None, 
						Noonan=None, lastSyncope=None, lastSVT=None, lastSCD=None, lastICDDischarge=None, pAFib=None, 
						anticoagulant=None, rateControlled=None, lastExclusionaryMedication=None, 
						lastExclusionaryComboTreatment=None, lastCardiacDrugAdjustment=None, lastSeptalReduction=None, 
						successfulSeptalReduction=None, HIV=None, hepC=None, hepB=None):
		self.characteristics = dict()
		self.characteristics['basics'] = {	'ID': 'Basic', 
											'name': name,
											'age': age, 
											'sex': sex, 
											'SBP': SBP, 
											'DBP': DBP, 
											'NYHA': NYHA,
											'LVEF': LVEF,
											'dateECHO': dateECHO,
											'pastToxicCV': pastToxicCV, 
											'NTproBNP': NTproBNP, 
											'language': language
		}
		# self.notes = notes
		self.characteristics['dcm'] = {	'ID': 'DCM', 
										'LVIDd': LVIDd,
										'height': height,
										'CAD': CAD,
										'percentStenosis': percentStenosis,
										'hypertrophicCM': hypertrophicCM, 
										'amyloidosis': amyloidosis,
										'sarcoidosis': sarcoidosis, 
										'congenitalHD': congenitalHD, 
										'Asian': Asian,
										'eligible': None
		}
		self.characteristics['amgen'] = {	'ID': 'AMGEN', 
											'lastHospitalHF': lastHospitalHF, 					
											'malignancies': malignancies,		# Dict of malignancies and their dates
											'severeComorbid': severeComorbid, 
											'lastDeviceInsertion': lastDeviceInsertion, 
											'lastCardiacIntervention': lastCardiacIntervention, 
											'eGFR': eGFR, 
											'stageCKD': stageCKD,
											'HDSupport': HDSupport, 
											'afib': afib,
											'NIV': NIV, 
											'lastACS': lastACS, 
											'lastStroke': lastStroke, 
											'lastTIA': lastTIA, 
											'valvularDisease': valvularDisease,
											'hypertrophicCM': hypertrophicCM, 
											'infiltrativeCM': infiltrativeCM, 
											'myocarditis': myocarditis, 
											'pericarditis': pericarditis, 
											'congenitalHD': congenitalHD, 
											'severeVArrhythmia': severeVArrhythmia, 
											'antiarrhythmics': antiarrhythmics, 
											'symptomBrady': symptomBrady,
											'TBL': TBL, 
											'ALT': ALT, 
											'AST': AST, 
											'majorTransplant': majorTransplant,
											'eligible': None
		}
		self.characteristics['explorer'] = {	'ID': 'MYK-EXPLORER',
												'weight': weight, 
												'IVSd': IVSd,
												'restLVOTPG': restLVOTPG,
												'valsalvaLVOTPG': valsalvaLVOTPG, 
												'postExerciseLVOTPG': postExerciseLVOTPG, 
												'O2Saturation': O2Saturation, 
												'QTcF': QTcF, 
												'CPETCapable': CPETCapable, 
												'RER': RER, 
												'exerciseLimited': exerciseLimited, 
												'CAD': CAD, 
												'percentStenosis': percentStenosis, 
												'aorticValveStenosis': aorticValveStenosis, 
												'malignancies': malignancies, 
												'severeComorbid': severeComorbid, 
												'lastDeviceInsertion': lastDeviceInsertion, 
												'Fabry': Fabry, 
												'infiltrativeCM': infiltrativeCM, 
												'Noonan': Noonan, 
												'lastSyncope': lastSyncope, 
												'lastSVT': lastSVT, 
												'lastSCD': lastSCD, 
												'lastICDDischarge': lastICDDischarge, 
												'pAFib': pAFib, 
												'anticoagulant': anticoagulant, 
												'rateControlled': rateControlled, 
												'lastExclusionaryMedication': lastExclusionaryMedication, 
												'lastExclusionaryComboTreatment': lastExclusionaryComboTreatment, 
												'lastCardiacDrugAdjustment': lastCardiacDrugAdjustment, 
												'lastSeptalReduction': lastSeptalReduction, 
												'successfulSeptalReduction': successfulSeptalReduction, 
												'TBL': TBL, 
												'ALT': ALT, 
												'AST': AST, 
												'eGFR': eGFR, 
												'HIV': HIV, 
												'hepC': hepC, 
												'hepB': hepB, 
												'eligible': None
		}

	def updateCharacteristics(self, infoType):
		os.system('clear')
		if (infoType == 'basics'):
			return updateBasics(self)
		elif (infoType == 'amgen'):
			return updateAMGEN(self)
		elif (infoType == 'dcm'):
			return updateDCM(self)
		elif (infoType == 'explorer'):
			return updateEXPLORER(self, infoType)

class PatientDB:
	def __init__(self):
		self.patientDB = dict()

	def addPatient(self, MRN, patient):
		self.patientDB[MRN] = patient

	def removePatient(self, MRN):
		del self.patientDB[MRN]

	def getPatient(self, MRN):
		return self.patientDB[MRN]

	def getStudyPatients(study):
		studyList = dict()
		try:
			for MRN in self.patientDB.keys():
				if (self.patientDB[MRN].characteristics[study]['eligible'] == True):
					studyList[MRN] = self.patientDB[MRN]
			return studyList
		except KeyError:
			print "That study doesn't appear to exist in the database"

def updateBasics(patient):
	os.system('clear')
	printHeader()
	keys = range(1, 12)
	basicsValues = ['name', 'age', 'sex', 'SBP', 'DBP', 'NYHA', 'LVEF', 'dateECHO', 'pastToxicCV', 'NTproBNP', 'language']
	optionDict = dict(itertools.izip(keys, basicsValues))
	print '[ 1 ] Name:', patient.characteristics['basics']['name']
	print '[ 2 ] Age:', patient.characteristics['basics']['age']
	print '[ 3 ] Sex:', patient.characteristics['basics']['sex']
	print '[ 4 ] Systolic Blood Pressure:', patient.characteristics['basics']['SBP']
	print '[ 5 ] Diastolic Blood Pressure:', patient.characteristics['basics']['DBP']
	print '[ 6 ] NYHA Class:', patient.characteristics['basics']['NYHA']
	print '[ 7 ] Most recent LVEF measurement:', patient.characteristics['basics']['LVEF']
	print '[ 8 ] Date of most recent ECHO:', patient.characteristics['basics']['dateECHO']
	print '[ 9 ] Cardiotoxic Drug Exposure (T/F):', patient.characteristics['basics']['pastToxicCV']
	print '[ 10 ] NT-proBNP:', patient.characteristics['basics']['NTproBNP']
	print '[ 11 ] Preferred Language: ', patient.characteristics['basics']['language']
	print '[ 12 ] Exit'
	option = userInput("Choose a value to edit: ", 'int')
	while (option in keys):
		if (option in [2, 4, 5, 6, 7, 10]):
			newValue = userInput("Enter new value: ", 'int')
		elif (option in [9]):
			newValue = userInput("Enter new value: ", 'bool')	
		elif (option in [1, 3, 11]):
			newValue = userInput("Enter new value: ", 'str')
		elif (option in [8]):
			newValue = userInput("Enter new value: ", 'date')
		patient.characteristics['basics'][optionDict[option]] = newValue
		printHeader()
		os.system('clear')
		print '[ 1 ] Name:', patient.characteristics['basics']['name']
		print '[ 2 ] Age:', patient.characteristics['basics']['age']
		print '[ 3 ] Sex:', patient.characteristics['basics']['sex']
		print '[ 4 ] Systolic Blood Pressure:', patient.characteristics['basics']['SBP']
		print '[ 5 ] Diastolic Blood Pressure:', patient.characteristics['basics']['DBP']
		print '[ 6 ] NYHA Class:', patient.characteristics['basics']['NYHA']
		print '[ 7 ] Most recent LVEF measurement:', patient.characteristics['basics']['LVEF']
		print '[ 8 ] Date of most recent ECHO:', patient.characteristics['basics']['dateECHO']
		print '[ 9 ] Cardiotoxic Drug Exposure (T/F):', patient.characteristics['basics']['pastToxicCV']
		print '[ 10 ] NT-proBNP:', patient.characteristics['basics']['NTproBNP']
		print '[ 11 ] Preferred Language:', patient.characteristics['basics']['language']
		print '[ 12 ] Exit'
		option = userInput("Choose a value to edit: ", 'int')

def updateDCM(patient):
	os.system('clear')
	printHeader()
	keys = range(1, 11)
	dcmValues = ['LVIDd', 'height', 'CAD', 'percentStenosis', 'hypertrophicCM', 'amyloidosis', 'sarcoidosis', 'congenitalHD', 'Asian', 'eligible']
	optionDict = dict(itertools.izip(keys, dcmValues))
	print '[ 1 ] LVIDd:', patient.characteristics['dcm']['LVIDd']
	print '[ 2 ] Height:', patient.characteristics['dcm']['height']
	print '[ 3 ] CAD (T/F):', patient.characteristics['dcm']['CAD']
	print '[ 4 ] Percent Stenosis:', patient.characteristics['dcm']['percentStenosis']
	print '[ 5 ] Hypertrophic CM (T/F):', patient.characteristics['dcm']['hypertrophicCM']
	print '[ 6 ] Amyloidosis (T/F):', patient.characteristics['dcm']['amyloidosis']
	print '[ 7 ] Sarcoidosis (T/F):', patient.characteristics['dcm']['sarcoidosis']
	print '[ 8 ] Congenital Heart Disease (T/F):', patient.characteristics['dcm']['congenitalHD']
	print '[ 9 ] Asian Ethnicity (T/F):', patient.characteristics['dcm']['Asian']
	print '[ 10 ] Eligible for Study:', patient.characteristics['dcm']['eligible']
	print '[ 11 ] Exit'
	option = userInput("Choose a value to edit: ", 'int')
	while (option in keys):
		if (option in [1, 2, 4]):
			newValue = userInput("Enter new value: ", 'int')
		elif (option in [3, 5, 6, 7, 8, 9, 10]):
			newValue = userInput("Enter new value: ", 'bool')
		patient.characteristics['dcm'][optionDict[option]] = newValue
		os.system('clear')
		printHeader()
		print '[ 1 ] LVIDd:', patient.characteristics['dcm']['LVIDd']
		print '[ 2 ] Height:', patient.characteristics['dcm']['height']
		print '[ 3 ] CAD (T/F):', patient.characteristics['dcm']['CAD']
		print '[ 4 ] Percent Stenosis:', patient.characteristics['dcm']['percentStenosis']
		print '[ 5 ] Hypertrophic CM (T/F):', patient.characteristics['dcm']['hypertrophicCM']
		print '[ 6 ] Amyloidosis (T/F):', patient.characteristics['dcm']['amyloidosis']
		print '[ 7 ] Sarcoidosis (T/F):', patient.characteristics['dcm']['sarcoidosis']
		print '[ 8 ] Congenital Heart Disease (T/F):', patient.characteristics['dcm']['congenitalHD']
		print '[ 9 ] Asian Ethnicity (T/F):', patient.characteristics['dcm']['Asian']
		print '[ 10 ] Eligible for Study:', patient.characteristics['dcm']['eligible']
		print '[ 11 ] Exit'
		option = userInput("Choose a value to edit: ", 'int')

def updateAMGEN(patient):
	os.system('clear')
	printHeader()
	keys = range(1, 28)
	amgenValues = [	'lastHospitalHF', 'malignancies', 'stageCKD', 'HDSupport', 'afib', 'NIV', 'lastACS', 
					'lastStroke', 'lastTIA', 'lastCardiacIntervention', 'lastDeviceInsertion', 'valvularDisease',
					'hypertrophicCM', 'infiltrativeCM', 'myocarditis', 'pericarditis', 'congenitalHD', 
					'severeVArrhythmia', 'antiarrhythmics', 'symptomBrady', 'eGFR', 'TBL', 'ALT', 'AST', 
					'severeComorbid', 'majorTransplant', 'eligible']	
	optionDict = dict(itertools.izip(keys, amgenValues))
	print '[ 1 ] Most recent hospitalization for HF: ', patient.characteristics['amgen']['lastHospitalHF']
	print '[ 2 ] Malignancies (T/F): ', patient.characteristics['amgen']['malignancies']
	print '[ 3 ] Stage of CKD: ', patient.characteristics['amgen']['stageCKD']
	print '[ 4 ] On Hemodynamic Support (T/F): ', patient.characteristics['amgen']['HDSupport']
	print '[ 5 ] In Atrial Fibrillation (T/F): ', patient.characteristics['amgen']['afib']
	print '[ 6 ] On Non-invasive Ventilation (T/F): ', patient.characteristics['amgen']['NIV']
	print '[ 7 ] Most recent ACS: ', patient.characteristics['amgen']['lastACS']
	print '[ 8 ] Most recent Stroke: ', patient.characteristics['amgen']['lastStroke']
	print '[ 9 ] Most recent Transischemic Attack: ', patient.characteristics['amgen']['lastTIA']
	print '[ 10 ] Most recent Cardiac Intervention: ', patient.characteristics['amgen']['lastCardiacIntervention']
	print '[ 11 ] Most recent Cardiac Device Insertion: ', patient.characteristics['amgen']['lastDeviceInsertion']
	print '[ 12 ] Any severe, uncorrected Valvular Disease (T/F): ', patient.characteristics['amgen']['valvularDisease']
	print '[ 13 ] Hypertrophic Cardiomyopathy Diagnosis (T/F): ', patient.characteristics['amgen']['hypertrophicCM']
	print '[ 14 ] Infiltrative Cardiomyopathy Diagnosis (T/F): ', patient.characteristics['amgen']['infiltrativeCM']
	print '[ 15 ] Active Myocarditis (T/F): ', patient.characteristics['amgen']['myocarditis']
	print '[ 16 ] Constrictive Pericarditis (T/F): ', patient.characteristics['amgen']['pericarditis']
	print '[ 17 ] Congenital Heart Disease (T/F): ', patient.characteristics['amgen']['congenitalHD']
	print '[ 18 ] Severe Ventricular Arrhythmia (T/F): ', patient.characteristics['amgen']['severeVArrhythmia']
	print '[ 19 ] Any exclusionary antiarrhythmics (T/F): ', patient.characteristics['amgen']['antiarrhythmics']
	print '[ 20 ] Symptomatic Bradycardia or 2nd or 3rd degree Heart Block without a pacemaker (T/F): ', patient.characteristics['amgen']['symptomBrady']
	print '[ 21 ] eGFR: ', patient.characteristics['amgen']['eGFR']
	print '[ 22 ] TBL: ', patient.characteristics['amgen']['TBL']
	print '[ 23 ] AST: ', patient.characteristics['amgen']['ALT']
	print '[ 24 ] ALT: ', patient.characteristics['amgen']['AST']
	print '[ 25 ] Severe comorbidities expected to reduce life expectancy to < 2 years (T/F): ', patient.characteristics['amgen']['severeComorbid']
	print '[ 26 ] Any major organ transplant (T/F): ', patient.characteristics['amgen']['majorTransplant']
	print '[ 27 ] Eligible for Study:', patient.characteristics['amgen']['eligible']
	print '[ 28 ] Exit'
	option = userInput("Choose a value to edit: ", 'int')
	while (option in keys):
		if (option in [3, 21, 22, 23, 24]):
			newValue = userInput("Enter new value: ", 'int')
		elif (option in [2, 4, 5, 6, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27]):
			newValue = userInput("Enter new value: ", 'bool')
		elif (option in [1, 7, 8, 9, 10, 11]):
			newValue = userInput("Enter new value: ", 'date')
		patient.characteristics['amgen'][optionDict[option]] = newValue
		printHeader()
		os.system('clear')
		print '[ 1 ] Most recent hospitalization for HF: ', patient.characteristics['amgen']['lastHospitalHF']
		print '[ 2 ] Malignancies (T/F): ', patient.characteristics['amgen']['malignancies']
		print '[ 3 ] Stage of CKD: ', patient.characteristics['amgen']['stageCKD']
		print '[ 4 ] On Hemodynamic Support (T/F): ', patient.characteristics['amgen']['HDSupport']
		print '[ 5 ] In Atrial Fibrillation (T/F): ', patient.characteristics['amgen']['afib']
		print '[ 6 ] On Non-invasive Ventilation (T/F): ', patient.characteristics['amgen']['NIV']
		print '[ 7 ] Most recent ACS: ', patient.characteristics['amgen']['lastACS']
		print '[ 8 ] Most recent Stroke: ', patient.characteristics['amgen']['lastStroke']
		print '[ 9 ] Most recent Transischemic Attack: ', patient.characteristics['amgen']['lastTIA']
		print '[ 10 ] Most recent Cardiac Intervention: ', patient.characteristics['amgen']['lastCardiacIntervention']
		print '[ 11 ] Most recent Cardiac Device Insertion: ', patient.characteristics['amgen']['lastDeviceInsertion']
		print '[ 12 ] Any severe, uncorrected Valvular Disease (T/F): ', patient.characteristics['amgen']['valvularDisease']
		print '[ 13 ] Hypertrophic Cardiomyopathy Diagnosis (T/F): ', patient.characteristics['amgen']['hypertrophicCM']
		print '[ 14 ] Infiltrative Cardiomyopathy Diagnosis (T/F): ', patient.characteristics['amgen']['infiltrativeCM']
		print '[ 15 ] Active Myocarditis (T/F): ', patient.characteristics['amgen']['myocarditis']
		print '[ 16 ] Constrictive Pericarditis (T/F): ', patient.characteristics['amgen']['pericarditis']
		print '[ 17 ] Congenital Heart Disease (T/F): ', patient.characteristics['amgen']['congenitalHD']
		print '[ 18 ] Severe Ventricular Arrhythmia (T/F): ', patient.characteristics['amgen']['severeVArrhythmia']
		print '[ 19 ] Any exclusionary antiarrhythmics (T/F): ', patient.characteristics['amgen']['antiarrhythmics']
		print '[ 20 ] Symptomatic Bradycardia or 2nd or 3rd degree Heart Block without a pacemaker (T/F): ', patient.characteristics['amgen']['symptomBrady']
		print '[ 21 ] eGFR: ', patient.characteristics['amgen']['eGFR']
		print '[ 22 ] TBL: ', patient.characteristics['amgen']['TBL']
		print '[ 23 ] AST: ', patient.characteristics['amgen']['ALT']
		print '[ 24 ] ALT: ', patient.characteristics['amgen']['AST']
		print '[ 25 ] Severe comorbidities expected to reduce life expectancy to < 2 years (T/F): ', patient.characteristics['amgen']['severeComorbid']
		print '[ 26 ] Any major organ transplant (T/F): ', patient.characteristics['amgen']['majorTransplant']
		print '[ 27 ] Eligible for Study:', patient.characteristics['amgen']['eligible']
		print '[ 28 ] Exit'
		option = userInput("Choose a value to edit: ", 'int')

def updateEXPLORER(patient, study):
	os.system('clear')
	printHeader()
	# keys = [key for key in patient.characteristics[study].keys() if key not in ['ID', 'eligible']]
	keys = range(1, 40)
	explorerValues = [ 'weight', 'IVSd', 'restLVOTPG', 'valsalvaLVOTPG', 'postExerciseLVOTPG', 'O2Saturation', 'QTcF',
						'CPETCapable', 'RER', 'exerciseLimited', 'CAD', 'percentStenosis', 'aorticValveStenosis', 'malignancies', 
						'severeComorbid', 'lastDeviceInsertion', 'Fabry', 'infiltrativeCM', 'Noonan', 'lastSyncope', 'lastSVT', 
						'lastSCD', 'lastICDDischarge', 'pAFib', 'anticoagulant', 'rateControlled', 'lastExclusionaryMedication',
						'lastExclusionaryComboTreatment', 'lastCardiacDrugAdjustment', 'lastSeptalReduction', 'successfulSeptalReduction', 
						'TBL', 'ALT', 'AST', 'eGFR', 'HIV', 'hepC', 'hepB', 'eligible']
	optionDict = dict(itertools.izip(keys, explorerValues))
	print '[ 1 ] Weight (kgs):', patient.characteristics['explorer']['weight']
	print '[ 2 ] IVSd (mm):', patient.characteristics['explorer']['IVSd']
	print '[ 3 ] LVOT Peak Gradient at rest:', patient.characteristics['explorer']['restLVOTPG']
	print '[ 4 ] LVOT Peak Gradient during Valsalva:', patient.characteristics['explorer']['valsalvaLVOTPG']
	print '[ 5 ] LVOT Peak Gradient after exercise:', patient.characteristics['explorer']['postExerciseLVOTPG']
	print '[ 6 ] Oxygen Saturation:', patient.characteristics['explorer']['O2Saturation']
	print '[ 7 ] QTcF/QTC:', patient.characteristics['explorer']['QTcF']
	print '[ 8 ] Able to perform upright CPET (T/F):', patient.characteristics['explorer']['CPETCapable']
	print '[ 9 ] RER:', patient.characteristics['explorer']['RER']
	print '[ 10 ] Medical condition that limits exercise (T/F):', patient.characteristics['explorer']['exerciseLimited']
	print '[ 11 ] Coronary Artery Disease (T/F):', patient.characteristics['explorer']['CAD']
	print '[ 12 ] Percent Stenosis in any epicardial coronary artery:', patient.characteristics['explorer']['percentStenosis']
	print '[ 13 ] Aortic Valve Stenosis (T/F):', patient.characteristics['explorer']['aorticValveStenosis']
	print '[ 14 ] Malignancies (T/F): ', patient.characteristics['explorer']['malignancies']
	print '[ 15 ] Severe comorbidities expected to interfere with ability to complete the study (T/F):', patient.characteristics['explorer']['severeComorbid']
	print '[ 16 ] Most recent Cardiac Device Insertion:', patient.characteristics['explorer']['lastDeviceInsertion']
	print '[ 17 ] Fabry Disease Diagnosis (T/F):', patient.characteristics['explorer']['Fabry']
	print '[ 18 ] Infiltrative Cardiomyopathy Diagnosis (e.g. amyloidosis) (T/F):', patient.characteristics['explorer']['infiltrativeCM']
	print '[ 19 ] Noonan Disease Diagnosis (T/F):', patient.characteristics['explorer']['Noonan']
	print '[ 20 ] Last Syncope Episode:', patient.characteristics['explorer']['lastSyncope']
	print '[ 21 ] Last Sustained Ventricular Tachycardia Episode:', patient.characteristics['explorer']['lastSVT']
	print '[ 22 ] Last Sudden Cardiac Death:', patient.characteristics['explorer']['lastSCD']
	print '[ 23 ] Last ICD Discharge:', patient.characteristics['explorer']['lastICDDischarge']
	print '[ 24 ] Paroxysmal or Intermittent Atrial Fibrillation (T/F):', patient.characteristics['explorer']['pAFib']
	print '[ 25 ] On Anticoagulant Therapy (T/F):', patient.characteristics['explorer']['anticoagulant']
	print '[ 26 ] Rate Controlled (T/F):', patient.characteristics['explorer']['rateControlled']
	print '[ 27 ] Treatment in the past 14 days with, or Planned treatment with Disopyramide, Ranolazine, CYP 2C19 inhibitor, Strong CYP 3A4 inhibitor, or St. Johns Wort (T/F): ', patient.characteristics['explorer']['lastExclusionaryMedication']
	print '[ 28 ] Treatment in the past 14 days with, or Planned treatment with: beta-blockers + verapamil or beta-blockers + diltiazem (T/F): ', patient.characteristics['explorer']['lastExclusionaryComboTreatment']
	print '[ 29 ] If treated with Beta-blockers, verapamil, or diltiazem, any anticipated dose adjustment or prior dose adjustment in the past 14 days (T/F):', patient.characteristics['explorer']['lastCardiacDrugAdjustment']
	print '[ 30 ] Last Septal Reduction Procedure:', patient.characteristics['explorer']['lastSeptalReduction']
	print '[ 31 ] Successful Septal Reduction Procedure:', patient.characteristics['explorer']['successfulSeptalReduction']
	print '[ 32 ] TBL:', patient.characteristics['explorer']['TBL']
	print '[ 33 ] ALT:', patient.characteristics['explorer']['ALT']
	print '[ 34 ] AST:', patient.characteristics['explorer']['AST']
	print '[ 35 ] eGFR:', patient.characteristics['explorer']['eGFR']
	print '[ 36 ] HIV (T/F):', patient.characteristics['explorer']['HIV']
	print '[ 37 ] Hepatitis C Virus (T/F):', patient.characteristics['explorer']['hepC']
	print '[ 38 ] Hepatitis B Virus (T/F):', patient.characteristics['explorer']['hepB']
	print '[ 39 ] Eligible for Study:', patient.characteristics['explorer']['eligible']
	print '[ 40 ] Exit'
	option = userInput("Choose a value to edit: ", 'int')
	while (option in optionDict.keys()):
		if (option in [1, 2, 3, 4, 5, 6, 7, 9, 12, 32, 33, 34, 35]):
			newValue = userInput("Enter new value: ", 'int')
		elif (option in [8, 10, 11, 13, 14, 15, 16, 17, 18, 19, 24, 25, 26, 27, 28, 29, 31, 36, 37, 38, 39]):
			newValue = userInput("Enter new value: ", 'bool')
		elif (option in [20, 21, 22, 23, 30]):
			newValue = userInput("Enter new value: ", 'date')
		patient.characteristics['explorer'][optionDict[option]] = newValue
		printHeader()
		os.system('clear')
		print '[ 1 ] Weight (kgs):', patient.characteristics['explorer']['weight']
		print '[ 2 ] IVSd (mm):', patient.characteristics['explorer']['IVSd']
		print '[ 3 ] LVOT Peak Gradient at rest:', patient.characteristics['explorer']['restLVOTPG']
		print '[ 4 ] LVOT Peak Gradient during Valsalva:', patient.characteristics['explorer']['valsalvaLVOTPG']
		print '[ 5 ] LVOT Peak Gradient after exercise:', patient.characteristics['explorer']['postExerciseLVOTPG']
		print '[ 6 ] Oxygen Saturation:', patient.characteristics['explorer']['O2Saturation']
		print '[ 7 ] QTcF/QTC:', patient.characteristics['explorer']['QTcF']
		print '[ 8 ] Able to perform upright CPET (T/F):', patient.characteristics['explorer']['CPETCapable']
		print '[ 9 ] RER:', patient.characteristics['explorer']['RER']
		print '[ 10 ] Medical condition that limits exercise (T/F):', patient.characteristics['explorer']['exerciseLimited']
		print '[ 11 ] Coronary Artery Disease (T/F):', patient.characteristics['explorer']['CAD']
		print '[ 12 ] Percent Stenosis in any epicardial coronary artery:', patient.characteristics['explorer']['percentStenosis']
		print '[ 13 ] Aortic Valve Stenosis (T/F):', patient.characteristics['explorer']['aorticValveStenosis']
		print '[ 14 ] Malignancies (T/F): ', patient.characteristics['explorer']['malignancies']
		print '[ 15 ] Severe comorbidities expected to interfere with ability to complete the study (T/F):', patient.characteristics['explorer']['severeComorbid']
		print '[ 16 ] Most recent Cardiac Device Insertion:', patient.characteristics['explorer']['lastDeviceInsertion']
		print '[ 17 ] Fabry Disease Diagnosis (T/F):', patient.characteristics['explorer']['Fabry']
		print '[ 18 ] Infiltrative Cardiomyopathy Diagnosis (e.g. amyloidosis) (T/F):', patient.characteristics['explorer']['infiltrativeCM']
		print '[ 19 ] Noonan Disease Diagnosis (T/F):', patient.characteristics['explorer']['Noonan']
		print '[ 20 ] Last Syncope Episode:', patient.characteristics['explorer']['lastSyncope']
		print '[ 21 ] Last Sustained Ventricular Tachycardia Episode:', patient.characteristics['explorer']['lastSVT']
		print '[ 22 ] Last Sudden Cardiac Death:', patient.characteristics['explorer']['lastSCD']
		print '[ 23 ] Last ICD Discharge:', patient.characteristics['explorer']['lastICDDischarge']
		print '[ 24 ] Paroxysmal or Intermittent Atrial Fibrillation (T/F):', patient.characteristics['explorer']['pAFib']
		print '[ 25 ] On Anticoagulant Therapy (T/F):', patient.characteristics['explorer']['anticoagulant']
		print '[ 26 ] Rate Controlled (T/F):', patient.characteristics['explorer']['rateControlled']
		print '[ 27 ] Treatment in the past 14 days with, or Planned treatment with Disopyramide, Ranolazine, CYP 2C19 inhibitor, Strong CYP 3A4 inhibitor, or St. Johns Wort (T/F): ', patient.characteristics['explorer']['lastExclusionaryMedication']
		print '[ 28 ] Treatment in the past 14 days with, or Planned treatment with: beta-blockers + verapamil or beta-blockers + diltiazem (T/F): ', patient.characteristics['explorer']['lastExclusionaryComboTreatment']
		print '[ 29 ] If treated with Beta-blockers, verapamil, or diltiazem, any anticipated dose adjustment or prior dose adjustment in the past 14 days (T/F):', patient.characteristics['explorer']['lastCardiacDrugAdjustment']
		print '[ 30 ] Last Septal Reduction Procedure:', patient.characteristics['explorer']['lastSeptalReduction']
		print '[ 31 ] Successful Septal Reduction Procedure:', patient.characteristics['explorer']['successfulSeptalReduction']
		print '[ 32 ] TBL:', patient.characteristics['explorer']['TBL']
		print '[ 33 ] ALT:', patient.characteristics['explorer']['ALT']
		print '[ 34 ] AST:', patient.characteristics['explorer']['AST']
		print '[ 35 ] eGFR:', patient.characteristics['explorer']['eGFR']
		print '[ 36 ] HIV (T/F):', patient.characteristics['explorer']['HIV']
		print '[ 37 ] Hepatitis C Virus (T/F):', patient.characteristics['explorer']['hepC']
		print '[ 38 ] Hepatitis B Virus (T/F):', patient.characteristics['explorer']['hepB']
		print '[ 39 ] Eligible for Study:', patient.characteristics['explorer']['eligible']
		print '[ 40 ] Exit'
		option = userInput("Choose a value to edit: ", 'int')

def checkDCM(database, MRN): 
	height = range(137, 199)
	male_threshold = [None]*15 + [52.0, 52.2, 52.4, 52.6, 52.8, 53.0, 53.1, 53.3, 53.5, 53.7, 53.9, 54.1, 
								  54.3, 54.5, 54.7, 54.9, 55.0, 55.2, 55.4, 55.6, 55.8, 56.0, 56.2, 56.3, 
								  56.5, 56.7, 56.9, 57.1, 57.3, 57.4, 57.6, 57.8, 58.0, 58.2, 58.3, 58.5, 
								  58.7, 58.9, 59.1, 59.2, 59.4, 59.6, 59.8, 59.9, 60.1, 60.3, 60.5]
	female_threshold = [46.8, 47.0, 47.2, 47.3, 47.5, 47.7, 47.8, 48.0, 48.2, 48.3, 48.5, 48.6, 48.8, 49.0, 
						49.1, 49.3, 49.5, 49.6, 49.8, 49.9, 50.1, 50.3, 50.4, 50.6, 50.7, 50.9, 51.0, 51.2, 
						51.3, 51.5, 51.7, 51.8, 52.0, 52.1, 52.3, 52.4, 52.6, 52.7, 52.9, 53.0, 53.2, 53.3, 
						53.5, 53.6, 53.8, 53.9, 54.1] + [None]*15
	DCMThresholds = {	'M': dict(itertools.izip(height, male_threshold)), 
						'F': dict(itertools.izip(height, female_threshold))
	}
	if ((database.patientDB[MRN].characteristics['basics']['LVEF'] < 50) and 
		(database.patientDB[MRN].characteristics['basics']['pastToxicCV'] == False) and 
		(database.patientDB[MRN].characteristics['basics']['SBP'] < 180 and database.patientDB[MRN].characteristics['basics']['DBP'] < 120) and 
		(database.patientDB[MRN].characteristics['dcm']['LVIDd'] > DCMThresholds[database.patientDB[MRN].characteristics['basics']['sex']][database.patientDB[MRN].characteristics['dcm']['height']]) and 
		((database.patientDB[MRN].characteristics['dcm']['CAD'] == False) or (database.patientDB[MRN].characteristics['dcm']['percentStenosis'] < 50)) and 
		(all(dx is False for dx in [database.patientDB[MRN].characteristics['dcm']['hypertrophicCM'], database.patientDB[MRN].characteristics['dcm']['amyloidosis'], database.patientDB[MRN].characteristics['dcm']['sarcoidosis']])) and 
		(database.patientDB[MRN].characteristics['dcm']['congenitalHD'] == False) and 
		(database.patientDB[MRN].characteristics['dcm']['Asian'] == False)
		):
		database.patientDB[MRN].characteristics['dcm']['eligible'] = True
		return True
	else:
		database.patientDB[MRN].characteristics['dcm']['eligible'] = False
		return False

# Also routinely scheduled IV
# Check if on HD?
# https://emedicine.medscape.com/article/304235-overview
def checkAMGEN(database, MRN):
	if ((database.patientDB[MRN].characteristics['basics']['LVEF'] < 35) and 
		(database.patientDB[MRN].characteristics['basics']['age'] >= 18 and database.patientDB[MRN]['basics']['age'] <=85) and 
		(database.patientDB[MRN].characteristics['basics']['SBP'] <= 140 and database.patientDB[MRN]['basics']['SBP'] >= 85) and 
		(database.patientDB[MRN].characteristics['basics']['DBP'] <= 90) and 
		((database.patientDB[MRN].characteristics['basics']['NTproBNP'] >= 400 and database.patientDB[MRN].characteristics['amgen']['afib'] == False) or 
			(database.patientDB[MRN].characteristics['basics']['NTproBNP'] >= 1200 and database.patientDB[MRN].characteristics['amgen']['afib'] == True)) and 
		(database.patientDB[MRN].characteristics['amgen']['eGFR'] >= 20) and 
		(database.patientDB[MRN].characteristics['amgen']['NIV'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['HDSupport'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['majorTransplant'] == False) and
		(database.patientDB[MRN].characteristics['amgen']['valvularDisease'] == False) and  
		(database.patientDB[MRN].characteristics['amgen']['hypertrophicCM'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['infiltrativeCM'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['severeVArrhythmia'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['symptomBrady'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['severeComorbid'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['myocarditis'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['pericarditis'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['congenitalHD'] == False) and 
		(database.patientDB[MRN].characteristics['amgen']['lastHospitalHF'] > datetime.date.today() - datetime.timedelta(days=365)) and 
		(database.patientDB[MRN].characteristics['amgen']['lastACS'] < datetime.date.today() - datetime.timedelta(days=90)) and 
		(database.patientDB[MRN].characteristics['amgen']['lastStroke'] < datetime.date.today() - datetime.timedelta(days=90)) and 
		(database.patientDB[MRN].characteristics['amgen']['lastTIA'] < datetime.date.today() - datetime.timedelta(days=90)) and 
		(database.patientDB[MRN].characteristics['amgen']['lastCardiacIntervention'] < datetime.date.today() - datetime.timedelta(days=90)) and 
		(database.patientDB[MRN].characteristics['amgen']['lastDeviceInsertion'] < datetime.date.today() - datetime.timedelta(days=30))
		):
		database.patientDB[MRN].characteristics['amgen']['eligible'] = True
		return True
	else:
		database.patientDB[MRN].characteristics['amgen']['eligible'] = False
		return False

def queryMRN(database):
	printHeader()
	MRN = raw_input("Please enter patient MRN, \nor enter 'Exit' to exit: ")
	if (MRN.lower() == 'exit'):
		return False, -1
	elif (MRN in database.patientDB.keys()):
		return True, MRN
	else:
		return False, MRN

def createPatient(MRN):
	printHeader()
	print "New patient for MRN:", MRN
	name = userInput("Name: ", 'str')
	age = userInput("Age: ", 'int')
	sex = userInput("Sex: ", 'str')
	SBP = userInput("Systolic Blood Pressure: ", 'int')
	DBP = userInput("Diastolic Blood Pressure: ", 'int')
	NYHA = userInput("NYHA Class (1-4): ", 'int')
	LVEF = userInput("Most recent LVEF measurement: ", 'int')
	dateECHO = userInput("Date of most recent ECHO: ", 'date')
	pastToxicCV = userInput("Cardiotoxic Drug Exposure (T/F): ", 'bool')		# Flesh this out
	NTproBNP = userInput("NT-proBNP: ", 'int')
	language = userInput("Preferred Language: ", 'str')
	newPatient = Patient(name, age, sex, SBP, DBP, NYHA, LVEF, dateECHO, pastToxicCV, NTproBNP, language)
	return newPatient

# Option to remove patient
def displayEligibility(database, MRN):
	printHeader()
	print "Details for", database.patientDB[MRN].characteristics['basics']['name'], "( MRN:", MRN, ") \n"
	print '[ 1 ] Basics'
	studyIndices = range(2, len(database.patientDB[MRN].characteristics.keys()) + 1)
	studyIDs = [key for key in database.patientDB[MRN].characteristics.keys() if key != 'basics']
	optionDict = dict(zip(studyIndices, studyIDs))
	optionDict[1] = 'basics'
	optionDict[len(database.patientDB[MRN].characteristics.keys()) + 1] = 'exit'
	for idx, key in zip(studyIndices, studyIDs):
		if (database.patientDB[MRN].characteristics[key]['eligible'] == True):
			print '[', idx, ']', database.patientDB[MRN].characteristics[key]['ID'] + ":", "Eligible for Study"
		elif (database.patientDB[MRN].characteristics[key]['eligible'] == False):
			print '[', idx, ']', database.patientDB[MRN].characteristics[key]['ID'] + ":", "Not Eligible for Study"
		elif (database.patientDB[MRN].characteristics[key]['eligible'] == None):
			print '[', idx, ']', database.patientDB[MRN].characteristics[key]['ID'] + ":", "Not Screened"
	print '[', len(database.patientDB[MRN].characteristics.keys()) + 1, ']', 'Exit'
	option = userInput("\nView details? ", 'int')
	return optionDict[option]

def displayStudyList(database):
	os.system('clear')
	printHeader()
	studies = database.patientDB[database.patientDB.keys()[0]].characteristics.keys()
	for study, idx in zip(studies, range(1, len(studies) + 1)):
		print "[", idx, "]", database.patientDB[database.patientDB.keys()[0]].characteristics[study]['ID']
	uin = userInput("Which study do you want to export the patient list of? ", 'int')
	if (uin in range(1, len(studies) + 1)):
		study = studies[uin - 1]
		studyList = []
		for MRN in database.patientDB.keys():
			if (database.patientDB[MRN].characteristics[study]['eligible'] == True):
				studyList.append(database.patientDB[MRN])
		basicCriteria = [criteria for criteria in studyList[0].characteristics['basics'].keys() if criteria not in ['ID', 'eligible']]
		studyCriteria = [criteria for criteria in studyList[0].characteristics[study].keys() if criteria not in ['ID', 'eligible']]
		with open(studyList[0].characteristics[study]['ID'] + "Study List.txt", "w+") as f:
			f.write('\t'.join(basicCriteria + studyCriteria) + '\n')
			for patient in studyList:
				f.write('\t'.join([str(patient.characteristics['basics'][criteria]) for criteria in basicCriteria]) + '\t')
				f.write('\t'.join([str(patient.characteristics[study][criteria]) for criteria in studyCriteria]) + '\n')
		raw_input("Patient list exported successfully!")
		os.system('clear')
	else:
		raw_input("Sorry, that study doesn't appear to exist")
		os.system('clear')

def str2bool(s):
	s = s.lower()
	if (s in ["f", "false", "n", "no"]):
		return False
	elif (s in ["t", "true", "y", "yes"]):
		return True

def userInput(prompt, varType):
	uin = raw_input(prompt) 
	if (varType == 'bool'):
		return str2bool(uin)
	elif (varType == 'int'):
		try:
			return int(uin)
		except ValueError:
			return userInput("Value entered was not a number. Please enter a number: ", 'int')
	elif (varType == 'str'):
		return uin.upper()
	elif (varType == 'date'):
		try:
			return datetime.datetime.strptime(uin, '%x')
		except ValueError:
			return datetime.datetime.strptime(uin, '%m/%d/%Y')
		except ValueError:
			return userInput("Value entered was not a valid date. Please enter a date: ", 'date')

def printHeader():
	print " \n////////////////////////////////////////////////////////////////////"
	print "//\t _____ _           ______ _           ____________ \t  //"
	print "//\t|_   _| |          | ___ \\ |          |  _  \\ ___ \\\t  //"
	print "//\t  | | | |__   ___  | |_/ / |_   _  ___| | | | |_/ /\t  //"
	print "//\t  | | | '_ \\ / _ \\ | ___ \\ | | | |/ _ \\ | | | ___ \\\t  //"
	print "//\t  | | | | | |  __/ | |_/ / | |_| |  __/ |/ /| |_/ /\t  //"
	print "//\t  \\_/ |_| |_|\\___| \\____/|_|\\__,_|\\___|___/ \\____/ \t  //"
	print "////////////////////////////////////////////////////////////////////\n"

def mainMenu():
	printHeader()
	print "[ 1 ] Search MRN"
	print "[ 2 ] View Study Lists"
	print "[ 3 ] Exit"
	return userInput("Choose a menu item above: ", 'int')

# Prompt user for import?
# Prompt user to add patient
# Prompt user to view patient lists
def main(): 
	database = PatientDB()
	menuOption = mainMenu()
	while (menuOption != 3):
		if (menuOption == 1):
			os.system('clear')
			searchResult, MRN = queryMRN(database)
			os.system('clear')
			while (MRN != -1):
				if (searchResult):
					study = displayEligibility(database, MRN)
					os.system('clear')
					while (study != 'exit'):
						database.patientDB[MRN].updateCharacteristics(study)
						os.system('clear')
						study = displayEligibility(database, MRN)
						os.system('clear')
				else:
					newPatient = createPatient(MRN)
					database.addPatient(MRN, newPatient)
					os.system('clear')
					study = displayEligibility(database, MRN)
					os.system('clear')
					while (study != 'exit'):
						database.patientDB[MRN].updateCharacteristics(study)
						os.system('clear')
						study = displayEligibility(database, MRN)
						os.system('clear')
				searchResult, MRN = queryMRN(database)
		elif (menuOption == 2):
			displayStudyList(database)
		menuOption = mainMenu()
	print "Goodbye!"

main()
# MRNList = [line.split('\t')[0] for line in open("PatientDB.txt").readlines()]

# def getMRNList(filename):
# 	with open(filename, 'r') as f:
# 		lines = f.readlines()
# 		MRNList = []
# 		for line in lines:
# 			MRNList.append(line.split('\t')[0])
# 	return MRNList