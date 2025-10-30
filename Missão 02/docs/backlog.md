# Backlog — Missão 2

## Épicos
- Vigilância epidemiológica
- Importação e limpeza de dados
- Alertas populacionais
- Dashboard geográfico

## Features e tarefas

### F1 — ETL hemogramas
- [ ] Definir schema
- [ ] Script ingestão CSV FHIR-like
- [ ] Validação ranges
- [ ] Logs erros
- [ ] Inserção no PostgreSQL

### F2 — API
- [ ] /upload
- [ ] /metrics
- [ ] /alerts
- [ ] Autenticação simples (MVP)

### F3 — Dashboard
- [ ] Heatmap municipal
- [ ] Tabela indicadores
- [ ] Filtro faixa etária
- [ ] Filtro município

### F4 — Alert Engine
- [ ] Detectar plaquetas <100k
- [ ] Queda >=15% em 72h
- [ ] Flags por município
- [ ] Salvar e expor via API
