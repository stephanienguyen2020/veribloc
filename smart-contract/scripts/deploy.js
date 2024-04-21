async function main() {
    const [deployer] = await ethers.getSigners();
  
    console.log("Deploying contracts with the account:", deployer.address);
  
    const DataMarketplace = await ethers.getContractFactory("DataMarketplace");
    const dataMarketplace = await DataMarketplace.deploy();
  
    console.log("DataMarketplace contract deployed to:", dataMarketplace.address);
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
  