// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

//@dev: 1. Deploy, 2. whitelist, 3. mint
contract SolarSpunkerNFT is ERC721, Ownable {
    struct SolarSpunker {
        address user;
        uint256 constantPowerConsumption;
        uint256 constantPowerProduction;
        uint256 latestPowerConsumption; 
        uint256 latestPowerProduction;
        bool avsApproved; 
    }

    SolarSpunker[] public solarSpunkers;
    mapping(address => bool) public whitelistedAddresses;
    mapping(address => SolarSpunker) public mapSpunker;

    event HourlyPowerConsumption(address indexed user, uint256 consumption);
    event HourlyPowerProduction(address indexed user, uint256 production);
    event NewSpunkerJoined(address indexed user);

    string public TokenUri;

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _TokenUri
    ) ERC721(_name, _symbol) Ownable(msg.sender) {
        TokenUri = _TokenUri;
    }

    modifier onlyWhitelisted() {
        require(whitelistedAddresses[msg.sender], "Not whitelisted");
        _;
    }

    //@dev: called by AVS operator via MA. Olas FSM if User staked and got AVS approved
    function approvedAVS(address _approveSpunker) public onlyOwner {
        SolarSpunker storage spunker = mapSpunker[_approveSpunker];
        require(spunker.avsApproved == false, "AVS already approved");
        spunker.avsApproved = true;
    }

    function addWhitelistedAddress(address _address) public onlyOwner {
        whitelistedAddresses[_address] = true;
    }

    function mint(
        address _to,
        uint256 _constantPowerConsumption,
        uint256 _constantPowerProduction,
        uint256 _latestPowerConsumption,
        uint256 _latestPowerProduction
    ) public onlyWhitelisted {
        uint256 tokenId = solarSpunkers.length;
        SolarSpunker memory newSpunker = SolarSpunker({
            user: _to,
            constantPowerConsumption: _constantPowerConsumption,
            constantPowerProduction: _constantPowerProduction,
            latestPowerConsumption: _latestPowerConsumption,
            latestPowerProduction: _latestPowerProduction,
            avsApproved: false
        });
        solarSpunkers.push(newSpunker);
        mapSpunker[_to] = newSpunker;
        _safeMint(_to, tokenId);
        emit NewSpunkerJoined(_to);
    }

    function emitHourlyPowerConsumption(uint256 _hourlyPowerConsumption) public {
    SolarSpunker storage spunker = mapSpunker[msg.sender];
    require(spunker.user == msg.sender, "You are not the owner");
    require(spunker.avsApproved, "AVS not approved");
    spunker.latestPowerConsumption = _hourlyPowerConsumption;
    emit HourlyPowerConsumption(spunker.user, _hourlyPowerConsumption);
}

function emitHourlyPowerProduction(uint256 _hourlyPowerProduction) public {
    SolarSpunker storage spunker = mapSpunker[msg.sender];
    require(spunker.user == msg.sender, "You are not the owner");
    require(spunker.avsApproved, "AVS not approved");
    spunker.latestPowerProduction = _hourlyPowerProduction;
    emit HourlyPowerProduction(spunker.user, _hourlyPowerProduction);
}

}
