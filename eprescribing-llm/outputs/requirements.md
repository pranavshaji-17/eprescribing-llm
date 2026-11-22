# Generated requirements: e-Prescribing

Total: **59** requirements (CON: 2, FR: 35, NFR: 8, REG: 14). Flagged NEEDS-VALIDATION: **0**.

## Summary table

| ID | Type | Priority | Statement | Sources |
|---|---|---|---|---|
| REQ-UC1-01 | FR | Must | The system shall create one MedicationRequest instance per drug in a multi-drug prescription. | FHIR-02 |
| REQ-UC1-02 | FR | Must | The system shall associate each MedicationRequest with a Patient, Practitioner, and Encounter resource. | FHIR-04 |
| REQ-UC1-03 | FR | Must | The system shall represent the prescription intent only, without recording administration status or events of actual medication delivery. | FHIR-01 |
| REQ-UC1-04 | FR | Must | The system shall allow a prescriber to cancel or change a prescription after it has been issued, with status updates reflecting the new intent via the status and intent elements of the MedicationRequest resource. | FHIR-05, PROJ-04 |
| REQ-UC1-05 | REG | Must | The system shall require two-factor authentication for controlled substance prescriptions during the signing process. | PROJ-04 |
| REQ-UC1-06 | NFR | Must | The system shall maintain an immutable audit trail for all actions related to prescription creation, modification, and transmission that includes timestamps, user IDs, and action types. | PROJ-04 |
| REQ-UC2-01 | FR | Must | The system shall perform drug-drug interaction, allergy, and dosing checks against a drug knowledge base before finalizing a medication order. | PROJ-03, PROJ-01 |
| REQ-UC2-02 | FR | Must | The system shall display all safety check alerts to the prescriber before allowing finalization of the medication order. | PROJ-03, PROJ-01 |
| REQ-UC2-03 | FR | Must | The system shall use a standardized drug knowledge base interface to retrieve interaction and allergy data for each medication order. | PROJ-02, PROJ-03 |
| REQ-UC2-04 | REG | Must | The system shall log all safety check results, including alerts and their resolution status, in an audit trail for each medication order. | PROJ-03, PROJ-04 |
| REQ-UC2-05 | FR | Must | The system shall not allow finalization of a medication order if any critical safety alert (e.g., severe allergy or fatal interaction) is present in the drug knowledge base check results. | PROJ-03, PROJ-01 |
| REQ-UC2-06 | FR | Must | The system shall ensure that all safety checks are performed independently of prescriber input and based solely on drug knowledge base data. | PROJ-03, PROJ-01 |
| REQ-UC3-01 | FR | Must | The system shall allow a prescriber to cancel or change an existing medication order after it has been issued. | PROJ-04 |
| REQ-UC3-02 | FR | Must | The system shall transmit a change request transaction to the pharmacy using the NCPDP SCRIPT standard when a prescriber modifies an issued order. | SCRIPT-02 |
| REQ-UC3-03 | FR | Must | The system shall transmit a cancel transaction to the pharmacy using the NCPDP SCRIPT standard when a prescriber cancels an issued order. | SCRIPT-02 |
| REQ-UC3-04 | FR | Must | The system shall update the MedicationRequest resource in the FHIR representation to reflect the new or cancelled status when a change or cancellation is made. | FHIR-05 |
| REQ-UC3-05 | REG | Must | The system shall support upgrading to new mandated versions of the NCPDP SCRIPT standard as required by CMS. | SCRIPT-03 |
| REQ-UC3-06 | NFR | Must | The system shall maintain a full audit trail of all cancel or change actions, including timestamp, prescriber identity, and action type, for review by compliance officers. | PROJ-04 |
| REQ-UC4-01 | FR | Must | The system shall transmit a signed prescription to the pharmacy system using the NCPDP SCRIPT message format. | SCRIPT-01 |
| REQ-UC4-02 | FR | Must | The system shall use the appropriate NCPDP SCRIPT transaction type to transmit the prescription, based on whether it is a new order, change request, refill, or cancellation. | SCRIPT-02 |
| REQ-UC4-03 | REG | Must | The system shall support upgrading to new mandated versions of NCPDP SCRIPT as required by CMS regulations. | SCRIPT-03 |
| REQ-UC4-04 | FR | Should | The system shall include a fill status update message in response to pharmacy confirmation of prescription fulfillment. | SCRIPT-02 |
| REQ-UC4-05 | NFR | Must | The system shall maintain an immutable audit trail of all transmission events including timestamps, message content, and recipient details. | PROJ-04 |
| REQ-UC4-06 | FR | Must | The system shall ensure that all transmitted prescriptions include a digital signature that is cryptographically valid and tied to the prescriber's credentials. | PROJ-04 |
| REQ-UC5-01 | FR | Must | The system shall allow the prescriber to electronically sign a prescription after completing safety checks and before transmission. | PROJ-03, PROJ-04 |
| REQ-UC5-02 | REG | Must | The system shall verify the prescriber's identity prior to allowing electronic signing of any prescription for controlled substances. | DEA-02 |
| REQ-UC5-03 | REG | Must | The system shall maintain a full audit trail of all events related to the creation, signing, and transmission of prescriptions for controlled substances. | DEA-06 |
| REQ-UC5-04 | FR | Must | The system shall enforce two-factor authentication when signing prescriptions containing controlled substances. | PROJ-04 |
| REQ-UC5-05 | FR | Must | The system shall not allow a prescription to be signed without prior completion of safety checks for drug interactions and allergies. | PROJ-03, PROJ-04 |
| REQ-UC5-06 | NFR | Must | The system shall ensure that all signed prescriptions are time-stamped with a precise timestamp at the moment of signing. | DEA-06, PROJ-03 |
| REQ-UC6-01 | FR | Must | The system shall require two-factor authentication at the moment of signing for controlled substance prescriptions, with one factor originating from a separate device or token. | DEA-03 |
| REQ-UC6-02 | FR | Must | The system shall enforce that two-factor authentication for signing is applied exclusively to controlled substance prescriptions and not to non-controlled substances. | DEA-03, PROJ-04 |
| REQ-UC6-03 | REG | Must | The system shall record the time, date, and identity of both authentication factors used during the two-factor signing process for each controlled substance prescription in an immutable audit trail. | DEA-06, PROJ-03 |
| REQ-UC6-04 | FR | Must | The system shall not allow a prescription to be signed with two-factor authentication if the prescriber's identity has not been verified through a separate credential provider prior to signing. | PROJ-04, DEA-03 |
| REQ-UC6-05 | NFR | Must | The system shall ensure that all events related to two-factor authentication for controlled substance prescriptions are logged and retained for at least five years from the date of the prescription event. | DEA-06 |
| REQ-UC6-06 | CON | Must | The system shall not allow a prescriber to sign a controlled substance prescription using the same device or token as their primary login credentials unless explicitly configured by an authorized credential provider with two-factor authentication enabled on a separate device. | DEA-03 |
| REQ-UC7-01 | FR | Must | The system shall verify the prescriber's identity using credentials provided by a credential provider before allowing the creation of an electronic prescription for a controlled substance. | DEA-02 |
| REQ-UC7-02 | FR | Must | The system shall require two-factor authentication as part of the identity verification process when creating prescriptions for controlled substances. | PROJ-04, DEA-02 |
| REQ-UC7-03 | FR | Must | The system shall record the timestamp, method, and outcome of each prescriber identity verification attempt in an immutable audit trail. | PROJ-01, PROJ-04 |
| REQ-UC7-04 | REG | Must | The system shall not allow a prescriber to create or sign a prescription for a controlled substance unless the identity verification has been successfully completed by a credential provider. | DEA-02 |
| REQ-UC7-05 | CON | Should | The system shall ensure that the credential provider's identity proofing method is interoperable with the e-prescribing platform using standardized protocols such as OAuth or SAML for secure authentication. | PROJ-02, SCRIPT-01 |
| REQ-UC8-01 | FR | Must | The system shall record and provide access to a full audit trail of all events related to the creation, signing, transmission, and security aspects of controlled-substance prescriptions. | DEA-06, PROJ-03 |
| REQ-UC8-02 | FR | Must | The system shall allow the compliance officer to filter and search audit trail entries by date, prescriber, drug type, prescription status, and event type. | PROJ-03, PROJ-04 |
| REQ-UC8-03 | REG | Must | The system shall retain audit trail records for a minimum of 7 years from the date of the last prescription event involving a controlled substance. | DEA-06 |
| REQ-UC8-04 | FR | Must | The system shall generate a timestamped, immutable log entry for each audit trail event that includes the user ID, action type, timestamp, and associated prescription identifier. | DEA-06, PROJ-03 |
| REQ-UC8-05 | REG | Must | The system shall support third-party auditing of its audit trail functionality at least every two years or whenever a significant change to the software occurs. | DEA-04 |
| REQ-UC8-06 | NFR | Must | The system shall ensure that all audit trail records are stored in an encrypted format and accessible only to authorized personnel with appropriate roles and permissions. | DEA-06, PROJ-01 |
| REQ-UC9-01 | FR | Must | The system shall lock controlled-substance prescribing functionality when an audit failure is detected. | DEA-05, PROJ-04 |
| REQ-UC9-02 | REG | Must | The system shall notify the DEA within 1 business day of any audit failure involving a controlled substance prescription. | DEA-05 |
| REQ-UC9-03 | REG | Must | The system shall maintain a full audit trail of all events related to controlled-substance prescriptions during periods when prescribing is locked due to an audit failure. | DEA-06, PROJ-04 |
| REQ-UC9-04 | FR | Must | The system shall only allow the compliance officer to unlock controlled-substance prescribing after an audit failure has been resolved and verified by a third-party auditor. | DEA-04, PROJ-04 |
| REQ-UC9-05 | NFR | Must | The system shall record the reason for each audit failure in the audit trail when controlled-substance prescribing is locked. | DEA-06, PROJ-04 |
| REQ-UC9-06 | FR | Must | The system shall not allow any changes to controlled-substance prescriptions while prescribing is locked due to an audit failure. | PROJ-04 |
| REQ-XC-01 | REG | Must | The system shall support the transmission of prescriptions using current and mandated versions of the NCPDP SCRIPT standard. | SCRIPT-03 |
| REQ-XC-02 | FR | Must | The system shall perform real-time safety checks for drug interactions, allergies, and correct dosing during prescription creation. | PROJ-01 |
| REQ-XC-03 | REG | Must | The system shall maintain a full audit trail of all events related to controlled-substance prescriptions, including creation, signing, transmission, and cancellation. | DEA-06 |
| REQ-XC-04 | FR | Must | The system shall verify prescriber identity using two-factor authentication before allowing the creation or signing of a prescription for controlled substances. | PROJ-04 |
| REQ-XC-05 | NFR | Must | The system shall ensure that all prescription transmissions are securely encrypted in transit using TLS 1.2 or higher. | PROJ-01 |
| REQ-XC-06 | FR | Must | The system shall automatically detect and notify the prescriber when a prescribed drug is flagged for interaction or allergy in real time, based on an external drug knowledge base. | PROJ-01 |

