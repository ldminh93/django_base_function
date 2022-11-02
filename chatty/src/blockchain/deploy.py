from src.blockchain.compile import abi, byte_code
import web3
from web3 import Web3

RPC = 'http://127.0.0.1:7545'
# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(RPC))
res = w3.isConnected()

account_from = {
    'private_key': 'd5d5034860768f42e85d19c041727f47db9655f2968c38bec1a2b0bbe61efbef',
    'address': '0x5430EFE6751Cca7d61f501fe65D367C3699A73E1',
}

# Create contract instance
Incrementer = w3.eth.contract(abi=abi, bytecode=byte_code)

# tx_create = w3.eth.account.sign_transaction(
#             {
#                 "nonce": w3.eth.get_transaction_count(sender),
#                 "gasPrice": w3.eth.generate_gas_price(),
#                 "gas": 21000,
#                 "to": receiver,
#                 "value": w3.toWei("1", "ether"),
#             },
#             sender_pk,
#         )
# Build constructor tx
receiver = '0xAc49486bAfAef1565bD06D4DF3a5400B3fCbB5df'

# call constructor function in "incrementer.sol"
construct_txn = Incrementer.constructor(5).buildTransaction(
    {
        'from': account_from['address'],
        "gasPrice": 210000,
        "gas": 210000,
        # "to": receiver,
        # "value": w3.toWei("1", "ether"),
        'nonce': w3.eth.get_transaction_count(account_from['address']),
    }
)
# Sign tx with PK
tx_create = w3.eth.account.sign_transaction(construct_txn, account_from['private_key'])

# Send tx and wait for receipt
tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Contract deployed at address: { tx_receipt.contractAddress }')