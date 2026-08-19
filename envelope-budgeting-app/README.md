# Envelope Budgeting App

A personal envelope budgeting web app - income is divided into named virtual
"envelopes" (Groceries, Rent, Savings, etc.), with spending logged manually
against each. UI is modeled on the feel of a payment app (GPay-style), but
this is purely a manual ledger - no real money movement or UPI integration.

## Tech Stack
- Frontend: React
- Backend: Custom API runner
- Database: PostgreSQL (run locally via Docker during development)

## Project Structure
envelope-budgeting-app/
  frontend/   - React app (UI only, talks to backend via HTTP)
  backend/    - API server (business logic, talks to Postgres)

## Status
Structure/schema design phase. No application logic implemented yet -
this repo is being built as a learning project, one concept at a time.
