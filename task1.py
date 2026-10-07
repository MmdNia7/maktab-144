import re
from datetime import datetime,timedelta
import argparse


class Contractor:
    def __init__(self,id,name,special,email,phone_number):
        if re.match(r"^CON-\d{6}$",id):
            self.id = id
        else:
            raise ValueError("Invalid id")
        self.name = name
        self.special = special
        if re.match(r".+@.+\.com$", email):
            self.email = email
        else:
            raise ValueError("Invalid email")
        if re.match(r"^09\d{9}$",phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Invalid phone-number")    

    @property
    def summary(self):
        return self.name + " | " + self.special
        


class Contract:
    def __init__(self, id, contractor_id, project_title, amount, start_date, end_date, status):
        if re.match(r"^PRJ-\d{4}-\d{3}$", id):
            self.id = id
        else:
            raise ValueError("Invalid contract id")
        self.contractor_id = contractor_id
        self.project_title = project_title
        self.amount = amount
        self.start_date = datetime.strptime(start_date, "%d-%m-%Y")
        self.end_date = datetime.strptime(end_date, "%d-%m-%Y")
        if self.end_date > self.start_date:
            pass
        else:
            raise ValueError("Invalid start_date or end_date")    
        if status in ["pending", "active", "completed", "cancelled"]:
            self.status = status
        else:
             raise ValueError("Invalid status")

    @property
    def remaining_days(self):
        result = datetime.now()
        if result >= self.end_date:
            return 0
        return (self.end_date - result).days

    @property
    def is_overdue(self):
        if self.status == "active" and datetime.now() > self.end_date:
            return True
        else:
            return False

class Payment:
    def __init__(self, id, contract_id, amount, payment_date, description):
        if re.match(r"^PAY-\d{6}$", id):
            self.id = id
        else:
            raise ValueError("Invalid payment id")
        self.contract_id = contract_id
        self.amount = amount
        self.peyment_date = datetime.strptime(payment_date, "%Y-%m-%d")
        if self.peyment_date > datetime.now():
            raise ValueError("Invalid peyment_date")
        self.description = description



class ContractSystem:
    def __init__(self):
        self.contractors = []
        self.contracts = []
        self.payments = []

    def add_contractor(self,contractor):
        for c in self.contractors:
            if contractor.id == c.id:
                raise ValueError("This contractor has already been registered.")
        self.contractors.append(contractor)            

    def remove_contractor(self,id):
        for c in self.contractors:
            if id == c.id:
                self.contractors.remove(c)
                return
        raise ValueError("error,No contractor was found.")
        
    def add_contract(self,contract):
        for c in self.contracts:
            if contract.id == c.id:
                raise ValueError("This contract has already been registered.")
        self.contracts.append(contract)

    def remove_contract(self, id):
        for c in self.contracts:
            if id == c.id:
                self.contracts.remove(c)
                return
        raise ValueError("Error, No contract was found.")    

    def add_payment(self, payment):
        for p in self.payments:
            if payment.id == p.id:
                raise ValueError("This payment has already been registered.")
        self.payments.append(payment)    

    def remove_payment(self,id):
        for p in self.payments:
            if id == p.id:
                self.payments.remove(p)
                return
        raise ValueError("Payment not found")       

    def total_paid_by_contractor(self, contractor_id):
        total = 0
        for contract in self.contracts:
            if contract.contractor_id == contractor_id:
                for payment in self.payments:
                    if payment.contract_id == contract.id:
                        total += payment.amount
        return total



c_system = ContractSystem()

contractor1 = Contractor(
    "CON-000001",
    "Ali Ahmadi",
    "Electrician",
    "ali@gmail.com",
    "09121234567"
)

contractor2 = Contractor(
    "CON-000002",
    "Reza Mohammadi",
    "Plumber",
    "reza@gmail.com",
    "09121234568"
)

contractor3 = Contractor(
    "CON-000003",
    "Sara Hosseini",
    "Painter",
    "sara@gmail.com",
    "09121234569"
)

c_system.add_contractor(contractor1)
c_system.add_contractor(contractor2)
c_system.add_contractor(contractor3)


contract1 = Contract(
    "PRJ-2026-001",
    "CON-000001",
    "Building Electrical",
    100000000,
    "01-10-2026",
    "20-10-2026",
    "active"
)

contract2 = Contract(
    "PRJ-2026-002",
    "CON-000001",
    "Office Wiring",
    80000000,
    "05-10-2026",
    "25-10-2026",
    "pending"
)

contract3 = Contract(
    "PRJ-2026-003",
    "CON-000002",
    "Water System",
    150000000,
    "01-09-2026",
    "15-09-2026",
    "completed"
)

contract4 = Contract(
    "PRJ-2026-004",
    "CON-000002",
    "Pool Plumbing",
    120000000,
    "10-10-2026",
    "30-10-2026",
    "active"
)

contract5 = Contract(
    "PRJ-2026-005",
    "CON-000003",
    "Office Painting",
    60000000,
    "01-10-2026",
    "12-10-2026",
    "active"
)


c_system.add_contract(contract1)
c_system.add_contract(contract2)
c_system.add_contract(contract3)
c_system.add_contract(contract4)
c_system.add_contract(contract5)


payment1 = Payment(
    "PAY-000001",
    "PRJ-2026-001",
    30000000,
    "2026-10-02",
    "First payment"
)

payment2 = Payment(
    "PAY-000002",
    "PRJ-2026-001",
    20000000,
    "2026-10-04",
    "Second payment"
)

payment3 = Payment(
    "PAY-000003",
    "PRJ-2026-002",
    25000000,
    "2026-10-05",
    "Initial payment"
)

payment4 = Payment(
    "PAY-000004",
    "PRJ-2026-003",
    50000000,
    "2026-09-05",
    "First payment"
)

payment5 = Payment(
    "PAY-000005",
    "PRJ-2026-003",
    40000000,
    "2026-09-12",
    "Final payment"
)

payment6 = Payment(
    "PAY-000006",
    "PRJ-2026-004",
    30000000,
    "2026-10-05",
    "Initial payment"
)

c_system.add_payment(payment1)
c_system.add_payment(payment2)
c_system.add_payment(payment3)
c_system.add_payment(payment4)
c_system.add_payment(payment5)
c_system.add_payment(payment6)



# CLI

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")    

contractors_parser = subparsers.add_parser("contractors-list")
contractors_parser.add_argument("--specialty")

contracts_parser = subparsers.add_parser("list-contracts")
contracts_parser.add_argument("--contractor-id")
contracts_parser.add_argument("--status")

summary_parser = subparsers.add_parser("contractor-summary")
summary_parser.add_argument("--contractor-id", required=True)

args = parser.parse_args()

if args.command == "contractors-list":
    for contractor in c_system.contractors:
        if args.specialty is None or contractor.special == args.specialty:
            print(contractor.summary)


if args.command == "list-contracts":
    for contract in c_system.contracts:
        if args.contractor_id is None or contract.contractor_id == args.contractor_id:
            if args.status is None or contract.status == args.status:
                print(
                    contract.id,
                    contract.project_title,
                    contract.contractor_id,
                    contract.status
                )


if args.command == "contractor-summary":
    for contractor in c_system.contractors:
        if contractor.id == args.contractor_id:
            print("Contractor:", contractor.summary)
            print("Total paid:", c_system.total_paid_by_contractor(contractor.id))

            print("Contracts:")
            for contract in c_system.contracts:
                if contract.contractor_id == contractor.id:
                    print(
                        contract.id,
                        contract.project_title,
                        contract.amount,
                        contract.status
                    )
            break
    else:
        print("Contractor not found")