## Traceability: use case x requirement type

| Use case | FR | NFR | REG | CON | Total |
|---|---|---|---|---|---|
| UC1 Create medication order | 4 | 1 | 1 | 0 | 6 |
| UC2 Run safety checks | 5 | 0 | 1 | 0 | 6 |
| UC3 Cancel or change order | 4 | 1 | 1 | 0 | 6 |
| UC4 Transmit to pharmacy | 4 | 1 | 1 | 0 | 6 |
| UC5 Sign prescription | 3 | 1 | 2 | 0 | 6 |
| UC6 Two-factor signing | 3 | 1 | 1 | 1 | 6 |
| UC7 Verify prescriber ID | 3 | 0 | 1 | 1 | 5 |
| UC8 Review audit trail | 3 | 1 | 2 | 0 | 6 |
| UC9 Lock on audit failure | 3 | 1 | 2 | 0 | 6 |
| XC Cross-cutting qualities | 3 | 1 | 2 | 0 | 6 |

## Requirements with reasoning

### UC1 Create medication order

**REQ-UC1-01** (FR, Must)

- **Statement:** The system shall create one MedicationRequest instance per drug in a multi-drug prescription.
- **Actor:** Prescriber
- **Reasoning:** Each medication order must be represented as a separate resource instance to ensure accurate tracking and safety checks for individual drugs, as per HL7 FHIR standards.
- **Acceptance criteria:** A prescription with multiple drugs results in exactly one MedicationRequest instance per drug, verified by querying the system's medication request list.
- **Source FHIR-02:** One resource instance is one medication order (HL7 FHIR MedicationRequest resource) https://hl7.org/fhir/medicationrequest.html

