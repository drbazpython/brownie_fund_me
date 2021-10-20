from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import deploy_mocks, get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else: # deploy a mock mockV3Aggregator.sol
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        
    # pass the price feed address to our fundme contract, see first parameter in deploy,
    # and reference the contract constructor in the FundMe.sol file
    print("Deploying contract .....")
    fund_me = FundMe.deploy(
        price_feed_address,
        {
        "from":account,
         }, 
        publish_source=config["networks"][network.show_active()].get("verify") # publish source code
        )
    print(f"Contract Deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()

    # brownie networks add Etherium ganache-local host=http://127.0.0.1:7545 chainid=1337