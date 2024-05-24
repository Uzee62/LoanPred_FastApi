from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
import json
import sklearn
from schemas import model_input


app = FastAPI()



#load the saved model

loan_prediction = pickle.load(open("LoanPred.pkl",'rb' ))

#creating an API

@app.post("/loan_prediction")
def loan_pred(input: model_input):
    input_data = input.json()
    input_dict = json.loads(input_data)
    
    Gender = input_dict["Gender"]
    Marital_Status = input_dict["Married"]
    Dependents = input_dict["Dependents"]
    Education = input_dict["Education"]
    Employes = input_dict["Self_Employed"]
    Income = input_dict["ApplicantIncome"]
    loan = input_dict["LoanAmount"]
    term = input_dict["Loan_Amount_Term"]
    Credit = input_dict["Credit_History"]
    Area = input_dict["Property_Area"]
    
    
    input_list= [Gender,Marital_Status,Dependents,Education,Employes,Income,loan,term,Credit,Area]
    
    prediction = loan_prediction.predict([input_list])
    
    if prediction[0]==1:
        return "Loan is approved"
    else:
        return "Loan is not approved"



