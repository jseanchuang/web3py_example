# from multisig_wallet import Multisig_wallet
import multisig_wallet

address = '0x1731918d1c0DcB82Ba7b70ce15C3c09dafbce980'


# wallet = multisig_wallet.Multisig_wallet(address)
# print(wallet.require())
res = multisig_wallet.Multisig_wallet()
res.require()
# acct.deposit(500)
# acct.withdraw(200)
# print(acct)
