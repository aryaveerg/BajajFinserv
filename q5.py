import pandas as pd

file_path = r"C:\Users\Aryaveer\Downloads\DataEngineeringQ2.json"
data = pd.read_json(file_path)

patient_details = pd.json_normalize(data['patientDetails'])

mode_gender = patient_details['gender'].mode()[0]  
patient_details['gender'] = patient_details['gender'].fillna(mode_gender) 

female_percentage = (patient_details['gender'].str.upper() == 'F').mean() * 100

print("Percentage of females after imputation:", round(female_percentage, 2))
