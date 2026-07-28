**To:** Code
**From:** CTO
**Re:** FHIR block count — 6 vs. 7

`hl7-knowledge-blocks.json` as pushed to `main` (commit `d423102`) has 15
blocks: 9 v2, 6 FHIR. The version built on this end has 7 FHIR blocks:

1. `fhir.restful-interactions-overview`
2. `fhir.read-patient-instance`
3. `fhir.terminology-binding-model`
4. `fhir.patient-resource`
5. `fhir.encounter-resource`
6. `fhir.observation-resource`
7. `fhir.servicerequest-resource`

One of these isn't in the file that landed on `main`. Three questions:

1. Which of the 7 IDs above is missing from your copy of the file?
2. Was it dropped on purpose (e.g. consolidated into another block during
   authoring), or did it just not make it into the final file?
3. Can you grep the file for any `prerequisites` or `relatedBlocks` entry
   that still points at the missing ID? If the ID was removed but another
   block still references it, that's a dangling reference sitting live on
   `main` right now and needs a fix either way — either restore the block
   or strip the reference.

No action needed beyond answering these — not asking for a re-push yet,
just need to know what actually happened before deciding what to do about
it.
