
import random

#Doctors work finite days 0900-1700
#Appointment duration 15-30  minutes +- [0 = 5], [1 = 10] , [2 = 15], [3 = 30]
#Doctor cannot see two patients at the same time
#Apointments cannot be intreupted
#Appointments have to fall within doctors working hours
#Each patient has a urgency level

class Doctors:
    def __init__(self,ID, time):
        self.id = ID
        self.time = time
        self.dplist = []
        self.aptime = []
    def AddPatient(self,patient):
        self.dplist.append(patient)
    def AllocateSpace(self,times):
        self.aptime = [times]

class Patients:
    def __init__(self,ID,urgency,time,preferance):
        self.iD = ID #Any numbber ID
        self.urgency = urgency #0-5
        self.time = time #15-30 minutes
        self.pref = preferance

D1 = Doctors("D1",14)
D2 = Doctors("D2",17)
D3 = Doctors("D3",15)

Docs = [D1,D2,D3]
PList = []
NoDoc = []
def PatientSorter(Doctor):
    LenList = (len(Doctor.dplist) - 1)
    i = 0
    fp = 0
    c = 0
    loop = True
    while loop: 
        if c == LenList:
            loop = False
        elif fp > LenList:
            i = -1
            c = 0
        elif PList[Doctor.dplist[i]].urgency > PList[Doctor.dplist[fp]].urgency:
            Doctor.dplist[i],Doctor.dplist[fp] = Doctor.dplist[fp],Doctor.dplist[i]
            c = 0
            loop = True
        elif PList[Doctor.dplist[i]].urgency == PList[Doctor.dplist[fp]].urgency:
            loop = True
        c+= 1
        i+= 1
        fp = i + 1

def TimeSlotSort(Doctor):
    WorkTime = Doctor.time
    PlannedTime = 0
    while PlannedTime != WorkTime:

        for i in range(12):
            Space = i * 5
            Doctor.AllocateSpace(Space)
            
        Start = 9
        for i in range(Doctor.dplist):
            time = PList[Doctor.dplist[i]].time
            



for i in range(30):
    p = "p"
    PList.append(p+str(i))
    PList[i] = Patients(ID=i,urgency=random.randrange(0,4),time=random.randrange(3),preferance=random.randrange(0,len(Docs) + 1))
    if (PList[i].pref != 0):
        for z in range(len(Docs)):
            pointer = z + 1
            if (pointer == PList[i].pref):
                Docs[z].AddPatient(PList[i].iD)
                

for i in range(len(PList)):
    print(PList[i].iD,",",PList[i].urgency)
print("Sort")
PatientSorter(D1)
PatientSorter(D2)
PatientSorter(D3)
print("D1 :")
for i in range (len(D1.dplist)):
    print("[",PList[D1.dplist[i]].iD,"]","[",PList[D1.dplist[i]].urgency,"]")
print("D2 :")
for i in range (len(D2.dplist)):
    print("[",PList[D2.dplist[i]].iD,"]","[",PList[D2.dplist[i]].urgency,"]")
print("D3 :")
for i in range (len(D3.dplist)):
    print("[",PList[D3.dplist[i]].iD,"]","[",PList[D3.dplist[i]].urgency,"]")