**REQ-UC1-02** (FR, Must)

- **Statement:** The system shall associate each MedicationRequest with a Patient, Practitioner, and Encounter resource.
- **Actor:** Prescriber
- **Reasoning:** These associations provide essential context for the prescription, enabling accurate patient identification, prescriber accountability, and care setting tracking as required by FHIR standards.
- **Acceptance criteria:** Each MedicationRequest instance must include valid references to a Patient, Practitioner, and Encounter resource in its metadata.
- **Source FHIR-04:** Relationships to other resources (HL7 FHIR MedicationRequest resource) https://hl7.org/fhir/medicationrequest.html

**REQ-UC1-03** (FR, Must)

- **Statement:** The system shall represent the prescription intent only, without recording administration status or events of actual medication delivery.
- **Actor:** Prescriber
- **Reasoning:** MedicationRequest is defined as an order of intent, not a record of administration; this ensures compliance with FHIR semantics and prevents misinterpretation of prescription status.
- **Acceptance criteria:** The system shall not include any field indicating that medication has been administered to the patient in the MedicationRequest instance.
- **Source FHIR-01:** Purpose: an order, not an administration (HL7 FHIR MedicationRequest resource) https://hl7.org/fhir/medicationrequest.html

**REQ-UC1-04** (FR, Must)

- **Statement:** The system shall allow a prescriber to cancel or change a prescription after it has been issued, with status updates reflecting the new intent via the status and intent elements of the MedicationRequest resource.
- **Actor:** Prescriber
- **Reasoning:** The ability to modify prescriptions post-issue is critical for patient safety and clinical workflow, supported by FHIR's status and intent fields which track the lifecycle of a request.
- **Acceptance criteria:** A prescriber can update the status (e.g., from 'active' to 'cancelled') or intent (e.g., from 'order' to 'proposal') of an existing MedicationRequest, and these changes are reflected in the resource instance.
- **Source FHIR-05:** Lifecycle: status and intent (HL7 FHIR MedicationRequest resource) https://hl7.org/fhir/medicationrequest.html
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC1-05** (REG, Must)

- **Statement:** The system shall require two-factor authentication for controlled substance prescriptions during the signing process.
- **Actor:** Prescriber
- **Reasoning:** Two-factor signing is mandated for controlled substances in the project's use case flow, ensuring stronger prescriber identity verification and compliance with regulatory expectations such as DEA EPCS rules.
- **Acceptance criteria:** All prescriptions involving controlled substances must trigger a two-factor authentication step before finalizing the signature process.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC1-06** (NFR, Must)

- **Statement:** The system shall maintain an immutable audit trail for all actions related to prescription creation, modification, and transmission that includes timestamps, user IDs, and action types.
- **Actor:** Prescriber
- **Reasoning:** An immutable audit trail is essential for compliance with regulatory requirements and for accountability in cases of errors or misuse, as required by the project's design and use case flow.
- **Acceptance criteria:** All actions (e.g., creation, cancellation) are logged with a timestamp, user identifier, and action type, and these logs cannot be altered after recording.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

### UC2 Run safety checks

**REQ-UC2-01** (FR, Must)

- **Statement:** The system shall perform drug-drug interaction, allergy, and dosing checks against a drug knowledge base before finalizing a medication order.
- **Actor:** Drug knowledge base
- **Reasoning:** Medication errors due to missed interactions or allergies are common in paper-based systems. Running safety checks before finalization prevents such errors and aligns with the project's goal of reducing medication harm.
- **Acceptance criteria:** A prescription is not finalized unless the system returns a clear list of alerts for drug interactions, allergies, or dosing issues that were detected during the check.
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a

**REQ-UC2-02** (FR, Must)

- **Statement:** The system shall display all safety check alerts to the prescriber before allowing finalization of the medication order.
- **Actor:** Prescriber
- **Reasoning:** Visibility of safety alerts ensures prescribers are aware of potential risks, enabling informed decisions and reducing the likelihood of prescribing errors.
- **Acceptance criteria:** The prescriber must see all generated alerts in a clear, actionable format before finalizing the prescription.
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a

**REQ-UC2-03** (FR, Must)

- **Statement:** The system shall use a standardized drug knowledge base interface to retrieve interaction and allergy data for each medication order.
- **Actor:** Drug knowledge base
- **Reasoning:** Standardized interfaces ensure interoperability with external drug databases like First Databank, enabling consistent and reliable safety checks across systems.
- **Acceptance criteria:** The system successfully retrieves interaction and allergy data from a recognized drug knowledge base using a defined interface protocol (e.g., HL7 FHIR or NCPDP).
- **Source PROJ-02:** Actors (Project brief (own work, not an external standard)) n/a
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a

