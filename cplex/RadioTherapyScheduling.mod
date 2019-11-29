/*********************************************
 * OPL 12.9.0.0 Model
 * Author: Luca Andrei
 * Creation Date: Oct 17, 2019 at 9:30:26 PM
 *********************************************/

/* Input variables */
int NbPatients = ...;
int NbDays = ...;
int NbSlots = ...;
 
range Patients = 1..NbPatients;
range Days = 1..NbDays;
range Slots = 1..NbSlots;

int NbTreatmentDays[Patients] = ...;
int PatientPriority[Patients] = ...;

int PMax = max (p in Patients) PatientPriority[p];

/* Decision variables */
dvar int BeginTreatmentInCurrentWeek[Patients] in 0..1;
dvar int PatientAssignment[Patients][Days][Slots] in 0..1;
dvar int FirstAppointment[Patients][Days][Slots] in 0..1;
dvar int FirstAppointmentPreparation[Patients][Days][Slots] in 0..1;

/* Optimization */
minimize
  sum(j in Patients, k in Days, w in Slots)
	(
	(1/PatientPriority[j] - 1) * FirstAppointment[j][k][w] +
    (1 - FirstAppointment[j][k][w]) * (1 / j) * pow(PatientPriority[j], 1 / (PMax - PatientPriority[j]))
    );
  
subject to {
  forall(k in Days, w in Slots)
    ct1:
      sum(j in Patients) 
      	(PatientAssignment[j][k][w] + FirstAppointmentPreparation[j][k][w]) <= 1; 
      	
  forall(j in Patients)
    ct2:
    	sum(k in Days, w in Slots) FirstAppointment[j][k][w] <= 1;   
    	
  forall(j in Patients)
    ct3:
    	sum(k in Days, w in Slots) FirstAppointmentPreparation[j][k][w] <= 1; 
    	 
  forall(j in Patients, k in 1..NbDays - NbTreatmentDays[j] + 1)
    	sum(s in k..k + NbTreatmentDays[j] - 1, w in Slots) 
    		PatientAssignment[j][s][w]
		>=
		NbTreatmentDays[j] * sum(w in Slots) FirstAppointment[j][k][w];
		
  forall(j in Patients)
    ct5:
    	sum(k in Days, w in Slots) PatientAssignment[j][k][w] 
    	== 
    	BeginTreatmentInCurrentWeek[j] * NbTreatmentDays[j];  
    	
  forall(j in Patients, k in Days, w in 1..NbSlots - 1)
    ct6:
		FirstAppointment[j][k][w] == FirstAppointmentPreparation[j][k][w + 1];
		
  forall(j in Patients, k in Days, w in Slots)
    ct7:
		PatientAssignment[j][k][w] >= FirstAppointment[j][k][w];
}

