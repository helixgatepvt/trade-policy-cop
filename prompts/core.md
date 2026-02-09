# Core Logic

## Purpose
Provide a single entry point to decide which trade policy logic applies.

## Inputs
- Country of export
- Country of import
- Product description
- Declared value

## Decision Flow
- If US and India → apply US–India MFA logic
- If India and EU → apply India–EU FTA logic
- Always evaluate Revenue Integrity checks

## Output
- Applicable policy
- Required checks
- Flags for risk or review