**REQ-UC2-04** (REG, Must)

- **Statement:** The system shall log all safety check results, including alerts and their resolution status, in an audit trail for each medication order.
- **Actor:** Compliance officer
- **Reasoning:** Audit trails are required to demonstrate compliance with regulatory standards and support accountability, especially when investigating medication errors or audit failures.
- **Acceptance criteria:** The audit trail contains a timestamped record of all safety checks performed and the outcome for each prescription order.
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC2-05** (FR, Must)

- **Statement:** The system shall not allow finalization of a medication order if any critical safety alert (e.g., severe allergy or fatal interaction) is present in the drug knowledge base check results.
- **Actor:** Prescriber
- **Reasoning:** Critical safety issues must be prevented from being prescribed to avoid patient harm. This requirement directly addresses the problem of missed allergies and interactions in paper-based systems.
- **Acceptance criteria:** The system blocks finalization when a critical alert (e.g., life-threatening allergy or interaction) is detected during the safety check.
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a

**REQ-UC2-06** (FR, Must)

- **Statement:** The system shall ensure that all safety checks are performed independently of prescriber input and based solely on drug knowledge base data.
- **Actor:** Drug knowledge base
- **Reasoning:** To prevent bias or error due to prescriber oversight, safety checks must be objective and data-driven, ensuring consistent and reliable outcomes.
- **Acceptance criteria:** The system performs all checks using only the drug knowledge base data without relying on prescriber annotations or manual input.
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a

### UC3 Cancel or change order

**REQ-UC3-01** (FR, Must)

- **Statement:** The system shall allow a prescriber to cancel or change an existing medication order after it has been issued.
- **Actor:** Prescriber
- **Reasoning:** This aligns with the target use case description and enables prescribers to correct errors post-issuance, improving patient safety and clinical accuracy.
- **Acceptance criteria:** A prescriber must be able to initiate a cancel or change request for an existing order through the system interface, and the action must be recorded in the audit trail.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC3-02** (FR, Must)

