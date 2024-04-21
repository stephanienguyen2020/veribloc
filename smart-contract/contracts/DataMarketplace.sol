// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract DataMarketplace {
    address public owner;
    uint256 public studyCount = 0;

    struct Study {
        address researcher;
        uint256 budget;
        uint256 participantTarget;
        uint256 amountPerParticipant;
        uint256 participantCount;
        bool completed;
        mapping(address => bool) participants;
    }

    mapping(uint256 => Study) public studies;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    function createStudy(uint256 _budget, uint256 _participantTarget) external returns (uint256) {
        require(_budget > 0, "Budget must be greater than zero.");
        require(_participantTarget > 0, "Participant target must be greater than zero.");

        uint256 studyId = studyCount++;
        Study storage s = studies[studyId];
        s.researcher = msg.sender;
        s.budget = _budget;
        s.participantTarget = _participantTarget;
        s.amountPerParticipant = _budget / _participantTarget;
        s.participantCount = 0;
        s.completed = false;

        return studyId;
    }

    function joinStudy(uint256 studyId) external {
        Study storage s = studies[studyId];
        require(s.participantCount < s.participantTarget, "This study already reached its participant target.");
        require(!s.completed, "This study is already completed.");
        require(s.participants[msg.sender] == false, "You have already joined this study.");

        s.participants[msg.sender] = true;
        s.participantCount++;

        if (s.participantCount == s.participantTarget) {
            completeStudy(studyId);
        }
    }

    function completeStudy(uint256 studyId) public {
        Study storage s = studies[studyId];
        require(msg.sender == s.researcher || msg.sender == owner, "Only the researcher or owner can complete the study.");
        require(!s.completed, "This study is already completed.");
        require(s.participantCount == s.participantTarget, "Participant target not reached.");

        for (uint256 i = 0; i < s.participantCount; i++) {
            payable(msg.sender).transfer(s.amountPerParticipant);
        }
        s.completed = true;
    }

    function refundStudy(uint256 studyId) external {
        Study storage s = studies[studyId];
        require(msg.sender == s.researcher, "Only the researcher can refund the study.");
        require(!s.completed, "The study is already completed.");
        require(s.participantCount < s.participantTarget, "The participant target has been reached.");

        uint256 refundAmount = s.budget - (s.amountPerParticipant * s.participantCount);
        payable(s.researcher).transfer(refundAmount);
        s.completed = true; // Prevent further actions
    }
}