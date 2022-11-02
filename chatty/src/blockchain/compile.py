import solcx
from solcx import compile_source

# 2. If you haven't already installed the Solidity compiler, uncomment the following line
# solcx.install_solc()

contract_file = solcx.compile_files(
    '/Users/ldminh/Training/Python/Django/chatty/chatty/src/blockchain/incrementer.sol',
    output_values=['abi','bin'])

# export contract data
abi = contract_file['incrementer.sol:Incrementer']['abi']
byte_code = contract_file['incrementer.sol:Incrementer']['bin']