- **Statement:** The system shall transmit a change request transaction to the pharmacy using the NCPDP SCRIPT standard when a prescriber modifies an issued order.
- **Actor:** Prescriber
- **Reasoning:** The NCPDP SCRIPT standard defines a 'change request' transaction type for modifying existing prescriptions, ensuring interoperability and compliance with industry standards.
- **Acceptance criteria:** Upon a change request initiated by the prescriber, the system must send an appropriate SCRIPT transaction to the pharmacy with correct transaction code and data fields.
- **Source SCRIPT-02:** Transaction types (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-UC3-03** (FR, Must)

- **Statement:** The system shall transmit a cancel transaction to the pharmacy using the NCPDP SCRIPT standard when a prescriber cancels an issued order.
- **Actor:** Prescriber
- **Reasoning:** The NCPDP SCRIPT standard includes a 'cancel' transaction type for terminating prescriptions, which ensures pharmacies are informed of the cancellation and can update their records accordingly.
- **Acceptance criteria:** When a prescriber cancels an order, the system must send a SCRIPT cancel transaction to the pharmacy with correct transaction details and status updates.
- **Source SCRIPT-02:** Transaction types (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-UC3-04** (FR, Must)

- **Statement:** The system shall update the MedicationRequest resource in the FHIR representation to reflect the new or cancelled status when a change or cancellation is made.
- **Actor:** Prescriber
- **Reasoning:** The HL7 FHIR MedicationRequest resource uses 'status' and 'intent' elements to represent the lifecycle of a prescription, ensuring accurate state representation in digital records.
- **Acceptance criteria:** After a change or cancellation, the system must update the status field (e.g., from 'active' to 'cancelled') and maintain correct intent values (e.g., 'order') in the FHIR MedicationRequest resource.
- **Source FHIR-05:** Lifecycle: status and intent (HL7 FHIR MedicationRequest resource) https://hl7.org/fhir/medicationrequest.html

**REQ-UC3-05** (REG, Must)

- **Statement:** The system shall support upgrading to new mandated versions of the NCPDP SCRIPT standard as required by CMS.
- **Actor:** Prescriber
- **Reasoning:** CMS mandates specific, evolving versions of the NCPDP SCRIPT standard; compliance requires the system to adapt to these changes over time to remain legally and technically compliant.
- **Acceptance criteria:** The system must detect and support transitions between mandated SCRIPT version updates as defined by CMS, without breaking existing functionality or data exchange.
- **Source SCRIPT-03:** Mandated versions change over time (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-UC3-06** (NFR, Must)

- **Statement:** The system shall maintain a full audit trail of all cancel or change actions, including timestamp, prescriber identity, and action type, for review by compliance officers.
- **Actor:** Compliance officer
- **Reasoning:** Audit trails are essential for accountability, regulatory compliance, and tracing actions that may impact patient safety or drug misuse, especially in controlled substance prescribing.
- **Acceptance criteria:** All cancel or change events must be logged with a timestamp, prescriber ID, action type (e.g., 'change', 'cancel'), and the original order details in an immutable audit log accessible to compliance officers.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

### UC4 Transmit to pharmacy

**REQ-UC4-01** (FR, Must)

- **Statement:** The system shall transmit a signed prescription to the pharmacy system using the NCPDP SCRIPT message format.
- **Actor:** Pharmacy system
- **Reasoning:** NCPDP SCRIPT is the established US standard for exchanging prescription information, ensuring interoperability and consistency across prescriber and pharmacy systems.
- **Acceptance criteria:** The pharmacy system receives a message in NCPDP SCRIPT format with all required fields populated and correctly structured.
- **Source SCRIPT-01:** Purpose (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-UC4-02** (FR, Must)

- **Statement:** The system shall use the appropriate NCPDP SCRIPT transaction type to transmit the prescription, based on whether it is a new order, change request, refill, or cancellation.
- **Actor:** Pharmacy system
- **Reasoning:** Different prescription actions require distinct SCRIPT transaction types to ensure accurate processing and tracking by pharmacy systems.
- **Acceptance criteria:** The transmitted message uses the correct SCRIPT transaction type (e.g., NEW, CHANGE) corresponding to the action being performed.
- **Source SCRIPT-02:** Transaction types (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-UC4-03** (REG, Must)

- **Statement:** The system shall support upgrading to new mandated versions of NCPDP SCRIPT as required by CMS regulations.
- **Actor:** Prescriber
- **Reasoning:** CMS mandates specific, evolving versions of the SCRIPT standard; compliance requires the system to adapt to these changes over time to remain legally and technically compliant.
- **Acceptance criteria:** The system can detect and adopt new mandated SCRIPT version requirements and validate that all outgoing messages conform to the current version.
- **Source SCRIPT-03:** Mandated versions change over time (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-UC4-04** (FR, Should)

- **Statement:** The system shall include a fill status update message in response to pharmacy confirmation of prescription fulfillment.
- **Actor:** Pharmacy system
- **Reasoning:** The SCRIPT standard includes transaction types for tracking fill status, enabling real-time visibility into prescription outcomes and supporting audit trails.
- **Acceptance criteria:** When the pharmacy confirms a fill, the system receives and records this update in its internal state with appropriate metadata.
- **Source SCRIPT-02:** Transaction types (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-UC4-05** (NFR, Must)

- **Statement:** The system shall maintain an immutable audit trail of all transmission events including timestamps, message content, and recipient details.
- **Actor:** Pharmacy system
- **Reasoning:** An immutable audit trail is essential for compliance with regulatory requirements and for verifying accountability in case of errors or misuse, especially for controlled substances.
- **Acceptance criteria:** All transmission events are logged with a timestamp, message ID, and recipient system details, and the log cannot be altered after creation.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC4-06** (FR, Must)

- **Statement:** The system shall ensure that all transmitted prescriptions include a digital signature that is cryptographically valid and tied to the prescriber's credentials.
- **Actor:** Pharmacy system
- **Reasoning:** The requirement for two-factor signing (for controlled substances) and digital signatures ensures authenticity, integrity, and prescriber identity verification as mandated by regulatory frameworks.
- **Acceptance criteria:** Each transmitted prescription includes a cryptographically signed message that is verifiable and linked to the authenticated prescriber credentials.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

### UC5 Sign prescription

**REQ-UC5-01** (FR, Must)

- **Statement:** The system shall allow the prescriber to electronically sign a prescription after completing safety checks and before transmission.
- **Actor:** Prescriber
- **Reasoning:** The signing step is a core part of the prescribing workflow and must occur after safety checks to ensure medication safety. The evidence shows that signing is a required action in the transmit flow and is tied to prescription creation.
- **Acceptance criteria:** A prescriber can initiate, complete, and submit a signature on a prescription only after all safety checks have been passed and before transmission begins.
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC5-02** (REG, Must)

- **Statement:** The system shall verify the prescriber's identity prior to allowing electronic signing of any prescription for controlled substances.
- **Actor:** Prescriber
- **Reasoning:** The DEA mandates that prescriber identity must be proofed before signing prescriptions for controlled substances to prevent forgery and misuse. This is a direct regulatory requirement from EPCS regulations.
- **Acceptance criteria:** The system shall require successful identity verification (e.g., credential provider confirmation) before enabling the prescriber to sign any prescription involving controlled substances.
- **Source DEA-02:** Prescriber identity proofing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC5-03** (REG, Must)

- **Statement:** The system shall maintain a full audit trail of all events related to the creation, signing, and transmission of prescriptions for controlled substances.
- **Actor:** Prescriber
- **Reasoning:** The DEA requires a full audit trail to demonstrate compliance with EPCS regulations. This ensures accountability and enables verification of prescriber actions, which is essential for regulatory audits.
- **Acceptance criteria:** All events such as identity proofing, signing, and transmission must be logged in a tamper-evident, time-stamped audit log accessible for review by compliance officers.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC5-04** (FR, Must)

- **Statement:** The system shall enforce two-factor authentication when signing prescriptions containing controlled substances.
- **Actor:** Prescriber
- **Reasoning:** Two-factor signing is explicitly defined as an extension of the sign prescription use case for controlled drugs, ensuring higher security and reducing forgery risk. This aligns with regulatory intent to protect high-risk prescriptions.
- **Acceptance criteria:** For any prescription containing a controlled substance, the prescriber must complete two-factor authentication before the system allows electronic signing.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC5-05** (FR, Must)

- **Statement:** The system shall not allow a prescription to be signed without prior completion of safety checks for drug interactions and allergies.
- **Actor:** Prescriber
- **Reasoning:** Safety checks are a core functionality that must precede signing to prevent medication errors. The workflow shows that safety checks are included in the creation process and must be completed before signing.
- **Acceptance criteria:** The system shall block signature entry until all drug interaction, allergy, and dose warnings have been reviewed and resolved by the prescriber.
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC5-06** (NFR, Must)

- **Statement:** The system shall ensure that all signed prescriptions are time-stamped with a precise timestamp at the moment of signing.
- **Actor:** Prescriber
- **Reasoning:** Accurate timing is essential for audit trail integrity and compliance with EPCS, which requires precise event logging. A timestamp ensures chronological accuracy of prescription events.
- **Acceptance criteria:** The system shall record the exact time (to at least one-second precision) when a prescription is signed and store it in an immutable audit log.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a

### UC6 Two-factor signing

**REQ-UC6-01** (FR, Must)

- **Statement:** The system shall require two-factor authentication at the moment of signing for controlled substance prescriptions, with one factor originating from a separate device or token.
- **Actor:** Prescriber
- **Reasoning:** The DEA mandates two-factor authentication for controlled substances to prevent forgery and unauthorized access. One factor must come from a separate device or token, ensuring the prescriber's identity is verified beyond just password-based methods.
- **Acceptance criteria:** When a controlled substance prescription is signed, the system shall prompt the prescriber to provide a second authentication factor from a separate device or token, and only allow signing upon successful verification of both factors.
- **Source DEA-03:** Two-factor authentication at signing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC6-02** (FR, Must)

- **Statement:** The system shall enforce that two-factor authentication for signing is applied exclusively to controlled substance prescriptions and not to non-controlled substances.
- **Actor:** Prescriber
- **Reasoning:** The DEA's EPCS rules specifically apply two-factor authentication only to controlled substance prescriptions. Applying it broadly would violate regulatory scope and introduce unnecessary complexity or risk for non-controlled drugs.
- **Acceptance criteria:** The system shall not require two-factor authentication when signing a prescription that does not contain a controlled substance, regardless of user input or configuration.
- **Source DEA-03:** Two-factor authentication at signing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC6-03** (REG, Must)

- **Statement:** The system shall record the time, date, and identity of both authentication factors used during the two-factor signing process for each controlled substance prescription in an immutable audit trail.
- **Actor:** Prescriber
- **Reasoning:** The DEA requires a full audit trail for compliance with EPCS, including all events related to signing. Recording both authentication factors ensures traceability and supports verification of prescriber identity and actions in case of audits or investigations.
- **Acceptance criteria:** For every controlled substance prescription signed using two-factor authentication, the system shall store the timestamp, date, and details of each factor (e.g., token response, device ID) in an unalterable log that can be retrieved for audit purposes.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a

**REQ-UC6-04** (FR, Must)

- **Statement:** The system shall not allow a prescription to be signed with two-factor authentication if the prescriber's identity has not been verified through a separate credential provider prior to signing.
- **Actor:** Prescriber
- **Reasoning:** Two-factor authentication for controlled substances must be part of a broader identity verification process. The prescriber's identity must first be authenticated before any signing occurs, as per the EPCS requirements and use case relationships.
- **Acceptance criteria:** The system shall block the two-factor signing step until the prescriber has successfully completed identity verification via a credential provider, as defined in UC7 Verify prescriber ID.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a
- **Source DEA-03:** Two-factor authentication at signing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC6-05** (NFR, Must)

- **Statement:** The system shall ensure that all events related to two-factor authentication for controlled substance prescriptions are logged and retained for at least five years from the date of the prescription event.
- **Actor:** Compliance officer
- **Reasoning:** Regulatory compliance requires long-term retention of audit data. The DEA mandates that audit trails be maintained to demonstrate compliance, and five years is a common minimum for such records in healthcare systems.
- **Acceptance criteria:** The system shall store all events related to two-factor authentication during controlled substance prescription signing and ensure they are accessible and unaltered for at least 5 years post-event.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC6-06** (CON, Must)

- **Statement:** The system shall not allow a prescriber to sign a controlled substance prescription using the same device or token as their primary login credentials unless explicitly configured by an authorized credential provider with two-factor authentication enabled on a separate device.
- **Actor:** Prescriber
- **Reasoning:** The DEA requires one factor to come from a separate device or token, meaning the same device cannot be used for both authentication and signing. This constraint ensures physical separation of authentication factors.
- **Acceptance criteria:** If a prescriber attempts to use their primary login device as the second factor during two-factor signing, the system shall reject the request and prompt them to use a different device or token.
- **Source DEA-03:** Two-factor authentication at signing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

### UC7 Verify prescriber ID

**REQ-UC7-01** (FR, Must)

- **Statement:** The system shall verify the prescriber's identity using credentials provided by a credential provider before allowing the creation of an electronic prescription for a controlled substance.
- **Actor:** Credential provider
- **Reasoning:** The DEA requires proof of prescriber identity before signing prescriptions for controlled substances, ensuring only authorized individuals can issue such prescriptions and reducing the risk of forgery or misuse.
- **Acceptance criteria:** When a prescriber attempts to create a prescription for a controlled substance, the system must prompt for and validate credentials from a credential provider before allowing any action.
- **Source DEA-02:** Prescriber identity proofing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC7-02** (FR, Must)

- **Statement:** The system shall require two-factor authentication as part of the identity verification process when creating prescriptions for controlled substances.
- **Actor:** Credential provider
- **Reasoning:** The Two-Factor Signing use case is explicitly linked to Verify prescriber ID and applies only to controlled substances, aligning with DEA EPCS requirements that mandate stronger authentication for high-risk prescriptions.
- **Acceptance criteria:** For any prescription involving a controlled substance, the system must enforce two-factor authentication during identity verification before allowing the prescription to be signed or transmitted.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a
- **Source DEA-02:** Prescriber identity proofing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC7-03** (FR, Must)

- **Statement:** The system shall record the timestamp, method, and outcome of each prescriber identity verification attempt in an immutable audit trail.
- **Actor:** Credential provider
- **Reasoning:** An auditable record is essential for compliance with DEA EPCS and for demonstrating accountability in cases of misuse or errors, supporting traceability and regulatory scrutiny.
- **Acceptance criteria:** Each identity verification event must be logged with a timestamp, the authentication method used (e.g., SMS, token), and whether it succeeded or failed, and this data must persist in an unalterable format.
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC7-04** (REG, Must)

- **Statement:** The system shall not allow a prescriber to create or sign a prescription for a controlled substance unless the identity verification has been successfully completed by a credential provider.
- **Actor:** Prescriber
- **Reasoning:** The DEA mandates that prescribers must be properly identified before issuing controlled substance prescriptions, preventing unauthorized or fraudulent prescribing actions.
- **Acceptance criteria:** Any attempt to create or sign a prescription for a controlled substance without successful identity verification shall result in an immediate rejection and user notification.
- **Source DEA-02:** Prescriber identity proofing (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC7-05** (CON, Should)

- **Statement:** The system shall ensure that the credential provider's identity proofing method is interoperable with the e-prescribing platform using standardized protocols such as OAuth or SAML for secure authentication.
- **Actor:** Credential provider
- **Reasoning:** Standardized authentication protocols ensure interoperability across different prescriber systems and support integration with existing healthcare IT infrastructure, enabling broader adoption.
- **Acceptance criteria:** The system must accept identity proofing tokens or assertions from credential providers that use OAuth 2.0 or SAML 2.0 as defined in industry standards.
- **Source PROJ-02:** Actors (Project brief (own work, not an external standard)) n/a
- **Source SCRIPT-01:** Purpose (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

### UC8 Review audit trail

**REQ-UC8-01** (FR, Must)

- **Statement:** The system shall record and provide access to a full audit trail of all events related to the creation, signing, transmission, and security aspects of controlled-substance prescriptions.
- **Actor:** Compliance officer
- **Reasoning:** The audit trail is essential for demonstrating compliance with DEA regulations and enabling verification of prescriber actions, especially for controlled substances. Evidence from DEA-06 mandates a full audit trail for controlled substance prescriptions.
- **Acceptance criteria:** A compliance officer can retrieve and review the complete sequence of events (e.g., creation, signing, transmission) for any prescribed controlled substance in real time or upon request.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a

**REQ-UC8-02** (FR, Must)

- **Statement:** The system shall allow the compliance officer to filter and search audit trail entries by date, prescriber, drug type, prescription status, and event type.
- **Actor:** Compliance officer
- **Reasoning:** Efficient review of audit trails requires searchable and filterable data to identify specific events quickly, especially in large-scale or high-volume prescribing environments. This supports effective compliance monitoring.
- **Acceptance criteria:** The compliance officer can perform searches using at least four criteria: date range, prescriber ID, drug category (e.g., controlled substance), and event type (e.g., signed, transmitted).
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC8-03** (REG, Must)

- **Statement:** The system shall retain audit trail records for a minimum of 7 years from the date of the last prescription event involving a controlled substance.
- **Actor:** Compliance officer
- **Reasoning:** The DEA requires long-term retention of audit trails to support compliance demonstrations and investigations, particularly for controlled substances. This duration aligns with regulatory expectations under 21 CFR Part 1311.
- **Acceptance criteria:** Audit trail records are stored securely and remain accessible for at least seven years after the last event involving a controlled substance prescription.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC8-04** (FR, Must)

- **Statement:** The system shall generate a timestamped, immutable log entry for each audit trail event that includes the user ID, action type, timestamp, and associated prescription identifier.
- **Actor:** Compliance officer
- **Reasoning:** Immutable, time-stamped logs ensure the integrity of audit trail data and prevent tampering or alteration. This supports accurate verification of prescriber actions and compliance with DEA EPCS rules.
- **Acceptance criteria:** Each event in the audit trail includes a timestamp, user ID, action type (e.g., 'prescription created'), and prescription ID, and these entries cannot be altered after creation.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-03:** Core functionalities (Project brief (own work, not an external standard)) n/a

**REQ-UC8-05** (REG, Must)

- **Statement:** The system shall support third-party auditing of its audit trail functionality at least every two years or whenever a significant change to the software occurs.
- **Actor:** Compliance officer
- **Reasoning:** The DEA mandates third-party audits of e-prescribing software to ensure ongoing compliance and reliability. This requirement ensures that audit trail integrity is independently verified over time.
- **Acceptance criteria:** An external auditor completes a full review of the system's audit trail functionality, including data accuracy, completeness, and security, at least every two years or after any major functional change.
- **Source DEA-04:** Third-party audit of the software (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC8-06** (NFR, Must)

- **Statement:** The system shall ensure that all audit trail records are stored in an encrypted format and accessible only to authorized personnel with appropriate roles and permissions.
- **Actor:** Compliance officer
- **Reasoning:** Protecting audit trail data from unauthorized access is critical to maintain the integrity and confidentiality of prescribing activities, especially for controlled substances. This aligns with security expectations in healthcare systems.
- **Acceptance criteria:** Audit trail records are encrypted at rest and accessed only by users with explicit authorization (e.g., compliance officer role), as verified through audit logs and access controls.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a

### UC9 Lock on audit failure

**REQ-UC9-01** (FR, Must)

- **Statement:** The system shall lock controlled-substance prescribing functionality when an audit failure is detected.
- **Actor:** Compliance officer
- **Reasoning:** To prevent unauthorized or non-compliant prescriptions from being issued when the system fails to meet DEA audit requirements, ensuring safety and regulatory compliance. The evidence shows that audit failures must be addressed promptly via notification and action.
- **Acceptance criteria:** When an audit failure is detected, controlled-substance prescribing functions must become inaccessible to all prescribers until the issue is resolved.
- **Source DEA-05:** Notification when an audit fails (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC9-02** (REG, Must)

- **Statement:** The system shall notify the DEA within 1 business day of any audit failure involving a controlled substance prescription.
- **Actor:** Compliance officer
- **Reasoning:** This requirement directly stems from DEA regulations that mandate timely notification of audit failures to ensure regulatory compliance and accountability. The evidence explicitly states a 1-business-day deadline for such notifications.
- **Acceptance criteria:** Upon detection of an audit failure, the system must automatically trigger a notification to the DEA within one business day, with a record of transmission in the audit trail.
- **Source DEA-05:** Notification when an audit fails (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-UC9-03** (REG, Must)

- **Statement:** The system shall maintain a full audit trail of all events related to controlled-substance prescriptions during periods when prescribing is locked due to an audit failure.
- **Actor:** Compliance officer
- **Reasoning:** The DEA requires a complete audit trail for compliance demonstration, even during periods of system failure or lockdown. This ensures transparency and traceability for regulatory review and accountability.
- **Acceptance criteria:** All actions related to controlled-substance prescriptions—including attempts to prescribe while locked—must be logged in the audit trail with timestamps and user identifiers.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC9-04** (FR, Must)

- **Statement:** The system shall only allow the compliance officer to unlock controlled-substance prescribing after an audit failure has been resolved and verified by a third-party auditor.
- **Actor:** Compliance officer
- **Reasoning:** To ensure that the system is compliant before resuming prescribing, the unlock process must be tied to formal audit validation. The requirement for third-party audits establishes a baseline of trust and compliance verification.
- **Acceptance criteria:** Prescribing can only be re-enabled after the compliance officer confirms resolution of the failure and receives evidence from a third-party audit confirming system compliance.
- **Source DEA-04:** Third-party audit of the software (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC9-05** (NFR, Must)

- **Statement:** The system shall record the reason for each audit failure in the audit trail when controlled-substance prescribing is locked.
- **Actor:** Compliance officer
- **Reasoning:** Providing clear, traceable failure reasons enables the compliance officer to investigate root causes and take corrective actions efficiently. This supports audit readiness and regulatory transparency.
- **Acceptance criteria:** Each audit failure must be accompanied by a recorded description of the failure type (e.g., missing signature, invalid timestamp) in the system's audit trail.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-UC9-06** (FR, Must)

- **Statement:** The system shall not allow any changes to controlled-substance prescriptions while prescribing is locked due to an audit failure.
- **Actor:** Prescriber
- **Reasoning:** To prevent unsafe or non-compliant prescription modifications during system failures, the system must enforce a complete lock on all prescribing actions. This aligns with safety and compliance goals outlined in the problem statement.
- **Acceptance criteria:** Any attempt by a prescriber to create, modify, or cancel a controlled-substance prescription while the system is locked shall be rejected with an error message indicating the audit failure status.
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

### XC Cross-cutting qualities

**REQ-XC-01** (REG, Must)

- **Statement:** The system shall support the transmission of prescriptions using current and mandated versions of the NCPDP SCRIPT standard.
- **Actor:** Prescriber
- **Reasoning:** CMS mandates specific versions of the NCPDP SCRIPT standard, which evolve over time. The system must remain compliant by supporting upgrades to new mandated versions.
- **Acceptance criteria:** The system successfully transmits prescriptions in accordance with the current mandated version of NCPDP SCRIPT when configured and validated against the latest standard.
- **Source SCRIPT-03:** Mandated versions change over time (NCPDP SCRIPT Standard) https://standards.ncpdp.org/

**REQ-XC-02** (FR, Must)

- **Statement:** The system shall perform real-time safety checks for drug interactions, allergies, and correct dosing during prescription creation.
- **Actor:** Prescriber
- **Reasoning:** Paper-based prescribing leads to medication errors due to illegible handwriting or missed interactions. Safety checks using a drug knowledge base reduce these risks and improve patient safety.
- **Acceptance criteria:** When a prescription is created, the system must detect and alert the prescriber to any known drug interactions, allergies, or incorrect dosing based on current drug knowledge data.
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a

**REQ-XC-03** (REG, Must)

- **Statement:** The system shall maintain a full audit trail of all events related to controlled-substance prescriptions, including creation, signing, transmission, and cancellation.
- **Actor:** Compliance officer
- **Reasoning:** The DEA's EPCS regulations require a full audit trail to demonstrate compliance with controlled substance prescription rules. This enables verification of prescriber identity and actions over time.
- **Acceptance criteria:** All events involving controlled-substance prescriptions—such as creation, signing, transmission, and cancellation—are recorded in an immutable, timestamped log accessible for review.
- **Source DEA-06:** Audit trail (DEA Electronic Prescriptions for Controlled Substances (EPCS), 21 CFR Part 1311) https://www.ecfr.gov/current/title-21/chapter-II/part-1311

**REQ-XC-04** (FR, Must)

- **Statement:** The system shall verify prescriber identity using two-factor authentication before allowing the creation or signing of a prescription for controlled substances.
- **Actor:** Prescriber
- **Reasoning:** Two-factor signing is required for controlled drugs under EPCS to prevent forgery and ensure only authorized prescribers can issue prescriptions.
- **Acceptance criteria:** Before a prescription for a controlled substance is signed, the system must confirm the prescriber's identity through two-factor authentication (e.g., password and token).
- **Source PROJ-04:** Use cases and relationships (Project brief (own work, not an external standard)) n/a

**REQ-XC-05** (NFR, Must)

- **Statement:** The system shall ensure that all prescription transmissions are securely encrypted in transit using TLS 1.2 or higher.
- **Actor:** Pharmacy system
- **Reasoning:** Secure transmission is essential to prevent unauthorized access and tampering of prescription data, especially for controlled substances that are vulnerable to misuse.
- **Acceptance criteria:** All messages sent from the prescriber system to the pharmacy must be encrypted using TLS 1.2 or higher during transmission.
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a

**REQ-XC-06** (FR, Must)

- **Statement:** The system shall automatically detect and notify the prescriber when a prescribed drug is flagged for interaction or allergy in real time, based on an external drug knowledge base.
- **Actor:** Prescriber
- **Reasoning:** Manual processes fail to catch interactions and allergies. Real-time checks using a reliable drug knowledge base reduce medication errors and improve patient safety.
- **Acceptance criteria:** The system must detect and alert the prescriber within seconds of entering a new prescription if any known interaction or allergy exists with existing medications.
- **Source PROJ-01:** Problem statement (Project brief (own work, not an external standard)) n/a
