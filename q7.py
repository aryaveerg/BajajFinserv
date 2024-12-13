import pandas as pd

file_path = r"C:\Users\Aryaveer\Downloads\DataEngineeringQ2.json" 
data = pd.read_json(file_path)

num_medicines_per_consultation = data['consultationData'].apply(lambda x: len(x['medicines']))

average_medicines = num_medicines_per_consultation.mean()

print("Average number of medicines prescribed:", round(average_medicines, 2))
