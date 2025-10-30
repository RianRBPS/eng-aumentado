# Arquitetura Conceitual

```mermaid
flowchart LR
    Labs -->|FHIR/CSV| Ingestor
    Ingestor --> ETL
    ETL --> DB[(PostgreSQL)]
    DB --> API
    API --> Dashboard
    Dashboard --> MapModule
    AlertsEngine --> Dashboard
```
