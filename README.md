# Web3py examples

|Example|Description|
| --|--|
|[gen_eth_hd_wallet.py](./gen_eth_hd_wallet.py)|Generate standard HD wallet base|
|[send_eth_tx.py](./send_eth_tx.py)|Send ETH transaction
|[gen_multisig_wallet](gen_multisig_wallet.py)|Generate Gnosis MultiSig wallet

# Run the code
```
$ source .env
$ python3 ${example}
```

## Environment variable template
```
### env variables for multisig example
export SENDER_ADDRESS=
export SENDER_PRIVATE_KEY=
export OWNER_ADDRESS_1=
export OWNER_ADDRESS_2=
export OWNER_ADDRESS_3=

### env variables for send eth transaction example
export SENDER_ADDRESS=
export SENDER_PRIVATE_KEY=
export RECEIVER_ADDRESS=
```