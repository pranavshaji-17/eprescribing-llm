SOURCE: HL7 FHIR MedicationRequest resource
URL: https://hl7.org/fhir/medicationrequest.html

> Study notes condensed from the source. For stronger grounding, paste real excerpts
> from the official page under new `## [FHIR-0X]` headings. Chunk IDs are cited by the LLM.

## [FHIR-01] Purpose: an order, not an administration
MedicationRequest represents the intent to supply a medication and give instructions for its use: a medication order or request. It represents intent only. It does not record that the medication was actually administered to the patient.

## [FHIR-02] One resource instance is one medication order
One MedicationRequest instance represents one medication order. A prescription containing several drugs therefore needs multiple MedicationRequest instances, which are linked to each other.

## [FHIR-03] Scope of use
The resource covers inpatient and outpatient settings and applies to prescribed medications, over-the-counter (OTC) medications and medical devices.

## [FHIR-04] Relationships to other resources
A MedicationRequest is tied to a Patient (who the order is for), a Practitioner (who requested it) and an Encounter (the care context in which it was made).

## [FHIR-05] Lifecycle: status and intent
The resource carries status and intent elements that express whether a request is active, cancelled or completed and whether it is a proposal, plan or order. This is relevant to cancelling or changing an order after it has been issued.
