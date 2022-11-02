from src.blockchain.compile import abi
from web3 import Web3
RPC = 'http://127.0.0.1:7545'
# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(RPC))
res = w3.isConnected()
contract_adds = '0x066446a9CbF874F79a4378cca671c52Eb622d64a'

# 4. Create contract instance
Incrementer = w3.eth.contract(address=contract_adds, abi=abi)

# 5. Call Contract
number = Incrementer.functions.number().call()

print(f'The current number stored is: { number } ')