class Customer:
    def __init__(self,customer_id,name,email,phonenumber,age,income,credit_score):

        self.name = name
        self.email = email
        self.phonenumber = phonenumber
        self.age = age
        self.income = income
        self.credit_score = credit_score

    def check_eligibility(self):
        if self.age < 21 or self.credit_score < 650 or self.income < 2500:
            return False
        return True
    def display_customer(self):
        print("\nCustomer Details")
        print("-------------------------")
        print('customer ID       :', self.customer_ID)
        print("name             :", self.name)
        print("Email            :", self.email)
        print("Phonenumber      :", self.phonenumber)
        print("Age              :", self.age)
        print("Income           :", self.income)
        print("Credit_score     :", self.credit_score)

pavani = Customer(1, 'pavani','pavani@gmail.com',9948158322,22,50000,750)
print('Eligibility: ', pavani.check_eligibility())
pavani.display_customer()


class Lone(ABC):
    def __init__(self,loan_id,customer,loan_amount,intrest_rate,tenure):

        self.loan_id = loan_id
        self.customer = customer
        self.__loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.__balance = loan_amount
        self.__total_paid = 0
        self.repayment_history = []
        self.status = "Applied"

    @abstractmethod
    def calculate_emi(self):
        pass

    def check_loan_eligibility(self):

        if not self.customer.check_eligibility():
            self.status = "Rejected"
            return False
        return True
    
    def sanction_loan(self):
        if self.status == "Rejected":
            print("Loan application was Rejected")
            return

        if not self.check_loan_eligibility():
            print("Customer is not eligibile for the loan")
            return

        self.status = "sanctioned"

        print("\n Loan sanctioned successfully")


    def repay(self,amount):
        if self.status != "sanctioned":
            print("Repayment is not allowed")
            print("Loan status:",self.status)
            return

        if amount <=0:
            print("Invalid repayment amount")
            return

        if amount > self.__balance:
            print("Repayment amount is greater than outstanding balance")
            return

        self.__balance -= amount
        self.__total_paid += amount

        self.repayment_history.append(amount)

        print("\nRepayment successful")
        print("Amount Paid      :",amount)
        print("Outstanding Balance:",self.__balance)

        if self.__balance == 0:
            self.status = "closed"
            print("Loan closed succeessfully")

    def get_balance(self):
        return self.__balance

    def get_loan_amount(self):
        return self.__loan_amount

    def get_total_paid(self):
        return self.__total_paid

    def display_statement(self):


        print("\n")
        print("="*40)
        print("LOAN STATEMENT")
        print("="*40)

        print("Loan ID                :",self.loan_id)
        print("Customer Name          :",self.customer.name)
        print("Loan Amount            :",self.__loan_amount)
        print("Interest Rate          :",self.interest_rate)
        print("Tenure                 :",self.tenure)
        print("Total Paid             :",self.__total_paid)
        print("Outstanding Balance    :",self.__balance)
        print("Loan status            :",self.status)

        print("\nRepayment History")

        if not self.repayment_history:
            print("No repayment made")

        else:
            for i in range(len(self.repayment_hostory)):
                print(f"Payment {i+i}           : {self.repayment_history[i]}")

        print("="*40)

    def __str__(self):

        return(
            f"Loan ID: {self.loan_id},"
            f"Customer: {self.customer_name},"
            f"Loan Amount: {self.__loan_amount},"
            f"Outstanding: {self.__balance},"
            f"status: {self.status}"
        )


teju = Customer(1,'teju','teju@gmail.com',994815322,22,50000,750)
teju.display_customer()




