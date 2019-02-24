import time
import os
from web3 import Web3, HTTPProvider


"""
A demonstration to send ETH
"""
sender_assress       = os.environ['SENDER_ADDRESS']
sender_private_key   = os.environ['SENDER_PRIVATE_KEY']
receiver_address     = os.environ['RECEIVER_ADDRESS']

w3 = Web3(HTTPProvider('https://ropsten.infura.io/'))

def main(amount_in_ether):
    ### Setp 1: Get sender nonce
    nonce = w3.eth.getTransactionCount(sender_assress)

    ### Step 2: Generate unsign tx 
    tx = {
            'to': receiver_address,
            'value': w3.toWei(amount_in_ether,'ether'),
            'gas': 2000000,
            'gasPrice': w3.toWei('11', 'gwei'),
            'nonce': nonce,
            'chainId': 3
    }

    ### Setp 3: Sign tx via sender private key
    signed_tx = w3.eth.account.signTransaction(tx, sender_private_key)

    ### Step 4: Send signed tx to chain
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    ### Step 5: Wait tx been mined
    tx_receipt = None
    count = 0
    while tx_receipt is None and (count < 30):
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        count += 1
        time.sleep(10)


    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'success', 'tx_receipt': tx_receipt}

res = main(0.1)
print(res)