// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataMarketplace {
    address public owner;
    uint256 public studyCount = 0;

    enum StudyStatus { Active, Completed, InDispute, Resolved }

    struct Study {
        address researcher;
        uint256 budget;
        uint256 participantTarget;
        uint256 amountPerParticipant;
        uint256 participantCount;
        bool verified;
        StudyStatus status;
        mapping(address => bool) participants;
    }

    mapping(uint256 => Study) public studies;
    mapping(uint256 => mapping(address => bool)) public disputes;

    constructor() {
        owner = msg.sender;
    }

    // Event to request off-chain verification
    event RequestVerification(uint256 indexed studyId);

    function createStudy(uint256 _budget, uint256 _participantTarget) external returns (uint256) {
        uint256 studyId = studyCount++;
        Study storage s = studies[studyId];
        s.researcher = msg.sender;
        s.budget = _budget;
        s.participantTarget = _participantTarget;
        s.amountPerParticipant = _budget / _participantTarget;
        s.participantCount = 0;
        s.verified = false;
        s.status = StudyStatus.Active;
        return studyId;
    }

    function joinStudy(uint256 studyId) external {
        Study storage s = studies[studyId];
        require(s.status == StudyStatus.Active, "Study is not active.");
        require(s.participantCount < s.participantTarget, "Participant target reached.");
        require(!s.participants[msg.sender], "Already joined this study.");

        s.participants[msg.sender] = true;
        s.participantCount++;

        if (s.participantCount == s.participantTarget) {
            emit RequestVerification(studyId);
        }
    }

    function verifyStudy(uint256 studyId, bool isVerified) external {
        require(msg.sender == owner, "Only the owner can verify the study.");
        Study storage s = studies[studyId];
        require(s.status == StudyStatus.Active, "The study is not active.");
        require(!s.completed, "The study is already completed.");

        s.verified = isVerified;
        if (isVerified) {
            completeStudy(studyId);
        } else {
            s.status = StudyStatus.InDispute; // Change status to in dispute if verification fails
        }
    }

    function fileDispute(uint256 studyId) external {
        Study storage s = studies[studyId];
        require(s.status == StudyStatus.Completed, "Study must be completed to file disputes.");
        require(s.participants[msg.sender], "Only participants can file disputes.");

        disputes[studyId][msg.sender] = true;
        s.status = StudyStatus.InDispute;
    }

    function resolveDispute(uint256 studyId, bool success) external {
        require(msg.sender == owner, "Only the owner can resolve disputes.");
        Study storage s = studies[studyId];
        require(s.status == StudyStatus.InDispute, "There is no ongoing dispute for this study.");

        if (success) {
            s.status = StudyStatus.Resolved;
            payoutParticipants(studyId);
        } else {
            refundResearcher(studyId);
        }
    }

    function completeStudy(uint256 studyId) private {
        Study storage s = studies[studyId];
        require(s.verified, "Study must be verified before completion.");
        s.status = StudyStatus.Completed;

        for (uint256 i = 0; i < s.participantCount; i++) {
            payable(s.participants[i]).transfer(s.amountPerParticipant);
        }
    }

    function refundStudy(uint256 studyId) private {
        Study storage s = studies[studyId];
        uint256 remainingFunds = s.budget - (s.amountPerParticipant * s.participantCount);
        payable(s.researcher).transfer(remainingFunds);
        s.completed = true; // Prevent further actions
    }

    function payoutParticipants(uint256 studyId) private {
        Study storage s = studies[studyId];
        for (uint256 i = 0; i < s.participantCount; i++) {
            payable(s.participants[i]).transfer(s.amountPerParticipant);
        }
    }
}
