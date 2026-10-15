
import random

#Doctors work finite days 0900-1700
#Appointment duration 15-30  minutes +-
#Doctor cannot see two patients at the same time
#Apointments cannot be intreupted
#Appointments have to fall within doctors working hours
#Each patient has a urgency level

class Doctors:
    def __init__(self,ID, time):
        self.id = ID
        self.time = time
        self.dplist = []
    def AddPatient(self,patient):
        self.dplist.append(patient)

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
for i in range(30):
    p = "p"
    PList.append(p+str(i))
    PList[i] = Patients(ID=i,urgency=random.randrange(0,4),time=random.randrange(2),preferance=random.randrange(0,len(Docs) + 1))
    if (PList[i].pref != 0):
        for z in range(len(Docs)):
            pointer = z + 1
            if (pointer == PList[i].pref):
                Docs[z].AddPatient(PList[i].iD)

print(D1.dplist)
print(D2.dplist)
print(D3.dplist)