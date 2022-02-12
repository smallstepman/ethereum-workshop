#!/usr/bin/env python3
import os
import json
from solcx import compile_standard
from rich import print
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open('./SimpleStorage.sol') as f:
    simple_storage_file = f.read()

compile_sol = compile_standard({
    "language": "Solidity",
    "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
            }
        }
    }},
    solc_version="0.8.10")

with open('compiled_code.json', 'w') as f:
    json.dump(compile_sol, f)

bytecode = compile_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']
abi = compile_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

# node_address = "https://mainnet.infura.io/v3/07eb858b5da44faa8cd0686663605874"
# node_address = "HTTP://127.0.0.1:8545"
node_address = "https://rinkeby.infura.io/v3/07eb858b5da44faa8cd0686663605874"
w3 = Web3(Web3.HTTPProvider(node_address))
chain_id = 4 #1337
my_address = "0x9C7FC26739d80595A19fC2bc1FF5e965fc03e26b"
pkey = os.getenv('PRIVATE_KEY')

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce = w3.eth.getTransactionCount(my_address)
print(SimpleStorage)
tx = SimpleStorage.constructor().buildTransaction({
    "chainId":chain_id,
    "from": my_address,
    "nonce": nonce,
    "gasPrice": w3.eth.gasPrice
})

txsign = w3.eth.account.signTransaction(tx, pkey)
txhash = w3.eth.send_raw_transaction(txsign.rawTransaction)
txreceipt = w3.eth.wait_for_transaction_receipt(txhash)


simple_storage = w3.eth.contract(abi=abi, address=txreceipt['contractAddress'])
print(simple_storage.functions.retrieve().call())
print(simple_storage.functions.store(18).call())
nonce = w3.eth.getTransactionCount(my_address)
tx = simple_storage.functions.store(15).buildTransaction({
    "chainId":chain_id,
    "from": my_address,
    "nonce": nonce,
    "gasPrice": w3.eth.gasPrice
})
txsign = w3.eth.account.signTransaction(tx, pkey)
txhash = w3.eth.send_raw_transaction(txsign.rawTransaction)
txreceipt = w3.eth.wait_for_transaction_receipt(txhash)

print(simple_storage.functions.retrieve().call())
