# PancakeSwap Token Swapper

This Python script allows you to swap memecoins (or any BEP-20 tokens) on PancakeSwap using Binance Smart Chain (BSC) via Web3.py.

## Features
- Connects to Binance Smart Chain (BSC) using Web3.py.
- Approves PancakeSwap to spend tokens.
- Swaps a specified token for another on PancakeSwap.
- Waits for transaction confirmation.

## Prerequisites
### 1. Install Dependencies
Ensure you have Python 3 installed, then install Web3.py:
```bash
pip install web3
```

### 2. Configure BSC Wallet
You need:
- A **wallet address** (e.g., MetaMask, Trust Wallet)
- A **private key** (for signing transactions)
- Some **BNB** for gas fees

### 3. Setup Token Addresses
Find the **contract addresses** for the tokens you want to swap.

## Usage
### 1. Update Configuration
Edit the script with:
- `PRIVATE_KEY`: Your wallet's private key
- `WALLET_ADDRESS`: Your BSC wallet address
- `TOKEN_IN`: Contract address of the token you are swapping **from**
- `TOKEN_OUT`: Contract address of the token you are swapping **to**
- `AMOUNT_IN`: Amount of tokens to swap (in smallest units, e.g., wei)

### 2. Run the Script
```bash
python swap_tokens.py
```

## How It Works
1. **Approves PancakeSwap Router** to spend the specified tokens.
2. **Executes the swap** on PancakeSwap.
3. **Waits for transaction confirmation** and displays the result.

## Security Considerations
- **Do not share your private key!** Store it securely.
- **Use testnet first** before executing on the mainnet.
- **Monitor gas fees** before confirming transactions.

## Troubleshooting
- Ensure you have **BNB** for transaction fees.
- Use a **reliable BSC node** (default: `https://bsc-dataseed.binance.org/`).
- If transactions fail, check the **token contract addresses** and **wallet balance**.

## License
This project is licensed under the MIT License.

