from pydantic import BaseModel
class model_input(BaseModel):
    Gender:float
    Married : float
    Dependents:float
    Education: float
    Self_Employed:float
    ApplicantIncome:float
    LoanAmount : float
    Loan_Amount_Term : float
    Credit_History : float
    Property_Area :float