import pickle
import APP



modelUrl = open('random_forest_regression_model.pkl', 'rb')
model = pickle.load(modelUrl)
Present_Price = 10.00
Kms_Driven = 24000
Owner = 1
age = 2
Fuel_Type_Diesel = 0
Fuel_Type_Petrol = 1
Seller_Type_Individual = 1
Transmission_Manual = 1
data = [Present_Price, Kms_Driven, Owner, age, Fuel_Type_Diesel,
       Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]

result = model.predict([data])
print(result[0])