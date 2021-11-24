pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ArtemToken is ERC20 {
    constructor() public ERC20("Artem Token", "ART") {
        _mint(msg.sender, 1000000000000000000000000); // 1 000 000 * 10 *18
    }
}
