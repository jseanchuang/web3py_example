import time
import json
import os
from web3 import Web3, HTTPProvider

with open("ABIs/multisig.json") as f:
    abis = json.load(f)

"""
A demonstration to generate Gnosis 2 of 3 multisig wallet.
By offical multisig wallet factory to create multisig wallet contract.

Multisig-factor address
Mainnet:
Ropsten:    0x5cb85db3e237cac78cbb3fd63e84488cac5bd3dd
Rinkeby:    0x19ba60816abca236baa096105df09260a4791418

Reference:
    1. https://github.com/gnosis/MultiSigWallet
"""

contract_address     = '0x1731918d1c0DcB82Ba7b70ce15C3c09dafbce980'

sender_address       = '0xC5db30061B9F8B4fF8b01814663c36AB6F81F175'
sender_private_key   = 'a754694c48c73552cbadf9127c9cd0efe508fe04c92b0b9eb65628a61a0f29f6'

w3 = Web3(HTTPProvider('https://ropsten.infura.io/'))

def main():

    ### Setp 1: Get sender nonce
    nonce = w3.eth.getTransactionCount(sender_address)

    ### Step 2: Generate unsign tx 
    contract_address_checksum = Web3.toChecksumAddress(contract_address)
    multisig_wallet = w3.eth.contract(address = contract_address_checksum, abi = abis["multiSigDailyLimit"]["abi"])

    print("start")
    tx = multisig_wallet.functions.confirmTransaction(2).buildTransaction({
        'chainId': 3,
        'gasPrice': w3.toWei('11', 'gwei'),
        'nonce': nonce,
    })
    tx = multisig_wallet.functions.confirmTransaction(2)
    print(tx.estimateGas())
    print("end")
    return
    ### Setp 3: Sign tx via sender private key
    signed_tx = w3.eth.account.signTransaction(tx, sender_private_key)

    ### Step 4: Send signed tx to chain
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    ### Step 5: Wait tx been mined
    txn_receipt = None
    count = 0
    while txn_receipt is None and (count < 30):
        txn_receipt = w3.eth.getTransactionReceipt(tx_hash)
        count += 1
        time.sleep(10)

    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    ### Step 6: Parse logs from tx_recepit to get created multisig wallet contract address
    # logs = factory_contract.events.ContractInstantiation().processReceipt(txn_receipt)
    # wallet_address = logs[0]['args']['instantiation']
    return {'status': 'success', 'txhash': tx_hash, 'wallet_address': wallet_address}

res = main()
print(res)