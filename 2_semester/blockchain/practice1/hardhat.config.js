require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.18",
  etherscan: {
    apiKey: "TFR1IF5VI6HQH49SF9XB88S71M61I1QPD9c;e"
  },
  networks: {
    sepolia: {
      url: 'https://eth-sepolia.g.alchemy.com/v2/-qOk9JIqJTpuqJXrVnLTt0fkMj4xImp8',
      accounts: ['2efbd57df4a01dbb198e5f577da24d33a689b850e0d4d0a48ffce0ef86bde650']
    }
  }
};
