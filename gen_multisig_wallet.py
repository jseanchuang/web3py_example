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

contract_address     = '0x5cb85db3e237cac78cbb3fd63e84488cac5bd3dd'

sender_address       = os.environ['SENDER_ADDRESS']
sender_private_key   = os.environ['SENDER_PRIVATE_KEY']
owner1_address       = os.environ['OWNER_ADDRESS_1']
owner2_address       = os.environ['OWNER_ADDRESS_2']
owner3_address       = os.environ['OWNER_ADDRESS_3']

w3 = Web3(HTTPProvider('https://ropsten.infura.io/'))

def main():

    ### Setp 1: Get sender nonce
    nonce = w3.eth.getTransactionCount(sender_address)

    ### Step 2: Generate unsign tx 
    contract_address_checksum = Web3.toChecksumAddress(contract_address)
    factory_contract = w3.eth.contract(address = contract_address_checksum, abi = abis["multiSigDailyLimitFactory"]["abi"])
    tx = factory_contract.functions.create([owner1_address, owner2_address, owner3_address], 2, 0
    ).buildTransaction({
        'chainId': 3,
        'gasPrice': w3.toWei('11', 'gwei'),
        'nonce': nonce,
    })

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
    logs = factory_contract.events.ContractInstantiation().processReceipt(txn_receipt)
    wallet_address = logs[0]['args']['instantiation']
    return {'status': 'success', 'txhash': tx_hash, 'wallet_address': wallet_address}

res = main()
print(res)