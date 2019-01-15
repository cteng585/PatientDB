import datetime
# TODO
# Come up with some sort of alert system? Maybe a way to email? HTTP format for patients?

# Base patient
# 1) Change LVEF
# 2) Change dateECHO
class Patient(object):
	def __init__(self, name, dateAdmit, SBP, DBP, NYHA, LVEF, dateECHO, pastToxicCV, notes):
		self.basics = { 'name': name,
						'dateAdmit': dateAdmit, 
						'SBP': SBP, 
						'DBP': DBP, 
						'NYHA': NYHA,
						'LVEF': LVEF,
						'dateECHO': dateECHO,
						'pastToxicCV': pastToxicCV
		}
		self.notes = notes

	def updateCharcteristics(key, newValue):
		self.characteristics[key] = newValue

	# def updateNotes():
	# 	self.dateECHO = dateECHO

# TODO:
# 1) Figure out a way to edit the patient comments in an intuitive manner.
#	Should be able to view the note, delete the note, edit the note
# 2) Create SBP/DBP cutoffs for HTN criteria
# 3) Create LVIDd cutoffs for heights (Appendix 8 DCM Protocol)
# 4) Create list of cardiotoxic drugs (Appendix 2 HCM Protocol)
# 5) Create list of Oral SoC drugs
class DCMPatient(Patient, object):
	def __init__(self, name, dateAdmit, SBP, DBP, NYHA, LVEF, dateECHO, pastToxicCV, notes, 
					LVIDd, height, spanish, eligible):
		self.charactersDCM = { 'LVIDd': LVIDd,
								'height': height,
								'spanish': spanish,
								'eligible': eligible
			}
		super(DCMPatient, self).__init__(name, dateAdmit, SBP, DBP, NYHA, LVEF, dateECHO, 
			pastToxicCV, notes)

testDCMPatient = DCMPatient("Vivian", "Chung", "1/1/2018", 120, 80, 2, .50, "1/1/2017", False, "", 43, 160, 
	False, False)

# Includes last Transient Ischemic Attack (TIA) date
# Also routinely scheduled IV
# Check if on HD?
# https://emedicine.medscape.com/article/304235-overview
# ICD, CRT, Permanent Pacemaker, Monitoring Device 
# insertion? If so, date?
# Any notable comorbidities
class AMGENPatient(Patient, object):
	def __init__(self, name, dateAdmit, SBP, DBP, NYHA, LVEF, dateECHO, pastToxicCV, notes, 
					dateACS, dateStroke, dateLastHF, dateMajorCVSurgery, oralSoC, malignancy, currentIVBlacklist, 
					stageCKD, transplant, NIV, deviceCV, comorbidities, eligible):
		self.charactersAMGEN = { 'dateACS': dateACS, 
								'dateStroke': dateStroke, 					
								'dateLastHF': dateLastHF, 
								'dateMajorCVSurgery': dateMajorCVSurgery, 
								'oralSoC': oralSoC, 
								'malignancy': malignancy, 
								'currentIVBlacklist': currentIVBlacklist, 
								'stageCKD': stageCKD, 
								'transplant': transplant, 
								'NIV': NIV, 
								'deviceCV': deviceCV, 
								'comorbidities': comorbidities,
								'eligible': eligible}
		super(AMGENPatient, self).__init__(name, dateAdmit, SBP, DBP, NYHA, LVEF, dateECHO, 
			pastToxicCV, notes)

testAMGENPatient = AMGENPatient("Chris", "Teng", "1/1/2018", 120, 80, 2, .50, "1/1/2017", False, "", "1/2/2020", 
	"1/2/2030", "1/2/2040", "1/2/2050", True, False, False, 1, False, False, False, [], True)

class PatientDB:
	def __init__(self):
		self.patientDB = dict()

	def addPatient(self, patient):
		MRN = raw_input("Please input MRN: \n")
		if (MRN in self.patientDB.keys()):
			editPatient = raw_input("Patient MRN already exists. Edit? \n [1] Yes \n [2] No \n*2")
			if (editPatient == 1):
				self.patientDB[MRN].edit()
		else:
			MRN = raw_input("Patient MRN : \n")
			study = raw_input("What study is the patient being screened for? \n [1] DCM \n [2] AMGEN \n [3] EXPLORER \n [4] MAVERICK")
			name = raw_input("Patient name : \n")
			NYHA = raw_input("NYHA Class : \n [1] 1 \n [2] 2 \n [3] 3 \n [4] 4 \n [5] NA")
			LVEF = raw_input("LVEF : \n")
			dateECHO = raw_input("Date of last ECHO (MM/DD/YYYY) : \n")

			# TODO: Add a list of CV Toxic drugs from Appendix 2
			pastToxicCV = raw_input("Past exposure to any cardiotoxic drugs? \n [1] Yes \n [2] No")

			SBP,DBP = raw_input("SBP/DBP : \n").split("/")
			
			




			self.patientDB[MRN] = patient

	def removePatient(self, MRN):
		del self.patientDB[MRN]

	def getPatient(self, MRN):
		return self.patientDB[MRN]

MRNList = [line.split('\t')[0] for line in open("PatientDB.txt").readlines()]

def getMRNList(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
		MRNList = []
		for line in lines:
			MRNList.append(line.split('\t')[0])
	return MRNList

def queryMRN():
	MRN = raw_input("Please enter patient MRN: ")
	if (MRN in MRNList):
		return MRNList.index(MRN)
	else:
		return -1

# Prompt user for import?
# Prompt user to add patient
# Prompt user to view patient lists
def main(): 
	# Populate the list of patient MRNs in the database
	MRNList = [line.split('\t')[0] for line in open("PatientDB.txt").readlines()]
	indexPatient = queryMRN()
	while (indexPatient):
		if (indexPatient > 0):
			# Show patient info
			# Ask if user wants to edit patient info or not
		else:
			print "This MRN is not in the database. Create a new patient? "
			newPatient = raw_input("[1] Yes \n [2] No")

