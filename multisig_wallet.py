class MultiSig_wallet:
    def __init__(self, address):
        # contract_address_checksum = Web3.toChecksumAddress(address)
        # self.multisig_wallet = w3.eth.contract(address = contract_address_checksum, abi = abis["multiSigDailyLimit"]["abi"])

    def require(self):
        # return self.multisig_wallet.functions.required().call()
        print("require")



# import time
# import json
# import os
# from web3 import Web3, HTTPProvider
# w3 = Web3(HTTPProvider('https://ropsten.infura.io/'))

# with open("ABIs/multisig.json") as f:
#     abis = json.load(f)

# def foo(address):
#     # print('I am foo in m1')
#     contract_address_checksum = Web3.toChecksumAddress(address)
#     multisig_wallet = w3.eth.contract(address = contract_address_checksum, abi = abis["multiSigDailyLimit"]["abi"])
#     res = multisig_wallet.functions.required().call()
#     print(res)
#     print('end')

# class MultiSig_wallet:
    
    # def __init__(self, address):
    #     contract_address_checksum = Web3.toChecksumAddress(address)
    #     self.multisig_wallet = w3.eth.contract(address = contract_address_checksum, abi = abis["multiSigDailyLimit"]["abi"])

    # def require(self):
    #     return self.multisig_wallet.functions.required().call()

