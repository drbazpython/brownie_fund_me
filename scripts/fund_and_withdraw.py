from brownie import FundMe, accounts
from scripts.helpful_scripts import get_account
def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance fee: {entrance_fee}")
    print("Funding ... ")
    fund_me.fund(
        {
            "from":account,
            "value": entrance_fee
        }
    )
    print("Funded")

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing ...")
    fund_me.withdraw({"from":account})
    print("Withdrawn")

def main():
    fund()
    withdraw()