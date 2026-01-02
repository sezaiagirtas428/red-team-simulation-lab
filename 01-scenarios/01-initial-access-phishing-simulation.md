# Scenario 01 — Initial Access via Phishing (Simulation)

## Objective
Document a realistic **phishing-based initial access scenario** from a red team perspective, focusing on attacker intent, potential system artifacts, and defender detection opportunities — without performing any real malicious activity.

## Scope and Safety Constraints
- No real phishing emails are sent
- No credentials are collected
- No malware or exploit code is used
- Scenario is **documentation and simulation only**
- All analysis is performed in a **controlled lab environment**

## Assumptions / Preconditions
- Windows test system (physical or virtual machine)
- Standard (non-administrative) user context
- Default or near-default Windows security configuration

## Attack Narrative (Simulated)
1) An attacker prepares a **socially convincing lure**, such as a fake invoice or notification document name.
2) The lure relies on **social engineering**, not technical exploitation, to convince the user to open the file.
3) In a real-world attack, this action could lead to:
   - Execution of a malicious payload
   - Credential harvesting
   - Establishment of an initial foothold
4) This scenario **does not execute** those actions, but documents the expected outcomes.

## Expected System Artifacts and Telemetry
If this were a real attack, defenders might observe:
- File downloaded to the user's Downloads directory
- Browser download history entries
- SmartScreen warnings or prompts
- Windows Defender detections or alerts
- Relevant Windows Event Log entries (Security / Defender)

## MITRE ATT&CK Mapping
- **Tactic:** TA0001 – Initial Access
- **Technique:** T1566 – Phishing

## Detection Opportunities
- Monitoring of newly downloaded files with uncommon or deceptive names
- Alerts triggered by SmartScreen or Defender
- User-reported suspicious attachments or files
- Correlation of download events with subsequent execution attempts

## Mitigation and Hardening Recommendations
- Security awareness training for end users
- Enforced SmartScreen and Defender protections
- Blocking or restricting risky file types from email and browsers
- Application control policies where applicable

## Validation Checklist
- [ ] Scenario remains fully non-malicious and ethical
- [ ] Attacker behavior and defender perspective are clearly described
- [ ] Relevant logs and artifacts are identified
- [ ] MITRE ATT&CK techniques are correctly mapped
