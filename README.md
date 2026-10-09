 Insurance Claims AI Assistant

An agentic AI application built with Python, CrewAI, and Anthropic Claude to retrieve insurance claim information, validate claim data, and generate preliminary assessments for human review.

## Project Overview

This project demonstrates an AI-assisted insurance claims workflow. A CrewAI agent uses a custom Python tool to retrieve mock claim records, review key information, identify missing or inconsistent data, and generate a preliminary claim assessment.

The application supports claims review. It does not make final insurance coverage or payment decisions.

## Features

- **Claim Retrieval:** Search mock insurance claim records using a claim ID.
- **Data Validation:** Check required fields, claim type, claim amount, claim ID consistency, and date validity.
- **AI-Powered Assessment:** Use CrewAI and Anthropic Claude to summarize claim information.
- **Structured Output:** Define a consistent assessment format using Pydantic.
- **Human Review:** Flag information requiring further verification without making final claim decisions.

## Technology Stack

- Python
- CrewAI
- Anthropic Claude API
- Pydantic
- Git and GitHub

## Project Structure

```text
insurance_claims_ai/
├── agents/
│   └── insurance_claims_analyst.jsonc
├── tools/
│   ├── search_claim.py
│   └── claim_assessment.py
├── crew.jsonc
├── pyproject.toml
├── .env.example
└── README.md


