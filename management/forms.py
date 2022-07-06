from django import forms
from django.forms import ModelForm, Textarea
from django.db.models import Q
from data.models import DSU
from accounts.models import CustomerUser
from .models import Department, TaskLinks, Transaction, Outflow, Inflow, Policy, Requirement

"""
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['first_name', 'last_name','contact', 'email'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

"""
class DepartmentForm(forms.ModelForm):  
    class Meta:  
        model = Department  
        fields = ['name', 'slug','description', 'is_active','is_featured']
        widgets = {"description": Textarea(attrs={"cols": 40, "rows": 2})}

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields["name"].empty_label = "Select"

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction

        fields = [
            "id",
            "sender",
            "receiver",
            "phone",
            "department",
            "category",
            "type",
            "payment_method",
            "qty",
            "amount",
            "transaction_cost",
            "description",
            "receipt_link",
        ]
        labels = {
            "sender": "Your full Name",
            "receiver": "Enter Receiver Name",
            "phone": "Receiver Phone",
            "department": "Department",
            "category": "Category",
            "type": "Type",
            "payment_method": "Payment Method",
            "qty": "Quantity",
            "amount": "Unit Price",
            "transaction_cost": "Transaction Cost",
            "description": "Description",
            "receipt_link": "Link",
        }
        widgets = {"description": Textarea(attrs={"cols": 30, "rows": 1})}

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields["payment_method"].empty_label = "Select"


class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflow
        fields = [
            "sender",
            "receiver",
            "phone",
            "department",
            "category",
            "type",
            "payment_method",
            "qty",
            "amount",
            "transaction_cost",
            "description",
        ]
        labels = {
            "sender": "Full Name",
            "receiver": "Enter Receiver Name",
            "phone": "Receiver Phone",
            "department": "Department",
            "category": "Category",
            "type": "Cost Type",
            "payment_method": "Payment Method",
            "qty": "Quantity",
            "amount": "Unit Price",
            "transaction_cost": "Transaction Cost",
            "description": "Description",
        }
        widgets = {"description": Textarea(attrs={"cols": 30, "rows": 1})}

    def __init__(self, *args, **kwargs):
        super(OutflowForm, self).__init__(*args, **kwargs)
        self.fields["payment_method"].empty_label = "Select"


class InflowForm(forms.ModelForm):
    class Meta:
        model = Inflow
        fields = [
            "receiver",
            "phone",
            "category",
            "task",
            "method",
            "period",
            "qty",
            "amount",
            "transaction_cost",
            "description",
        ]
        labels = {
            "receiver": "Enter Receiver Name",
            "phone": "Receiver Phone",
            "department": "Department",
            "category": "Category",
            "task": "Task",
            "method": "Payment Method",
            "period": "Period",
            "qty": "Quantity",
            "amount": "Unit Price",
            "transaction_cost": "Transaction Cost",
            "description": "Comments",
        }
        widgets = {"description": Textarea(attrs={"cols": 30, "rows": 1})}

    def __init__(self, *args, **kwargs):
        super(InflowForm, self).__init__(*args, **kwargs)
        self.fields["method"].empty_label = "Select"


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = [
            "first_name",
            "last_name",
            "department",
            "type",
            "description",
            "policy_doc",
        ]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "type": "Policy Type",
            "department": "Department",
            "description": "Description",
            "policy_doc": "Attach Policy",
        }


class ManagementForm(forms.ModelForm):
    class Meta:
        model = DSU
        # fields =['client','category','question_type','doc','link']
        fields = [
            "trained_by",
            "client_name",
            "type",
            "category",
            "task",
            "plan",
            "challenge",
            "uploaded",
        ]
        labels = {
            "type": "Client/Staff?",
            "client_name": "Manager",
            "trained_by": "Staff/Employee",
            "category": "Category",
            "task": "What Did You Work On?",
            "plan": "What is your next plan of action on areas that you have not touched on?",
            "challenge": "What specific questions/Challenges are you facing?",
            "uploaded": "Have you uploaded any DAF evidence/1-1 sessions?",
        }


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = [
            "created_by",
            "assigned_to",
            "requestor",
            "company",
            "category",
            "app",
            "delivery_date",
            "duration",
            "what",
            "why",
            "how",
            "doc",
            'is_active'
        ]

        labels = {
            "created_by": "Creator",
            "assigned_to": "assigned_to",
            "requestor ": "Who needs it/beneficiary?",
            "app": "Specify app if Website",
            "company":"company",
            "category": "Select a category",
            "what": "Describe the Requirement",
            "why": "Why do they need it ?",
            "delivery_date": "When should this be delivered",
            "how": "Mode of delivery(website/Report/database?",
            "duration": "how long will it take to work on this requirement",
            "doc": "Upload Supporting Document",
        }
        #  If you have to exclude some features you put them here
        # exclude = (
        #     "user",
        #     "recurring",
        # )

        # Forms updated by Karki
    # def __init__(self, **kwargs):
    #     super(RequirementForm, self).__init__(**kwargs)
    #     self.fields["assigned_to"].queryset = CustomerUser.objects.filter(
    #         Q(is_admin=True) | Q(is_employee=True)
    #         # Q(is_client=True)
    #     )

    # def __init__(self, **kwargs):
    #     super(RequirementForm, self).__init__(**kwargs)
    #     self.fields["assigned_to"].queryset = CustomerUser.objects.filter(
    #         is_employee=True 
    #         # Q(is_employee=True)

    #     )

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = TaskLinks
        fields = [
                    "task",
                    "added_by",
                    "link_name",
                    "description",
                    "doc",
                    "link",
                    "is_active",
                    "is_featured",
        ]

        labels = {
                "task ":"Task Name",
                "added_by":"Your Username",
                "link_name":"Enter link name",
                "description":"Describe the link/Evidence",
                "doc":"Upload file/document if possible",
                "link":"Upload link/paste your link below",
                # "is_active ":"Is this link still active "
        }
        #  If you have to exclude some features you put them here
        # exclude = (
        #     "user",
        #     "recurring",
        # )

        # Forms updated by Karki
    # def __init__(self, **kwargs):
    #     super(EvidenceForm, self).__init__(**kwargs)
    #     self.fields["added_by"].queryset = CustomerUser.objects.filter(is_employee=True)

