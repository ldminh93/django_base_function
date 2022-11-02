#
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from web3 import Web3
# from decouple import config
# from web3.auto import w3
# from web3.gas_strategies.rpc import rpc_gas_price_strategy
#
#
#
#
# class House:
#
#     def __init__(self, price):
#         self._price = price
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, new_price):
#         if new_price > 0 and isinstance(new_price, int):
#             self._price = new_price
#         else:
#             print("Please enter a valid price")
#
#     @price.deleter
#     def price(self):
#         del self._price
#
#
# house = House(3000)
# house.price = 2000
# a = house.price
#
# def decorator(func):
#     def wrapper():
#         print('start ')
#         func()
#         print('end')
#     return wrapper()
#
#
#
# from functools import wraps
#
# def allowed_states(allowed):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(self, request):
#             print('Start Function')
#             print(allowed)
#             result = func(self, request)
#             print('End Function')
#             return result
#         return wrapper
#     return decorator
#
# import json
#
# class Blockchain(APIView):
#
#     @allowed_states(allowed=1)
#     def get(self, request):
#         # infura_url = 'https://goerli.infura.io/v3/e7c309ac5ecd46a58b7c7c31a0352891'
#         # print(infura_url)
#         RPC = 'http://127.0.0.1:7545'
#         # HTTPProvider:
#         w3 = Web3(Web3.HTTPProvider(RPC))
#         res = w3.isConnected()
#         print(res)
#         latest_block = w3.eth.get_block('latest')
#         print(latest_block)
#         # is_address_valid = w3.isAddress('0x6dAc6E2Dace28369A6B884338B60f7CbBF7fb9be')
#         sender = '0x5430EFE6751Cca7d61f501fe65D367C3699A73E1'
#         sender_pk = 'd5d5034860768f42e85d19c041727f47db9655f2968c38bec1a2b0bbe61efbef'
#         receiver = '0xAc49486bAfAef1565bD06D4DF3a5400B3fCbB5df'
#
#         # get balance
#         sender_bl = w3.fromWei(w3.eth.get_balance(sender), "ether")
#
#         receiver_bl = w3.fromWei(w3.eth.get_balance(receiver), "ether")
#
#         # Set the gas price strategy
#         w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)
#
#         # sign transaction
#         tx_create = w3.eth.account.sign_transaction(
#             {
#                 "nonce": w3.eth.get_transaction_count(sender),
#                 "gasPrice": w3.eth.generate_gas_price(),
#                 "gas": 21000,
#                 "to": receiver,
#                 "value": w3.toWei("1", "ether"),
#             },
#             sender_pk,
#         )
#
#         # Send tx and wait for receipt
#         tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
#         tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
#         print(f"Transaction successful with hash: {tx_receipt.transactionHash.hex()}")
#
#
#         #
#         # EIP20_ABI = json.loads(
#         #     '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501
#         # unicorns = w3.eth.contract(address='0x83F94C29D00735b30D1C76B0Da061eEddeE9b1b5', abi=EIP20_ABI)
#         #
#         # nonce = w3.eth.get_transaction_count('0x83F94C29D00735b30D1C76B0Da061eEddeE9b1b5')
#         #  1	Ethereum mainnet
#         # 2	Morden (disused), Expanse mainnet
#         # 3	Ropsten
#         # 4	Rinkeby
#         # 5	Goerli
#         # 42	Kovan
#         #
#         # me = '0x83F94C29D00735b30D1C76B0Da061eEddeE9b1b5'
#         # alice = '0x313257411063D59f7788A3186c4a626688a7C9bD'
#         # nonce = w3.eth.get_transaction_count(me)
#         # refund = {
#         #     "from": me,
#         #     "to": alice,
#         #     'chainId': 5,
#         #     "value": 0x10000000000,
#         #     "gas": 30000,
#         #     # "gasPrice": int(w3.eth.gasPrice * 1.40),
#         #     'maxFeePerGas': w3.toWei('3', 'gwei'),
#         #     'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
#         #     "nonce": nonce
#         # }
#         #
#         # key = "0x637e2db65ac116c2931eaf961a11bab76037a92fba394dccf6e8c1ac72613d35"
#         # signed_txn = w3.eth.account.sign_transaction(refund, key)
#         # txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
#         # w3.eth.wait_for_transaction_receipt(txn_hash)
#         # w3.eth.get_balance(me)
#         # w3.eth.get_balance(alice)
#
#
#         # transaction = unicorns.functions.transfer(
#         #     '0x313257411063D59f7788A3186c4a626688a7C9bD',
#         #     0x100000000000,
#         # ).build_transaction({
#         #     'from': '0x83F94C29D00735b30D1C76B0Da061eEddeE9b1b5',
#         #     'value': 0,
#         #     'chainId': 5,
#         #     'gas': 700000,
#         #     'maxFeePerGas': w3.toWei('2', 'gwei'),
#         #     'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
#         #     'nonce': nonce,
#         # })
#         #
#         # private_key = '0x637e2db65ac116c2931eaf961a11bab76037a92fba394dccf6e8c1ac72613d35'
#         #
#         # signed_txn = w3.eth.account.signTransaction(transaction, private_key)
#         # res = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
#         #
#         # hex = w3.toHex(w3.keccak(signed_txn.rawTransaction))
#         #
#         # check_sum = w3.toChecksumAddress('0xd7986a11f29fd623a800adb507c7702415ee7718')
#         # balance = w3.eth.get_balance(check_sum)
#         # print(balance)
#         #
#         # ether_value = w3.fromWei(balance, 'ether')
#         # print(ether_value)
#         #
#         # trans = w3.eth.get_transaction('0x49342a58976e9bacf21db970d3f69666bbae809e38be88f00560189010decf89')
#         #
#         # trans_receipt = w3.eth.get_transaction_receipt('0xd0f9e247581f9d4c5177fb315e7115e50fc9f673e0915b4b64f3ef5c1b8b81aa')
#         # print(trans_receipt)
#
#         return Response(status=status.HTTP_201_CREATED)
