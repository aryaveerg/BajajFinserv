import pandas as pd

file_path = r"C:\Users\Aryaveer\Downloads\DataEngineeringQ2.json" 
data = pd.read_json(file_path)

medicines_list = data['consultationData'].apply(lambda x: x['medicines'])

is_active = [medicine['isActive'] for sublist in medicines_list for medicine in sublist]

active_percentage = (sum(is_active) / len(is_active)) * 100
inactive_percentage = 100 - active_percentage

print(f"{round(active_percentage, 2)},{round(inactive_percentage, 2)}")
