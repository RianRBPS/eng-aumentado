# Requisitos Funcionais – Painel Epidemiológico de Hemogramas

**Projeto:** Painel Epidemiológico de Hemogramas  
**Local:** Estado de Goiás  
**Data:** Outubro de 2025  

---

## Lista de Requisitos Funcionais

| Código | Requisito Funcional | Descrição |
|--------|------------------|-----------|
| RF01   | Registro de hemogramas | O sistema deve permitir receber e armazenar hemogramas completos de laboratórios públicos e privados. |
| RF02   | Dashboard interativo | Exibir dashboards com indicadores de anemia, leucopenias e trombocitopenias. |
| RF03   | Alertas automáticos | Enviar notificações quando houver aumento súbito ou picos de indicadores hematológicos críticos. |
| RF04   | Análise temporal | Permitir visualização de indicadores ao longo do tempo (diário, semanal, mensal, anual). |
| RF05   | Análise regional | Permitir visualização por município, microrregião e região. |
| RF06   | Filtros demográficos | Permitir filtragem de dados por faixa etária, sexo e grupo populacional. |
| RF07   | Exportação de relatórios | Gerar relatórios exportáveis em PDF e Excel com indicadores e gráficos. |
| RF08   | Integração com SUS | Importar dados de hemogramas e exportar resultados consolidados seguindo padrões HL7 FHIR. |
| RF09   | Histórico de dados | Armazenar histórico completo para análises comparativas e longitudinal. |
| RF10   | Configuração de alertas | Permitir configurar thresholds para alertas automáticos por indicador e região. |
| RF11   | Login e autenticação | Sistema deve permitir login seguro de usuários com papéis definidos (gestor estadual, municipal, pesquisador). |
| RF12   | Controle de permissões | Diferenciar acessos por perfil de usuário (visualização, exportação, configuração de alertas). |
| RF13   | Indicadores derivados | Calcular índices derivados como NLR, PLR e RDW a partir dos hemogramas. |
| RF14   | Validação de dados | Verificar consistência dos dados importados e gerar logs de erro para registros inválidos. |
| RF15   | Notificação de inconsistências | Alertar administradores sobre dados inconsistentes ou faltantes. |
| RF16   | Dashboard comparativo | Permitir comparação entre municípios, microrregiões e faixas etárias. |
| RF17   | Atualização diária | Garantir atualização diária dos dados com processamento automático. |
| RF18   | Suporte a múltiplos laboratórios | Importar dados simultaneamente de múltiplos laboratórios parceiros. |
| RF19   | Interface amigável | Dashboard e relatórios devem ser intuitivos e de fácil navegação para usuários não técnicos. |
| RF20   | Suporte a auditoria | Registrar logs de acesso, alterações e exportações para auditoria futura. |
| RF21   | Exportação automática de alertas | Enviar alertas automáticos por e-mail ou SMS para gestores quando thresholds críticos forem atingidos. |
| RF22   | Dashboard geoespacial | Exibir mapas interativos com indicadores por região, microrregião e município. |
| RF23   | Comparação temporal | Permitir comparar indicadores atuais com históricos de anos anteriores. |
| RF24   | Integração com pesquisas acadêmicas | Disponibilizar dados anonimizados para pesquisadores autorizados. |
| RF25   | Notificações personalizadas | Usuários podem configurar alertas específicos para indicadores ou regiões de interesse. |
| RF26   | Dashboard mobile-friendly | Interface adaptável para tablets e smartphones. |
| RF27   | Exportação de dados brutos | Possibilitar download de dados brutos em CSV para análises externas. |
| RF28   | Filtro por tipo de hemograma | Permitir filtrar por exames completos, parciais ou específicos (ex: plaquetas, leucócitos). |
| RF29   | Relatórios customizáveis | Usuários podem selecionar indicadores e períodos para gerar relatórios personalizados. |
| RF30   | Agendamento de relatórios | Permitir agendar geração automática de relatórios periódicos. |
| RF31   | Integração com sistemas municipais | Importar dados de laboratórios municipais e consolidar no painel estadual. |
| RF32   | Histórico de alertas | Armazenar histórico de alertas gerados para auditoria e análise de tendências. |
| RF33   | Exportação de dashboards | Permitir exportar dashboards como imagens ou PDF. |
| RF34   | Módulo de treinamento | Incluir guia interativo ou tutorial para novos usuários do sistema. |
| RF35   | Suporte multilíngue | Sistema deve suportar pelo menos português e inglês em interfaces e relatórios. |
| RF36   | Indicadores epidemiológicos avançados | Gerar métricas como taxa de incidência, prevalência ajustada e risco relativo. |
| RF37   | Comparativo com médias nacionais | Permitir comparar indicadores estaduais com dados nacionais disponíveis. |
| RF38   | Histórico de auditoria de acesso | Registrar log de login, logout e ações do usuário. |
| RF39   | Integração com dashboards acadêmicos | Permitir conexão com plataformas de visualização de dados acadêmicos e epidemiológicos. |
| RF40   | Suporte a múltiplos tipos de alerta | Notificações podem ser visuais, sonoras ou via e-mail/SMS dependendo do nível de criticidade. |

---

**Observação:** Estes requisitos funcionais estão alinhados com o objetivo de monitoramento epidemiológico, integração com sistemas existentes e suporte à decisão em saúde pública.  

