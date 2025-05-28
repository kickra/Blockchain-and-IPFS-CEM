// SPDX-License-Identifier: MIT
pragma solidity >= 0.4.0 <= 0.9;

contract Evidence {
    string public lab;
    string public hospital;
    string public police;
    string public court;
    string public users;

    function setlab(string memory ud) public {
        lab = ud;	
    }

    function getlab() public view returns (string memory) {
        return lab;
    }

    function sethospital(string memory pd) public {
        hospital = pd;	
    }

    function gethospital() public view returns (string memory) {
        return hospital;
    }

    function setpolice(string memory ra) public {
        police = ra;	
    }

    function getpolice() public view returns (string memory) {
        return police;
    }

    function setcourt(string memory ca) public {
        court = ca;	
    }

    function getcourt() public view returns (string memory) {
        return court;
    }
    
    function setuser(string memory pa) public {
        users = pa;	
    }

    function getuser() public view returns (string memory) {
        return users;
    }

    constructor() public {
    lab = "";
	hospital = "";
    police = "";
    court = "";
    users = "";
    }
}