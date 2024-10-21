from rest_framework import serializers

class LoanDefaultSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    income = serializers.FloatField()
    loan_amount = serializers.FloatField()
    credit_score = serializers.IntegerField()
    months_employed = serializers.IntegerField()
    num_credit_lines = serializers.IntegerField()
    interest_rate = serializers.FloatField()
    loan_term = serializers.IntegerField()
    dti_ratio = serializers.FloatField()
    education = serializers.ChoiceField(choices=["Bachelor's", "Master's", "PhD", "High School"])
    employment_type = serializers.ChoiceField(choices=["Full-time", "Part-time", "Unemployed", "Self-employed"])
    marital_status = serializers.ChoiceField(choices=["Single", "Married", "Divorced", "Widowed"])
    has_mortgage = serializers.ChoiceField(choices=["Yes", "No"])
    has_dependents = serializers.ChoiceField(choices=["Yes", "No"])
    loan_purpose = serializers.ChoiceField(choices=["Auto", "Business", "Home", "Education", "Other"])
    has_cosigner = serializers.ChoiceField(choices=["Yes", "No"])
