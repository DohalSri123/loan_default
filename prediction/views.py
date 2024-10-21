from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from .serializers import LoanDefaultSerializer
from .model import model

class LoanDefaultPredictionView(APIView):
    def post(self, request):
        # Validate the input data
        serializer = LoanDefaultSerializer(data=request.data)
        if serializer.is_valid():
            # Prepare the data as a DataFrame
            input_data = pd.DataFrame({
                'Age': [serializer.validated_data['age']],
                'Income': [serializer.validated_data['income']],
                'LoanAmount': [serializer.validated_data['loan_amount']],
                'CreditScore': [serializer.validated_data['credit_score']],
                'MonthsEmployed': [serializer.validated_data['months_employed']],
                'NumCreditLines': [serializer.validated_data['num_credit_lines']],
                'InterestRate': [serializer.validated_data['interest_rate']],
                'LoanTerm': [serializer.validated_data['loan_term']],
                'DTIRatio': [serializer.validated_data['dti_ratio']],
                'Education': [serializer.validated_data['education']],
                'EmploymentType': [serializer.validated_data['employment_type']],
                'MaritalStatus': [serializer.validated_data['marital_status']],
                'HasMortgage': [serializer.validated_data['has_mortgage']],
                'HasDependents': [serializer.validated_data['has_dependents']],
                'LoanPurpose': [serializer.validated_data['loan_purpose']],
                'HasCoSigner': [serializer.validated_data['has_cosigner']]
            })
            
            # Preprocess input data like before (using one-hot encoding)
            input_encoded = pd.get_dummies(input_data, columns=['Education', 'EmploymentType', 'MaritalStatus', 
                                                                'LoanPurpose', 'HasMortgage', 'HasDependents', 
                                                                'HasCoSigner'])
            input_encoded = input_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

            # Make the prediction
            prediction = model.predict(input_encoded)
            result = "NOT DEFAULT" if prediction[0] == 0 else "DEFAULT"

            # Return the result
            return Response({"prediction": result}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
