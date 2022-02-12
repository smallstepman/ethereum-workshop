### plan
0. swap eth for weth
1. deposit some eth into aave
2. borrow some sset with the eth collaterl 
3. sell that borrowed assed (short selling)
4. repay everythng back

### testing
integration tests: kovan
uni tests: mainnet-fork

### result
```shell
❯ brownie run scripts/aave_borrow.py --network kovan
Brownie v1.17.1 - Python development framework for Ethereum

EthDefiProject is the active project.

Running 'scripts/aave_borrow.py::main'...
approving erc20 token
Transaction sent: 0x4f5b514c04d43e34813ddd3c053758c0d7b6700bd49796db6de0b2c8f69743b1
  Gas price: 2.500000007 gwei   Gas limit: 28805   Nonce: 15
  IERC20.approve confirmed   Block: 28765205   Gas used: 26187 (90.91%)

  IERC20.approve confirmed   Block: 28765205   Gas used: 26187 (90.91%)
approved!
Depositing...
Transaction sent: 0x31bd77f143fb5ab508eb2e23f619dcffea54d2e1bfd9c6c3c48123251b209875
  Gas price: 2.500000007 gwei   Gas limit: 207906   Nonce: 16
  ILendingPool.deposit confirmed   Block: 28765207   Gas used: 181716 (87.40%)

  ILendingPool.deposit confirmed   Block: 28765207   Gas used: 181716 (87.40%)

Deposited
you have 0.200004962701833619 worth of ETH deposited.
you have 0.076287699700206095 worth of ETH borrowed.
you can borrow 0.0837162704612608 worth of ETH deposited.
lets borrow
the DAI/ETH price is 0.0002617356248681
Transaction sent: 0xd4946a7c0dc3d5ea4fc23c1cf5db99a4496e2e04900696aa629af0bc084399aa
  Gas price: 2.500000007 gwei   Gas limit: 330966   Nonce: 17
  ILendingPool.borrow confirmed   Block: 28765208   Gas used: 299518 (90.50%)

  ILendingPool.borrow confirmed   Block: 28765208   Gas used: 299518 (90.50%)

we borrowed some dai 
you have 0.200005011930570698 worth of ETH deposited.
you have 0.155818157393564229 worth of ETH borrowed.
you can borrow 0.004185852150892329 worth of ETH deposited.
approving erc20 token
Transaction sent: 0x591708375a0a3621bae5b4b8cee6debeb16f87d70221ce7152bc861b4ef6bf31

  IERC20.approve confirmed   Block: 28765209   Gas used: 29080 (90.91%)

approved!
Transaction sent: 0xa738271cea37afa925725df999cb30e97929c047a9c08a04625b7b5c7c3d6bb5
  Gas price: 2.500000007 gwei   Gas limit: 243212   Nonce: 19
  ILendingPool.repay confirmed   Block: 28765211   Gas used: 218113 (89.68%)

  ILendingPool.repay confirmed   Block: 28765211   Gas used: 218113 (89.68%)

repaid!

```
