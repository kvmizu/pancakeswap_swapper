from web3 import Web3
import json
import time

# Connect to BNB Chain (Use your own BSC node or Infura/Alchemy if required)
BSC_RPC_URL = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(BSC_RPC_URL))

# Your wallet private key and address
PRIVATE_KEY = "your_private_key_here"
WALLET_ADDRESS = "your_wallet_address_here"

# PancakeSwap Router V2 Contract (Mainnet)
PANCAKESWAP_ROUTER = "0x10ED43C718714eb63d5aA57B78B54704E256024E"

# Load PancakeSwap Router ABI
PANCAKESWAP_ABI = json.loads('[{"constant":false,"inputs":[{"name":"amountIn","type":"uint256"},{"name":"amountOutMin","type":"uint256"},{"name":"path","type":"address[]"},{"name":"to","type":"address"},{"name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

# Token contract addresses (Change these to your tokens)
TOKEN_IN = "0x...Your_Token_Address"   # Token you are swapping from
TOKEN_OUT = "0x...Your_Token_Address"  # Token you are swapping to

# Amount to swap (in smallest unit, e.g., 1 token with 18 decimals = 1000000000000000000)
AMOUNT_IN = web3.to_wei(1, 'ether')  # Adjust accordingly

# Approve the transaction first
def approve_token(spender, amount, token_address):
    token_abi = json.loads('[{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
    token_contract = web3.eth.contract(address=web3.to_checksum_address(token_address), abi=token_abi)

    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
    txn = token_contract.functions.approve(spender, amount).build_transaction({
        'from': WALLET_ADDRESS,
        'gas': 200000,
        'gasPrice': web3.to_wei('5', 'gwei'),
        'nonce': nonce
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Approval Transaction Sent! TxHash: {web3.to_hex(tx_hash)}")

    # Wait for approval transaction confirmation
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Approval Confirmed!")

# Swap Tokens Function
def swap_tokens():
    router_contract = web3.eth.contract(address=web3.to_checksum_address(PANCAKESWAP_ROUTER), abi=PANCAKESWAP_ABI)
    
    # Define swap parameters
    amount_out_min = 0  # Set to 0 to accept any amount, adjust for slippage tolerance
    path = [web3.to_checksum_address(TOKEN_IN), web3.to_checksum_address(TOKEN_OUT)]
    deadline = int(time.time()) + 60  # 1-minute deadline

    # Get nonce
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)

    # Build swap transaction
    txn = router_contract.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(
        AMOUNT_IN, amount_out_min, path, WALLET_ADDRESS, deadline
    ).build_transaction({
        'from': WALLET_ADDRESS,
        'gas': 300000,
        'gasPrice': web3.to_wei('5', 'gwei'),
        'nonce': nonce
    })

    # Sign and send the transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Swap Transaction Sent! TxHash: {web3.to_hex(tx_hash)}")

    # Wait for transaction confirmation
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Swap Successful!", receipt)

# Execute the functions
approve_token(PANCAKESWAP_ROUTER, AMOUNT_IN, TOKEN_IN)  # First approve
swap_tokens()  # Then swap
