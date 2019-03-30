import time
import json
import os
from web3 import Web3, HTTPProvider

with open("ABIs/multisig.json") as f:
    abis = json.load(f)

"""
A demonstration to generate Gnosis 2 of 3 multisig wallet.
By offical multisig wallet factory to create multisig wallet contract.


Reference:
    1. https://github.com/gnosis/MultiSigWallet
"""

contract_address     = '0x1731918d1c0DcB82Ba7b70ce15C3c09dafbce980'


w3 = Web3(HTTPProvider('https://ropsten.infura.io/'))

def main():

    contract_address_checksum = Web3.toChecksumAddress(contract_address)
    multisig_wallet = w3.eth.contract(address = contract_address_checksum, abi = abis["multiSigDailyLimit"]["abi"])

    # res = multisig_wallet.functions.getTransactionCount(True, False).call()
    
    # failed
    # res = multisig_wallet.functions.getTransactionIds(0, 5, True, True).call()

    # res = multisig_wallet.functions.getOwners().call()

    res = multisig_wallet.functions.transactions(3).call()

    # res = multisig_wallet.functions.required().call()
    return res

    # txn_receipt = w3.eth.getTransactionReceipt('0xa796eebea59b54a1fffd181da4e10edb0b8976604cf23d0bcfd40fdb845598b7')
    # sub = multisig_wallet.events.Submission().processReceipt(txn_receipt)

    # print(sub)
    # print("========")
    # con = multisig_wallet.events.Confirmation().processReceipt(txn_receipt)
    # print(con)
    # print("========")
    # exe = multisig_wallet.events.Execution().processReceipt(txn_receipt)
    # print(exe)
    # return True


    

res = main()
print(res)