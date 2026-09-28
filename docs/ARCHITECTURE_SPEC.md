# DIGITAL EXPERIENCE JURY AUDITOR
## Especificação oficial da skill — Awards + Benchmark + SEO + UX + Engineering

**Status:** arquitetura conceitual congelada para implementação  
**Versão da especificação:** 1.0  
**Data de referência:** 2026-09-28  
**Idioma-base da documentação:** Português (saídas podem ser localizadas)  
**Nome técnico sugerido:** `digital-experience-jury-auditor`  
**Tipo:** skill de auditoria autônoma, comparativa, explicável e versionada  

---

# 0. OBJETIVO

Esta skill não existe apenas para dizer se um site é “bom” ou “ruim”. Ela deve demonstrar, com evidências reproduzíveis:

1. **onde o site está hoje**;
2. **por que recebeu cada nota**;
3. **onde perdeu pontos e em qual critério**;
4. **o que está faltando para atingir o próximo patamar**;
5. **quais problemas têm maior impacto real**;
6. **quais elementos não devem ser alterados**;
7. **como o site se compara a trabalhos premiados relevantes**;
8. **como se comporta em SEO, acessibilidade, performance, engenharia, conteúdo, conversão, resiliência e cross-device**;
9. **qual é o grau de confiança de cada conclusão**;
10. **se alterações posteriores melhoraram ou pioraram o produto**.

A skill deve atuar simultaneamente como:

- jurado simulado do **Awwwards**;
- jurado simulado do **The Webby Awards**;
- jurado heurístico do **FWA — Favourite Website Awards**;
- jurado simulado do **CSS Design Awards**;
- auditor de SEO;
- auditor de experiência e usabilidade;
- auditor de acessibilidade;
- auditor de performance;
- auditor de engenharia web;
- auditor de conteúdo;
- auditor de conversão/objetivo;
- auditor de resiliência;
- auditor de higiene de segurança e privacidade;
- motor de benchmark de projetos premiados;
- motor de mineração de padrões;
- motor de análise de originalidade/distintividade;
- motor de decisão e priorização;
- motor de regressão entre versões.

---

# 1. PRINCÍPIOS INEGOCIÁVEIS

## 1.1 No evidence = no score

> **NO EVIDENCE = NO SCORE**

A skill nunca deve presumir que um requisito passou ou falhou sem evidência suficiente.

Quando algo não puder ser medido:

```text
STATUS: NOT VERIFIED
Reason: campo/RUM indisponível, browser não disponível, acesso negado etc.
Score handling: critério excluído ou marcado como não verificável.
Confidence impact: reduzir confidence score.
```

Nunca transformar ausência de dados em nota positiva.

---

## 1.2 Nenhuma penalização sem explicação

Toda perda de pontos deve possuir:

- observação;
- evidência;
- critério afetado;
- motivo da penalização;
- magnitude da penalização;
- impacto esperado;
- benchmark aplicável;
- correção recomendada;
- condição de validação pós-correção.

Proibido:

```text
UX: 7.2 — navegação pode melhorar.
```

Obrigatório:

```text
UX > Navigation clarity
Score: 7.2 / 10
Lost: -2.8
Evidence: menu mobile possui 11 itens de primeiro nível; foco visível se perde no overlay;
current-page state não é comunicado.
Why penalized: maior carga de decisão + perda de orientação + falha de teclado.
Benchmark: P75 do cohort direto apresenta <= 7 escolhas primárias e estado atual explícito.
Next level: reduzir profundidade, corrigir foco e comunicar localização.
```

---

## 1.3 Nenhuma recomendação sem impacto

Toda recomendação deve responder:

- **o que muda**;
- **por que muda**;
- **qual problema resolve**;
- **quais notas podem subir**;
- **quais riscos introduz**;
- **quanto custa implementar**;
- **como validar**.

---

## 1.4 Nenhum benchmark sem contexto

A skill não pode comparar indiscriminadamente:

- e-commerce com portfólio experimental;
- SaaS com editorial;
- site de campanha com aplicação transacional;
- experiência artística com site informacional;
- desktop showcase com produto mobile-first.

Cada benchmark deve declarar a coorte utilizada e a razão de compatibilidade.

---

## 1.5 Correlação não é requisito

O fato de um padrão aparecer em sites premiados **não torna esse padrão obrigatório**.

A skill deve distinguir:

- requisito;
- padrão esperado;
- vantagem;
- opção;
- tendência;
- experimento;
- anti-pattern;
- padrão sem correlação relevante.

Exemplo:

```text
Custom cursor
Observed: 29% da coorte
Classification: OPTIONAL
Conclusion: ausência não é deficiência.
```

---

## 1.6 Tecnologia não recebe pontos por existir

Não conceder bônus automático por:

- WebGL;
- Three.js;
- GSAP;
- shaders;
- smooth scrolling;
- custom cursor;
- 3D;
- IA;
- vídeo hero;
- microinterações;
- framework moderno.

Avaliar sempre:

```text
purpose
integration
originality
execution
usability cost
accessibility cost
performance cost
maintenance cost
narrative value
```

Uma tecnologia pode gerar efeito líquido negativo.

---

## 1.7 Separar padrão oficial de modelo interno

A skill **nunca** deve chamar sua nota simulada de “nota oficial” da premiação.

Usar:

```text
AWWWARDS READINESS SCORE
WEBBY READINESS SCORE
FWA SIMULATED JUDGMENT
CSSDA JURY SIMULATION
```

Nunca:

```text
OFFICIAL WEBBY SCORE
OFFICIAL FWA SCORE
```

---

# 2. FONTES NORMATIVAS E STATUS DOS CRITÉRIOS

A implementação deve versionar as fontes e registrar a data da última validação.

## 2.1 Awwwards

Fonte pública de avaliação:

- https://www.awwwards.com/about-evaluation/
- https://www.awwwards.com/websites/
- https://www.awwwards.com/websites/sites_of_the_day/

Pesos públicos usados pelo modelo Awwwards:

| Dimensão | Peso |
|---|---:|
| Design | 40% |
| Usability | 30% |
| Creativity | 20% |
| Content | 10% |

Esses pesos podem ser tratados como oficiais enquanto a fonte vigente os mantiver.

As subdimensões definidas nesta skill são **internas**, usadas para explicar a nota.

---

## 2.2 The Webby Awards

Fontes:

- https://www.webbyawards.com/judging-criteria/
- https://www.webbyawards.com/judging-process/
- https://winners.webbyawards.com/winners/websites-and-mobile-sites

Na página 2026/2027 de critérios, Websites & Mobile Sites inclui:

- Content;
- Structure and Navigation;
- Visual Design;
- Functionality;
- Interactivity;
- Innovation;
- Overall Experience.

O Webby não publica, nessa fonte, pesos oficiais equivalentes aos 40/30/20/10 do Awwwards.

Portanto:

- a skill **não deve inventar pesos oficiais**;
- o score geral do Webby será um **model score**;
- por padrão, dimensões são normalizadas de forma equilibrada;
- categorias específicas podem alterar o **target esperado**, não fingir um peso oficial inexistente.

---

## 2.3 CSS Design Awards

Fontes:

- https://www.cssdesignawards.com/about
- páginas públicas de nominees/winners.

Dimensões públicas:

- UI;
- UX;
- Innovation.

A página institucional informa atualmente:

- WOTD depende do painel de jurados e, para consideração, a média deve ficar acima de aproximadamente **8.00**, com variação conforme a qualidade dos trabalhos submetidos;
- Special Kudos é associado a média de jurados acima de **6**;
- prêmios públicos de UI/UX/Innovation dependem também de votos públicos e média dos jurados.

A skill pode simular **jury readiness**, mas não pode prever votos públicos como se fossem determinísticos.

---

## 2.4 FWA

Fontes:

- https://thefwa.com/
- https://thefwa.com/cases/

O FWA possui histórico público de trabalhos reconhecidos e níveis como FWA of the Day, porém a documentação pública atual não fornece um sistema de pesos tão explícito quanto Awwwards.

Regra:

> O FWA será avaliado por uma rubrica heurística calibrada empiricamente contra trabalhos reconhecidos pelo próprio FWA.

A skill deve rotular a saída:

```text
FWA SIMULATED JUDGMENT
```

Nunca representar a rubrica heurística como fórmula oficial do FWA.

---

## 2.5 SEO — Google Search

Fontes-base:

- https://developers.google.com/search/docs/essentials
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide

Google Search Essentials distingue:

- technical requirements;
- spam policies;
- key best practices.

A documentação deixa explícito que cumprir requisitos e boas práticas **não garante** crawl, indexação ou posição específica.

A skill deve separar:

- **SEO Quality Score** — qualidade técnica/estrutural observável;
- **Organic Visibility** — desempenho real quando houver Search Console/dados externos confiáveis.

---

## 2.6 Core Web Vitals

Fonte:

- https://web.dev/articles/vitals

Thresholds vigentes usados como referência:

- LCP <= 2.5 s;
- INP <= 200 ms;
- CLS <= 0.1;
- avaliação de campo preferencialmente no percentil 75, segmentado por mobile e desktop.

Dados de laboratório não devem ser apresentados como substitutos de dados de campo.

---

## 2.7 Acessibilidade

Fonte normativa:

- https://www.w3.org/TR/WCAG22/

Usar **WCAG 2.2** como baseline principal enquanto continuar vigente.

A pontuação interna de acessibilidade serve para priorização; ela **não substitui declaração formal de conformidade WCAG**.

---

# 3. MODOS DE AUDITORIA

## 3.1 QUICK

Uso:

- triagem rápida;
- primeiro diagnóstico;
- pré-check de release.

Cobertura mínima:

- home;
- 2–4 páginas representativas;
- desktop + mobile;
- SEO técnico essencial;
- CWV/lab quando disponível;
- acessibilidade automatizável + checks manuais principais;
- cohort reduzido, preferencialmente 12–20 benchmarks.

Saída:

- Executive Audit;
- top findings;
- notas com confidence limitado.

---

## 3.2 FULL

Uso padrão.

Cobertura:

- descoberta de arquitetura;
- 5–15 templates/páginas representativas;
- desktop/mobile/tablet quando relevante;
- fluxos principais;
- SEO completo;
- acessibilidade;
- performance;
- benchmark 20–50 sites relevantes;
- awards simulation completa;
- pattern mining;
- distinctiveness;
- decision roadmap.

---

## 3.3 FORENSIC

Auditoria máxima.

Pode incluir:

- crawl extensivo;
- source/repository access;
- Search Console;
- Analytics/RUM;
- logs quando autorizados;
- headers e rede;
- análise de bundle;
- dependências;
- cache;
- screenshots e filmstrips;
- múltiplos browsers;
- múltiplos device profiles;
- benchmark 40–100+ referências;
- histórico e versões anteriores;
- relatório técnico completo.

---

## 3.4 REGRESSION

Compara duas ou mais auditorias.

Obrigatório produzir:

```text
IMPROVED
UNCHANGED
REGRESSED
NEW ISSUE
RESOLVED
NOT COMPARABLE
```

Nunca considerar melhora global se uma melhoria estética introduziu regressão crítica em UX, SEO, acessibilidade ou performance sem explicitá-la.

---

## 3.5 AWARD SUBMISSION MODE

Foco em uma premiação/categoria específica.

Exemplo:

```text
Target: Webby > Best User Experience
```

O modo deve:

- preservar a auditoria integral;
- aprofundar os critérios relevantes;
- montar benchmark da categoria;
- declarar gap para referências recentes;
- identificar blockers de submissão competitiva.

---

## 3.6 SEO FORENSIC MODE

Foco em:

- crawlability;
- indexability;
- canonicalização;
- renderização;
- Search Console;
- queries;
- páginas;
- CTR;
- sitemap;
- arquitetura;
- entidades;
- structured data;
- conteúdo;
- CWV;
- canibalização;
- problemas de indexação;
- visibilidade real.

---

# 4. INPUTS

## 4.1 Obrigatório

```yaml
url: https://example.com
```

## 4.2 Opcionais

```yaml
locale: pt-BR
business_goal: lead_generation
site_type: portfolio
award_targets:
  - awwwards
  - webby
  - fwa
  - cssda
award_categories: []
competitors: []
known_benchmarks: []
source_repository: null
search_console: null
analytics: null
previous_audit: null
constraints:
  performance_budget: null
  must_keep: []
  cannot_change: []
```

Se site_type e business_goal não forem fornecidos, a skill deve inferir e registrar:

```text
INFERRED — confidence 84%
```

Não esconder inferências.

---

# 5. PIPELINE PRINCIPAL

```text
01  Scope resolution
02  Source/rubric freshness check
03  Site fingerprint
04  Crawl & architecture discovery
05  Representative page sampling
06  Render matrix
07  Technical measurements
08  SEO audit
09  Accessibility audit
10  UX/usability audit
11  Visual/design audit
12  Motion/interaction audit
13  Content audit
14  Engineering audit
15  Conversion/goal audit
16  Resilience/security hygiene
17  Benchmark cohort construction
18  Award-version integrity check
19  Benchmark extraction
20  Pattern mining
21  Distinctiveness analysis
22  Award scoring
23  Independent quality scoring
24  Confidence calculation
25  Decision prioritization
26  Do-not-change extraction
27  Regression analysis, if applicable
28  Executive report
29  Forensic report
30  Machine-readable findings
```

---

# 6. COBERTURA DE PÁGINAS

A home não pode representar sozinha o site.

A skill deve identificar templates e jornadas, por exemplo:

- home;
- about;
- service;
- category;
- portfolio/case;
- product;
- article;
- search;
- contact;
- form;
- cart/checkout quando aplicável;
- login/account quando autorizado;
- 404;
- empty/error states;
- páginas mobile relevantes.

Relatório:

```text
PAGE COVERAGE
Homepage             100%
Services             100%
Portfolio templates   80%
Articles               60%
Contact               100%
404                   100%

Overall coverage: 87%
Confidence: HIGH
```

A skill deve usar **templates representativos**, não necessariamente todas as URLs, salvo FORENSIC.

---

# 7. MATRIZ DE RENDERIZAÇÃO

Baseline recomendado, adaptável:

## Viewports

- 360×800;
- 390×844;
- 768×1024;
- 1024×768;
- 1440×900;
- 1920×1080.

Adicionar landscape mobile se interação/motion justificar.

## Browsers

Quando disponíveis:

- Chromium/Chrome;
- Firefox;
- WebKit/Safari-equivalent.

Se Safari real não for testado:

```text
Safari: NOT VERIFIED
```

Nunca assumir compatibilidade.

## Condições de rede/CPU

Quando a infraestrutura permitir:

- unthrottled baseline;
- Fast 4G;
- Slow 4G;
- CPU throttling representativo;
- cold load;
- repeat load.

---

# 8. AWARD ENGINE — AWWWARDS

## 8.1 Fórmula oficial de alto nível

```text
AWW =
Design      * 0.40 +
Usability   * 0.30 +
Creativity  * 0.20 +
Content     * 0.10
```

Cada dimensão: 0–10.

## 8.2 Design — 40%

Subrubrica interna:

| Subdimensão | Peso interno |
|---|---:|
| Art direction | 20% |
| Typography | 15% |
| Layout/grid/composition | 15% |
| Visual hierarchy | 15% |
| System consistency | 10% |
| Responsive visual execution | 10% |
| Imagery/media treatment | 10% |
| Detail/polish | 5% |

### Verificar

- identidade própria;
- coerência visual;
- qualidade de grid;
- proporção;
- escala tipográfica;
- ritmo;
- contraste;
- tratamento de mídia;
- consistência entre páginas;
- qualidade responsiva;
- estados visuais;
- refinamento.

---

## 8.3 Usability — 30%

| Subdimensão | Peso interno |
|---|---:|
| IA/navigation | 20% |
| Interaction feedback | 15% |
| Task clarity | 15% |
| Mobile/touch usability | 15% |
| Accessibility-related usability | 15% |
| Readability | 10% |
| Error/state handling | 5% |
| Perceived speed | 5% |

Não confundir “navegação diferente” com “navegação ruim”. Medir discoverability, orientação e sucesso da tarefa.

---

## 8.4 Creativity — 20%

| Subdimensão | Peso interno |
|---|---:|
| Concept originality | 25% |
| Concept/interface integration | 20% |
| Interaction originality | 15% |
| Motion/storytelling | 15% |
| Distinctiveness | 15% |
| Risk discipline | 10% |

“Risk discipline” mede se experimentação foi controlada sem degradar produto.

---

## 8.5 Content — 10%

| Subdimensão | Peso interno |
|---|---:|
| Relevance & voice | 25% |
| Information structure | 20% |
| Media quality | 20% |
| Clarity | 15% |
| Design-content cohesion | 10% |
| Completeness | 10% |

---

# 9. AWARD ENGINE — WEBBY

## 9.1 Dimensões vigentes para Websites & Mobile Sites

- Content;
- Structure and Navigation;
- Visual Design;
- Functionality;
- Interactivity;
- Innovation;
- Overall Experience.

## 9.2 Regra de score

Como pesos oficiais não são publicados na fonte normativa consultada:

```text
WEBBY READINESS SCORE = normalized model score
```

Default:

```text
mean(valid dimensions)
```

A saída deve incluir:

```text
MODEL SCORE — not an official Webby score
```

## 9.3 Avaliação por dimensão

### Content

- relevância;
- clareza;
- ponto de vista/voz;
- adequação ao meio;
- qualidade multimídia;
- capacidade de manter interesse.

### Structure & Navigation

- organização;
- priorização;
- mental model;
- transparência;
- consistência;
- velocidade de descoberta.

### Visual Design

- qualidade;
- adequação;
- hierarquia;
- estética;
- inclusão;
- coerência.

### Functionality

- funcionamento real;
- links;
- velocidade;
- compatibilidade;
- tecnologia pertinente;
- diversidade de dispositivos/condições;
- acessibilidade funcional.

### Interactivity

- ação/reação;
- feedback;
- riqueza de interação;
- utilidade;
- relação com o meio web.

### Innovation

- novidade pertinente;
- aplicação de técnica/conceito;
- valor gerado;
- não premiar novelty sem propósito.

### Overall Experience

- coesão;
- memorabilidade;
- satisfação;
- intenção de retornar/continuar;
- integração dos componentes.

---

# 10. AWARD ENGINE — CSS DESIGN AWARDS

Dimensões principais:

```text
UI         0–10
UX         0–10
Innovation 0–10
```

## UI

- estética;
- composição;
- tipografia;
- detalhes;
- visual states;
- efeitos;
- consistência;
- responsividade.

## UX

- navegação;
- funcionalidade;
- compreensão;
- feedback;
- acessibilidade prática;
- device behavior;
- tarefa.

## Innovation

- novas ideias de design;
- novas ideias de desenvolvimento;
- originalidade de interação;
- integração;
- valor real.

## WOTD readiness

A skill pode apresentar:

```text
CSSDA JURY SIMULATION
UI: 8.4
UX: 8.1
Innovation: 8.3
Internal mean: 8.27
WOTD reference threshold: currently around > 8.00 per CSSDA About, variable by submission quality.
```

Não declarar WOTD garantido.

## Public awards

Não prever resultado de votação pública.

Exibir:

```text
PUBLIC VOTE COMPONENT: NOT PREDICTED
```

---

# 11. AWARD ENGINE — FWA

O FWA utiliza uma rubrica interna da skill, calibrada contra corpus de projetos reconhecidos.

## Rubrica heurística inicial

| Dimensão | Peso interno |
|---|---:|
| Concept strength | 25% |
| Innovation | 20% |
| Craft / execution | 20% |
| Experience / engagement | 15% |
| Technical execution | 10% |
| Memorability | 10% |

Saída:

```text
FWA SIMULATED JUDGMENT
Score: 8.3 / 10
Confidence: 86%
Method: empirical rubric calibrated against FWA-recognized corpus.
```

A calibragem deve poder alterar pesos internos no futuro sem reescrever a história: toda auditoria registra `rubric_version`.

---

# 12. SEO ENGINE — QUALITY SCORE

Escala: 0–100.

| Área | Peso |
|---|---:|
| Crawlability & Indexability | 15 |
| Technical SEO | 15 |
| Architecture & Internal Linking | 10 |
| On-page & Semantics | 15 |
| Content & Search Intent | 15 |
| Performance / CWV | 10 |
| Structured Data & SERP Appearance | 7 |
| Image & Media SEO | 5 |
| Mobile / accessibility-adjacent discoverability | 5 |
| Trust / Spam / Risk hygiene | 3 |
| **Total** | **100** |

## 12.1 Crawlability & Indexability

Verificar:

- status HTTP;
- robots.txt;
- meta robots;
- X-Robots-Tag;
- canonical;
- sitemap;
- noindex;
- blocked resources;
- orphan pages;
- redirects;
- redirect chains;
- soft 404;
- URL discoverability;
- JS rendering;
- canonical conflicts;
- pagination quando aplicável.

### Blockers

Exemplos que podem limitar/capar a nota:

- site inteiro em noindex;
- robots bloqueando conteúdo principal;
- canonicals generalizados incorretamente;
- conteúdo principal indisponível para crawler;
- maioria das páginas retornando erro/soft-404.

---

## 12.2 Technical SEO

- HTML válido o suficiente para interpretação;
- metadata;
- HTTP/HTTPS;
- redirects;
- hreflang quando aplicável;
- status consistency;
- renderização;
- scripts que bloqueiam conteúdo;
- canonicalization;
- sitemap hygiene.

---

## 12.3 Architecture & Internal Linking

- profundidade;
- caminhos de descoberta;
- orphan pages;
- anchor text;
- topical grouping;
- breadcrumbs;
- links crawlable;
- hub pages;
- relevância contextual.

---

## 12.4 On-page & Semantics

- title;
- main heading;
- headings;
- descriptive language;
- semantic HTML;
- entity clarity;
- metadata;
- alt contextual;
- internal anchors;
- URL descriptiveness.

---

## 12.5 Content & Search Intent

- utilidade;
- originalidade;
- people-first quality;
- completude;
- intenção;
- consistência;
- atualização;
- redundância;
- canibalização;
- thin pages;
- topical coverage.

---

## 12.6 Performance / CWV

Separar:

```text
FIELD DATA
LAB DATA
```

Nunca substituir silenciosamente um pelo outro.

Thresholds de referência atuais:

```text
LCP <= 2.5 s
INP <= 200 ms
CLS <= 0.1
Target: P75, mobile and desktop separately
```

---

## 12.7 Structured Data & SERP Appearance

Verificar:

- JSON-LD/microdata quando aplicável;
- validade;
- adequação ao conteúdo;
- rich-result eligibility;
- title links;
- snippet readiness;
- breadcrumbs;
- favicon/site name quando pertinente;
- schemas de entidade apropriados.

Nunca afirmar:

```text
schema válido = rich result garantido
```

Usar:

```text
ELIGIBLE
NOT ELIGIBLE
NOT VERIFIED
```

---

## 12.8 Image & Media SEO

- alt;
- contexto textual;
- dimensões;
- formatos;
- filenames quando relevante;
- loading;
- discoverability;
- video pages;
- metadata de vídeo/imagem quando aplicável.

---

## 12.9 Trust / Spam / Risk

Auditar práticas potencialmente problemáticas à luz das Search Essentials e spam policies.

Não produzir acusações sem evidência.

---

# 13. ORGANIC VISIBILITY — CAMADA SEPARADA

Não misturar qualidade SEO com desempenho orgânico real.

## BLACK BOX

Sem Search Console:

```text
SEO QUALITY: 92/100
ORGANIC VISIBILITY: NOT VERIFIED
```

## CONNECTED / FORENSIC

Com dados autorizados:

- clicks;
- impressions;
- CTR;
- average position;
- query clusters;
- landing pages;
- index coverage;
- device;
- country;
- period;
- trend;
- cannibalization signals.

Sempre informar período analisado.

---

# 14. ACCESSIBILITY ENGINE

## 14.1 Duas saídas independentes

```text
ACCESSIBILITY QUALITY SCORE: 0–100
WCAG 2.2 CONFORMANCE: A / AA / AAA / PARTIAL / NOT VERIFIED
```

O score nunca substitui conformance.

## 14.2 Verificações

- teclado;
- focus order;
- visible focus;
- skip links;
- landmarks;
- headings;
- labels;
- names/roles/values;
- contrast;
- non-text contrast;
- alt;
- captions/transcripts quando aplicável;
- reduced motion;
- zoom/reflow;
- target size;
- drag alternatives;
- status messages;
- errors;
- authentication patterns quando aplicável;
- semantics;
- ARIA correta;
- screen-reader sanity checks quando infraestrutura permitir.

## 14.3 Automated != complete

A skill deve declarar quais checks foram:

- automatizados;
- manuais;
- não verificados.

---

# 15. PERFORMANCE ENGINE

Métricas possíveis:

- LCP;
- INP/RUM;
- CLS;
- TTFB;
- FCP;
- Speed Index;
- Total Blocking Time em lab;
- JS transferred/executed;
- CSS;
- images;
- fonts;
- third-party payload;
- request count;
- main-thread work;
- long tasks;
- cache behavior;
- hydration cost;
- memory/GPU, quando mensurável.

## Performance budgets

A skill pode inferir budgets por classe de site, mas deve rotulá-los como internos.

Exemplo:

```text
Budget type: inferred
Hero initial media: 1.2 MB target
Initial JS: 250 KB compressed target
```

Não tratar budget inferido como padrão oficial.

---

# 16. UX ENGINE

Dimensões:

- information architecture;
- navigation;
- orientation;
- task flow;
- feedback;
- affordance;
- error prevention;
- error recovery;
- cognitive load;
- reading flow;
- forms;
- touch;
- responsiveness;
- perceived latency;
- state visibility;
- user control;
- accessibility-related usability.

A skill deve observar jornada, não somente screenshot.

---

# 17. DESIGN / VISUAL ENGINE

## Typography

- family system;
- weights;
- scale;
- line-height;
- tracking;
- measure;
- optical behavior;
- hierarchy;
- responsive scaling;
- font loading;
- contrast.

## Layout

- grid;
- alignment;
- spacing;
- negative space;
- density;
- rhythm;
- responsive composition;
- content width;
- section transitions.

## Art Direction

- visual language;
- imagery;
- cropping;
- consistency;
- brand coherence;
- distinctiveness;
- image-text relationship.

## UI System

- tokens;
- components;
- consistency;
- states;
- polish;
- edge cases.

---

# 18. MOTION & INTERACTION ENGINE

Avaliar:

- purpose;
- hierarchy;
- timing;
- easing;
- continuity;
- spatial logic;
- scroll mapping;
- gesture mapping;
- microinteraction;
- transition consistency;
- motion density;
- reduced motion;
- performance cost;
- discoverability;
- feedback.

Exemplo de diagnóstico:

```text
MOTION DENSITY: HIGH
Issue: four competing animation systems during initial orientation.
Benchmark: top cohort generally preserves one dominant motion hierarchy per viewport.
Impact:
  Creativity +0.2
  Usability -0.8
  Accessibility -0.3
Net assessment: harmful in current implementation.
```

---

# 19. CONTENT ENGINE

Avaliar:

- clareza;
- voz;
- relevância;
- diferenciação;
- consistência;
- estrutura;
- narrativa;
- microcopy;
- CTA;
- densidade;
- redundância;
- clichês;
- media storytelling;
- adequação ao público;
- adequação à interface;
- freshness.

Conteúdo não pode receber nota alta apenas porque “há pouco texto”.

---

# 20. CONVERSION / GOAL EFFECTIVENESS ENGINE

Primeiro identificar objetivo:

```text
lead
sale
signup
booking
contact
read
explore
share
apply
subscribe
other
```

Depois medir:

- clarity of value;
- CTA discoverability;
- friction;
- trust cues;
- task completion;
- form burden;
- interruption;
- continuity;
- post-action feedback.

Não otimizar conversão destruindo integridade visual ou experiência. Reportar trade-offs.

---

# 21. ENGINEERING ENGINE

Quando houver acesso suficiente:

- architecture;
- component boundaries;
- duplicate code;
- dead code;
- dependency load;
- bundle splitting;
- rendering strategy;
- hydration;
- caching;
- image pipeline;
- font strategy;
- third-party scripts;
- state management;
- error boundaries;
- observability;
- maintainability;
- testability;
- build warnings;
- console errors.

Sem source access:

```text
ENGINEERING SCORE: PARTIAL / BLACK-BOX
```

Não inferir qualidade interna completa apenas pelo bundle final.

---

# 22. RESILIENCE ENGINE

Testar, quando aplicável:

- 404;
- failed API;
- slow API;
- broken image;
- timeout;
- offline/intermittent network;
- failed form submission;
- empty state;
- partial content;
- loading states;
- auth expiry;
- JS failure fallback quando pertinente.

---

# 23. SECURITY & PRIVACY HYGIENE

Esta camada **não é pentest**.

Verificar somente higiene observável/autorizada:

- HTTPS;
- mixed content;
- security headers principais;
- insecure third-party resources;
- obvious secret exposure;
- excessive tracking;
- consent behavior quando aplicável;
- vulnerable dependency signals quando source access permitir;
- unsafe forms/practices visíveis.

Nunca explorar vulnerabilidades destrutivamente.

---

# 24. BENCHMARK INTELLIGENCE ENGINE

Esta é uma camada central da skill.

## 24.1 Objetivo

Construir padrões comparáveis usando trabalhos reconhecidos por:

- Awwwards;
- Webby;
- FWA;
- CSS Design Awards.

E, quando apropriado, líderes orgânicos para SEO.

---

## 24.2 Tipos de coorte

### A. Direct Peers

Compatibilidade por:

- site type;
- business intent;
- content density;
- interaction intensity;
- vertical;
- user journey;
- device orientation;
- product vs showcase.

### B. Award Category Peers

Projetos da mesma categoria ou categoria mais próxima.

### C. Elite Cohort

Exemplos:

- SOTD/SOTM/SOTY;
- Webby Winners;
- CSSDA WOTD/WOTM/WOTY;
- FWA of the Day/Month/Year quando disponível.

### D. Multi-Award Cohort

Projetos reconhecidos em mais de um sistema de premiação.

### E. Temporal Cohort

```text
CURRENT: <= 24 months
RECENT:  <= 36 months
HISTORICAL: > 36 months
LEGACY/INFLUENTIAL: curated historical
```

---

## 24.3 Tamanho mínimo

Recomendação:

```text
QUICK: 12–20
FULL: 20–50
FORENSIC: 40–100+
ELITE SUBCOHORT: >= 10 quando possível
```

Se n for pequeno:

```text
BENCHMARK CONFIDENCE: LOW SAMPLE SIZE
```

---

## 24.4 Seleção robusta

Preferir:

- median;
- percentiles;
- IQR;
- trimmed mean quando necessário.

Evitar depender apenas da média, que pode ser dominada por outliers.

---

# 25. AWARD VERSION INTEGRITY

Problema:

Um site premiado em 2024 pode ter sido redesenhado em 2026.

A skill deve separar:

```text
AWARD VERSION
CURRENT LIVE VERSION
```

Registro:

```yaml
award_date: 2024-03-18
award_archive_evidence: available
current_live_snapshot_date: 2026-09-28
version_equivalence: not_confirmed
```

Regra:

> Nunca dizer que o site atual é o site que recebeu o prêmio sem evidência de equivalência.

Se houver apenas live version:

```text
USE: contemporary reference only
NOT: historical award-version evidence
```

---

# 26. BENCHMARK SOURCE RECORD

Cada referência deve registrar:

```yaml
id: benchmark_x
name: Example
url: https://example.com
award_source: awwwards
award_level: SOTD
award_category: portfolio
award_date: 2026-04-10
source_url: https://...
site_type: portfolio
vertical: creative
interaction_intensity: high
content_density: low
award_version_verified: true
current_version_checked: true
snapshot_date: 2026-09-28
features:
  typography: ...
  navigation: ...
  motion: ...
  performance: ...
provenance: official_gallery
```

---

# 27. SOURCE GOVERNANCE

Para benchmark automático:

1. priorizar fontes oficiais;
2. respeitar robots/termos aplicáveis;
3. não contornar autenticação/paywall;
4. limitar requisições;
5. cachear metadados;
6. registrar provenance;
7. não copiar conteúdo integral protegido desnecessariamente;
8. armazenar preferencialmente metadados, métricas e features derivadas;
9. screenshots de benchmark somente quando permitidos/necessários para auditoria interna;
10. manter links de origem.

---

# 28. PATTERN MINING ENGINE

Para cada padrão:

```yaml
pattern: dominant_visual_hero
observed_count: 31
cohort_size: 38
frequency: 0.816
classification: EXPECTED
award_correlation: moderate
causality: not_claimed
notes: ...
```

## Classificações

### REQUIRED
Necessidade normativa/funcional ou quase indispensável para a dimensão.

### EXPECTED
Muito recorrente entre referências fortes e coerente com a finalidade.

### ADVANTAGE
Pode produzir vantagem competitiva quando bem executado.

### OPTIONAL
Ausência não deve gerar penalização.

### TREND
Recorrente no período atual, mas não estrutural.

### EXPERIMENTAL
Baixa incidência ou abordagem emergente.

### ANTI-PATTERN
Padrão associado a problemas de experiência, performance ou qualidade.

### NOT CORRELATED
Aparece nos vencedores, mas não há evidência suficiente para tratá-lo como fator relevante.

---

# 29. DISTINCTIVENESS ENGINE

Objetivo:

> avaliar se o projeto tem identidade própria ou apenas reproduz convenções de galerias de premiação.

Dimensões:

- typography similarity;
- layout similarity;
- hero composition;
- navigation model;
- motion language;
- transition model;
- color treatment;
- cursor model;
- interaction grammar;
- visual motif;
- content architecture.

Saída:

```text
DISTINCTIVENESS: 74/100

High:
- art direction
- imagery treatment

Medium:
- typography

Low:
- hero architecture

Observation:
Hero structure appears in 37% of recent direct-peer award cohort.
Classification: trend saturation risk.
```

Similaridade nunca deve gerar acusação de cópia sem evidência específica.

---

# 30. INNOVATION VS GIMMICK

Criar índice interno:

```text
INNOVATION VALUE
```

Fatores:

- novelty;
- purpose;
- integration;
- execution;
- memorability;
- usability cost;
- accessibility cost;
- performance cost;
- maintenance cost.

Exemplo:

```text
3D hero
Novelty: +0.4
Brand integration: +0.6
Memorability: +0.3
Performance: -0.8
Accessibility: -0.3
Usability: -0.2

Net: 0.0
Classification: GIMMICK RISK
```

---

# 31. EVIDENCE ENGINE

Toda auditoria deve gerar um pacote mínimo de evidências.

```text
URL
canonical URL
timestamp
rubric versions
benchmark dataset version
browser
viewport
device profile
network profile
HTML/DOM evidence
headers
screenshots
performance evidence
CWV source type
robots
sitemap
structured data
console/network errors
accessibility evidence
benchmark references
```

## Tipos de evidência

```text
OBSERVED
MEASURED
SOURCE-VERIFIED
BENCHMARK-DERIVED
INFERRED
USER-PROVIDED
NOT VERIFIED
```

---

# 32. FINDING SCHEMA

Cada finding deve conter:

```yaml
id: UX-NAV-001
status: open
lens:
  - ux
  - awwwards.usability
  - webby.structure_navigation
page: /work
viewport: 390x844
browser: chromium
severity: P1
confidence: 0.94
observation: "..."
evidence:
  type: observed
  reference: "..."
criterion: "navigation clarity"
benchmark:
  cohort_id: cohort_2026_portfolio
  percentile_reference: P75
penalty:
  dimension: usability
  amount: -0.6
why_penalized: "..."
user_impact: "..."
seo_impact: "none|low|medium|high"
award_impact: "..."
recommended_action: "..."
validation: "..."
effort: medium
regression_risk: low
priority: P1
```

---

# 33. PENALTY MODEL

## 33.1 Score starts from evidence, not from optimism

Implementação recomendada:

1. avaliar subdimensões;
2. registrar evidências positivas e negativas;
3. determinar nota de subdimensão;
4. consolidar dimensão;
5. aplicar caps/bloqueadores;
6. registrar deduções explicáveis.

Não iniciar automaticamente em 10 e apenas deduzir se isso induzir inflação.

## 33.2 No double punishment

Uma causa-raiz não deve receber múltiplas deduções dentro da mesma dimensão apenas porque se manifesta várias vezes.

Pode afetar dimensões diferentes quando o efeito é genuinamente distinto.

Exemplo:

```text
Hero video 18 MB
Performance: penalty
Awwwards Usability: penalty for perceived wait
SEO CWV: penalty
```

Isso é válido porque são lentes diferentes.

Mas não deduzir três vezes em Performance pelo mesmo download.

---

# 34. SEVERITY MODEL

## P0 — BLOCKER / CRITICAL

- impede tarefa essencial;
- site/área indisponível;
- indexabilidade crítica;
- acessibilidade grave de fluxo;
- segurança/higiene crítica observada;
- regressão que inviabiliza experiência principal.

## P1 — HIGH

Grande impacto em experiência, prêmio, SEO ou conversão.

## P2 — MEDIUM

Impacto real, mas não bloqueador.

## P3 — POLISH

Refinamento, acabamento ou otimização menor.

## P4 — OPPORTUNITY / EXPERIMENTAL

Não é defeito. Possível avanço/diferenciação.

---

# 35. SCORE CAPS

Para impedir que média esconda falhas graves.

Exemplos internos ajustáveis:

```text
If main task impossible on mobile:
  UX max = 5.0 until resolved

If entire public site unintentionally noindex:
  SEO Quality max = 35

If keyboard cannot operate primary navigation:
  Accessibility quality max = 60
  WCAG AA cannot be claimed

If primary page consistently crashes:
  Engineering/Resilience max = 50
```

Caps devem estar documentados e versionados.

---

# 36. CONFIDENCE SCORE

Escala 0–100.

Proposta:

| Componente | Peso |
|---|---:|
| Evidence coverage | 35% |
| Benchmark fit | 25% |
| Measurement quality | 20% |
| Repeatability | 20% |

Classificação:

```text
90–100 VERY HIGH
80–89  HIGH
60–79  MEDIUM
<60    LOW
```

Toda nota principal deve possuir confidence.

---

# 37. BENCHMARK PERCENTILES

Quando houver amostra suficiente:

```text
TYPOGRAPHY
Your score: 8.1

P25  7.3
P50  7.8
P75  8.4
P90  8.8
P95  9.1

Relative position: P68
```

Não calcular percentil com corpus inadequado ou pequeno sem aviso.

---

# 38. AWARD GAP ANALYSIS

Não inventar cutoffs oficiais.

Usar faixas derivadas do corpus e rotular:

```text
EMPIRICAL BENCHMARK RANGE
```

Exemplo:

```text
Current: 7.36
Recent direct-peer median: 7.82
Recent elite P25: 8.41
Gap to elite P25: +1.05
```

Isso é superior a afirmar “8.5 garante SOTD”.

---

# 39. DECISION ENGINE

A nota não é o produto principal. O produto principal é a tomada de decisão.

## 39.1 Fatores

- severity;
- user impact;
- award impact;
- SEO impact;
- accessibility impact;
- conversion impact;
- confidence;
- breadth;
- implementation effort;
- regression risk;
- leverage.

## 39.2 Priority ranking

Usar matriz explicável, não falsa precisão.

Exemplo interno:

```text
priority_value =
severity_factor
* impact_breadth
* confidence
* leverage
/ effort_factor
```

O valor serve apenas para ordenar findings semelhantes.

A classificação P0–P4 é soberana.

---

# 40. OUTPUT DE DECISÃO

Tabela mínima:

| Finding | Lost score | Impact | Effort | Confidence | Priority |
|---|---:|---|---|---:|---|
| Mobile navigation | -1.4 | Very High | Medium | 94% | P0/P1 |
| Hero LCP | -0.9 | Very High | Low | 98% | P0/P1 |
| Type scale | -0.4 | Medium | Low | 90% | P2 |
| Custom cursor | 0 | Low | Medium | 84% | P4 |

---

# 41. DO NOT CHANGE

Obrigatório em FULL/FORENSIC.

Objetivo:

- preservar acertos;
- evitar regressões de redesign;
- distinguir problema de preferência pessoal.

Exemplo:

```text
DO NOT CHANGE

1. Hero typography
Reason: P88 against direct-peer cohort; strong hierarchy; no accessibility penalty.

2. Navigation transition
Reason: distinctive and does not impair task completion.

3. Image treatment
Reason: high distinctiveness and consistent art direction.
```

---

# 42. DIGITAL EXCELLENCE SCORE — DES

Esta métrica é **da skill**, não das premiações.

Importante: award scores não entram diretamente no DES para evitar dupla contagem.

## Estrutura inicial

| Eixo | Peso |
|---|---:|
| Experience Craft / Visual & Interaction | 25 |
| UX / Usability | 15 |
| Engineering & Performance | 20 |
| SEO / Discoverability | 15 |
| Accessibility | 10 |
| Content | 5 |
| Conversion / Goal Effectiveness | 5 |
| Resilience + Security/Privacy Hygiene | 5 |
| **Total** | **100** |

Cross-device funciona como multiplicador/cap transversal, não como eixo isolado.

## Regra

```text
DES != award probability
DES != SEO ranking probability
DES = internal holistic product-quality indicator
```

Aplicar caps quando P0 existir.

---

# 43. CROSS-DEVICE CONSISTENCY

Avaliar variação entre dispositivos.

Exemplo:

```text
DESKTOP UX   8.8
MOBILE UX    6.4
TABLET UX    7.9

CROSS-DEVICE CONSISTENCY: 63/100
Penalty source: mobile navigation + interaction overlap.
```

Um desktop excelente não pode esconder mobile ruim.

---

# 44. REGRESSION ENGINE

Cada execução deve aceitar `previous_audit`.

Exemplo:

```text
AUDIT #001 2026-09-28
AUDIT #002 2026-10-14

Design         8.1 -> 8.5  +0.4
UX             7.4 -> 8.2  +0.8
SEO           71   -> 89   +18
Performance   83   -> 76   -7   REGRESSION
```

## Regras

- comparar mesmas páginas/viewport quando possível;
- marcar alteração de metodologia;
- não comparar métricas incompatíveis;
- detectar resolved/new/regressed;
- apontar provável commit/release somente se evidência existir.

---

# 45. CALIBRATION ENGINE

A skill precisa ser calibrada contra sites premiados reais.

Corpus inicial recomendado:

```text
Awwwards SOTY/SOTM/SOTD
CSSDA WOTD/WOTM/WOTY
FWA recognized cases
Webby Winners/Nominees
```

Objetivo:

- evitar inflação de notas;
- evitar severidade excessiva;
- verificar distribuição;
- ajustar subrubricas;
- testar concordância entre evaluator e corpus.

## Teste de sanidade

Se sites medianos recebem 9.0 frequentemente:

```text
FAIL: score inflation
```

Se vencedores consistentes ficam em 6.0–7.0 sem razão documentada:

```text
FAIL: over-severity or rubric mismatch
```

---

# 46. ANTI-BIAS ENGINE

A skill deve verificar explicitamente vieses:

- recency bias;
- trend bias;
- technology bias;
- complexity bias;
- minimalism bias;
- maximalism bias;
- Western-design bias quando contexto exigir;
- preference for animation;
- preference for dark mode;
- preference for large type;
- preference for 3D/WebGL.

Pergunta obrigatória antes de premiar um padrão:

> “Isso melhora esta experiência específica ou apenas se parece com trabalhos premiados?”

---

# 47. CATEGORY FIT ENGINE

A skill pode identificar categorias compatíveis para benchmark/submissão.

Saída:

```text
CATEGORY FIT
Awwwards: Portfolio / Photography / Experimental
Webby: Best User Interface / Best Visual Design
CSSDA: UI + Innovation
FWA: immersive/creative experience peer cohort
```

Isto é classificação de compatibilidade, não garantia de prêmio.

---

# 48. REPORT — EXECUTIVE AUDIT

Formato máximo recomendado: 2–8 páginas equivalentes em markdown.

Estrutura:

```text
1. Executive result
2. Award readiness
3. DES
4. SEO
5. Accessibility
6. Performance
7. Biggest strengths
8. Biggest gaps
9. P0/P1 findings
10. Top actions
11. Do not change
12. Confidence & coverage
```

---

# 49. REPORT — FORENSIC AUDIT

Estrutura:

```text
DIGITAL EXPERIENCE JURY AUDIT

00 Executive Summary
01 Scope & Method
02 Evidence Coverage
03 Awwwards
04 Webby
05 FWA
06 CSSDA
07 Benchmark Cohorts
08 Pattern Mining
09 Distinctiveness
10 Design
11 UX
12 Motion & Interaction
13 Content
14 Performance
15 SEO
16 Organic Visibility
17 Accessibility
18 Engineering
19 Conversion
20 Resilience
21 Security/Privacy Hygiene
22 Cross-device
23 Findings Register
24 Award Gap Analysis
25 Decision Roadmap
26 Do Not Change
27 Regression
28 Confidence
29 Limitations
30 Sources & Dataset Version
```

---

# 50. MACHINE-READABLE OUTPUTS

Recomendados:

```text
report-executive.md
report-forensic.md
findings.json
scores.json
benchmark-summary.json
evidence-manifest.json
regression.json
```

---

# 51. SCORES.JSON — EXEMPLO

```json
{
  "audit_id": "2026-09-28-example",
  "rubric_version": "1.0",
  "awwwards": {
    "design": 8.4,
    "usability": 7.9,
    "creativity": 8.1,
    "content": 7.8,
    "readiness": 8.11,
    "confidence": 0.91
  },
  "webby": {
    "score_type": "model_score",
    "readiness": 8.22,
    "confidence": 0.88
  },
  "cssda": {
    "ui": 8.5,
    "ux": 8.0,
    "innovation": 8.2,
    "confidence": 0.90
  },
  "fwa": {
    "score_type": "simulated_judgment",
    "readiness": 8.3,
    "confidence": 0.84
  },
  "seo_quality": 87,
  "accessibility_quality": 91,
  "des": 88.4
}
```

---

# 52. SKILL FILE TREE

Estrutura recomendada:

```text
digital-experience-jury-auditor/
│
├── SKILL.md
├── README.md
│
├── config/
│   ├── rubric-versions.yaml
│   ├── severity.yaml
│   ├── score-caps.yaml
│   ├── audit-modes.yaml
│   └── source-policy.yaml
│
├── rubrics/
│   ├── awwwards.md
│   ├── webby.md
│   ├── fwa.md
│   ├── cssda.md
│   ├── seo.md
│   ├── accessibility.md
│   ├── performance.md
│   ├── ux.md
│   ├── visual-design.md
│   ├── motion-interaction.md
│   ├── content.md
│   ├── engineering.md
│   ├── conversion.md
│   ├── resilience.md
│   └── security-hygiene.md
│
├── benchmark/
│   ├── benchmark-schema.md
│   ├── cohort-selection.md
│   ├── award-version-integrity.md
│   ├── pattern-mining.md
│   ├── distinctiveness.md
│   └── cache-policy.md
│
├── schemas/
│   ├── finding.schema.json
│   ├── scores.schema.json
│   ├── benchmark.schema.json
│   ├── evidence.schema.json
│   └── regression.schema.json
│
├── templates/
│   ├── executive-report.md
│   ├── forensic-report.md
│   ├── finding.md
│   └── regression-report.md
│
├── calibration/
│   ├── protocol.md
│   ├── corpus-manifest.json
│   └── acceptance-tests.md
│
└── references/
    ├── normative-sources.md
    └── changelog.md
```

---

# 53. SKILL.MD — CONTRATO FUNCIONAL

O `SKILL.md` implementado deve conter no mínimo:

```text
ROLE
You are a rigorous digital experience auditor and simulated award juror.

GOAL
Evaluate a website using award-specific rubrics, objective web quality checks,
SEO, accessibility, engineering and contextual benchmarks.

NON-NEGOTIABLES
- no evidence = no score
- never call simulated scores official
- explain every penalty
- benchmark only against compatible cohorts
- distinguish correlation from requirement
- distinguish field from lab data
- preserve successful areas with DO NOT CHANGE
- report limitations
- show confidence
- prioritize decisions, not cosmetic changes
```

---

# 54. EXECUTION RULES FOR THE AGENT

## Before scoring

The agent MUST:

1. validate rubric freshness;
2. determine audit mode;
3. map site type and goal;
4. establish page coverage;
5. gather evidence;
6. build or load relevant benchmark cohort.

## During scoring

The agent MUST:

- cite findings to evidence;
- avoid double punishment;
- apply caps consistently;
- mark unverified areas;
- distinguish objective failures from qualitative judgment;
- include confidence.

## After scoring

The agent MUST:

- produce strengths;
- produce weaknesses;
- explain lost points;
- identify missing capabilities;
- provide decision priorities;
- provide do-not-change list;
- record benchmark provenance;
- record rubric/dataset versions.

---

# 55. “WHAT IS MISSING?” REQUIREMENT

Para cada dimensão abaixo de 9.0 ou abaixo do target selecionado, a skill deve produzir explicitamente:

```text
WHAT IS MISSING TO REACH NEXT LEVEL
```

Formato:

```text
Current: 7.6
Next target: 8.0
Missing:
1. ...
2. ...
3. ...

Estimated recoverable gap: +0.5 to +0.8
Confidence: 88%
```

Não prometer ganho exato quando qualitativo.

---

# 56. POSITIVE EVIDENCE REQUIREMENT

A skill deve registrar acertos com o mesmo rigor dos erros.

Cada dimensão inclui:

```text
WHAT IS WORKING
WHY IT WORKS
BENCHMARK POSITION
DO NOT CHANGE / SAFE TO EVOLVE
```

Isso evita auditoria enviesada para negatividade.

---

# 57. ROOT CAUSE REQUIREMENT

Problemas devem ser agrupados por causa-raiz.

Exemplo:

```text
ROOT CAUSE: oversized autoplay hero video
Effects:
- LCP
- mobile data cost
- perceived speed
- Awwwards usability
- Webby functionality
- SEO CWV
```

A recomendação deve atacar a causa-raiz, não seis sintomas separadamente.

---

# 58. TRADE-OFF REPORTING

Toda recomendação com trade-off relevante deve exibir:

```text
GAIN
LOSS/RISK
NET EXPECTED EFFECT
VALIDATION PLAN
```

Exemplo:

```text
Add scroll-linked WebGL scene
GAIN: creativity, memorability
RISK: LCP, GPU load, motion sensitivity, mobile battery
NET: uncertain
Decision: P4 experimental, prototype behind feature flag
```

---

# 59. BLACK-BOX VS SOURCE-ASSISTED

## Black-box

Pode avaliar:

- render;
- network;
- DOM;
- accessible tree quando disponível;
- runtime;
- SEO público;
- CWV/lab;
- interaction;
- benchmark.

Não pode afirmar integralmente:

- maintainability;
- source architecture;
- test quality;
- unused private code;
- CI quality.

## Source-assisted

Com repositório autorizado:

- build;
- component architecture;
- dependency graph;
- dead code;
- test coverage;
- code-level performance;
- security dependency signals;
- SSR/CSR/SSG strategy;
- caching implementation.

---

# 60. PRIVACY / SECRETS

Quando houver source access:

- não incluir secrets em relatório;
- mascarar tokens;
- não enviar credenciais a benchmarks externos;
- não armazenar `.env` no evidence package;
- citar apenas presença do risco.

Exemplo:

```text
CRITICAL: secret-like credential found in client bundle.
Value: [REDACTED]
```

---

# 61. UPDATE POLICY

Rubricas e fontes podem mudar.

Antes de auditoria importante:

```text
check official criteria freshness
compare last_verified_at
update rubric_version if needed
```

Se um prêmio alterar critérios:

- manter versões anteriores;
- não recalcular auditorias históricas silenciosamente;
- marcar auditorias novas com nova rubric version.

---

# 62. ACCEPTANCE TESTS DA SKILL

A implementação não é considerada pronta até passar pelos testes abaixo.

## A. Evidence integrity

Dado um finding, é possível localizar a evidência?

**PASS obrigatório.**

## B. Penalty explainability

Toda dedução possui motivo e critério?

**PASS obrigatório.**

## C. No fake official scores

Webby/FWA/CSSDA/Awwwards simulation está corretamente rotulada?

**PASS obrigatório.**

## D. Benchmark fit

A coorte possui compatibilidade documentada?

**PASS obrigatório.**

## E. Version integrity

Live version e award version não são confundidas?

**PASS obrigatório.**

## F. SEO separation

SEO Quality e Organic Visibility estão separados?

**PASS obrigatório.**

## G. Lab vs field

CWV de laboratório e campo estão separados?

**PASS obrigatório.**

## H. Accessibility

Score interno não é apresentado como certificação WCAG?

**PASS obrigatório.**

## I. Anti-hype

Tecnologia sofisticada pode receber impacto líquido negativo?

**PASS obrigatório.**

## J. Do not change

FULL/FORENSIC gera áreas preserváveis?

**PASS obrigatório.**

## K. Root cause

Findings relacionados são consolidados por causa-raiz?

**PASS obrigatório.**

## L. Regression

Mudanças entre auditorias são corretamente categorizadas?

**PASS obrigatório.**

## M. Confidence

Toda nota central possui confidence?

**PASS obrigatório.**

## N. Missing-to-next-level

Toda dimensão abaixo do target explica o que falta?

**PASS obrigatório.**

---

# 63. EXEMPLO DE SAÍDA EXECUTIVA

```text
DIGITAL EXPERIENCE JURY AUDIT
Date: 2026-09-28
Mode: FULL
Coverage: 89%
Overall confidence: 91%

AWARD READINESS
Awwwards          8.21 / 10
Webby             8.47 / 10  [MODEL SCORE]
FWA               8.30 / 10  [SIMULATED]
CSSDA UI          8.55 / 10
CSSDA UX          8.10 / 10
CSSDA Innovation  8.25 / 10

QUALITY
DES                88 / 100
SEO Quality         87 / 100
Accessibility       92 / 100
Performance         81 / 100
Engineering         89 / 100

BENCHMARK
Direct peer cohort: n=42
Elite cohort: n=15
Relative position: P82

TOP STRENGTHS
1. ...
2. ...
3. ...

P0
None

P1
1. Mobile navigation
2. Hero LCP

WHAT IS MISSING FOR NEXT LEVEL
1. ...
2. ...
3. ...

DO NOT CHANGE
1. ...
2. ...

DECISION ORDER
NOW: ...
NEXT: ...
THEN: ...
EXPERIMENTAL: ...
IGNORE: ...
```

---

# 64. EXEMPLO DE FINDING COMPLETO

```text
ID: PERF-LCP-004
Page: /
Viewport: 390x844
Severity: P1
Confidence: 98%

OBSERVATION
The hero's primary media dominates initial transfer and becomes the LCP element.

MEASURED
LCP lab: 3.41 s
Target reference: <= 2.5 s
Field data: NOT VERIFIED

WHY PENALIZED
The page misses the current “good” LCP reference in the measured lab scenario.
The issue also worsens perceived responsiveness during initial orientation.

SCORE IMPACT
Performance: -8/100
SEO/CWV subscore: -3/10 points available in sub-area
Awwwards Usability: -0.3 estimated
Webby Functionality: negative

BENCHMARK
Direct peer P50 hero transfer is lower; exact causal relation to award status is not claimed.

ROOT CAUSE
Oversized first-viewport media + late resource priority.

RECOMMENDATION
Reduce initial media payload, use responsive source strategy, prioritize LCP candidate,
avoid loading non-critical visual layers before primary content.

VALIDATION
Repeat the same device/network profile. Compare cold-load LCP and visual completeness.

EFFORT
Medium

REGRESSION RISK
Low–Medium

PRIORITY
P1
```

---

# 65. IMPLEMENTATION PHASES

## Phase 1 — Core auditor

- crawl;
- render;
- evidence;
- Awwwards/Webby/CSSDA/FWA rubrics;
- SEO;
- accessibility;
- performance;
- UX;
- reports.

## Phase 2 — Benchmark engine

- official gallery connectors/crawlers;
- cohort classifier;
- version integrity;
- percentile engine;
- pattern mining.

## Phase 3 — Distinctiveness + decision

- similarity feature extraction;
- anti-hype;
- innovation/gimmick;
- root cause;
- prioritization;
- do-not-change.

## Phase 4 — Forensic integrations

- Search Console;
- Analytics/RUM;
- repository/source;
- expanded browser matrix;
- regression history.

## Phase 5 — Calibration

- build award corpus;
- run batch audits;
- compare distributions;
- adjust internal rubrics;
- lock calibration version.

---

# 66. DEFINITION OF DONE

A primeira versão produtiva da skill só está pronta quando consegue, a partir de uma URL:

1. mapear o site;
2. escolher páginas representativas;
3. coletar evidências;
4. testar desktop/mobile;
5. medir performance disponível;
6. auditar SEO;
7. auditar acessibilidade;
8. avaliar UX/design/motion/content;
9. construir coorte premiada contextual;
10. separar award-version de live-version;
11. calcular scores corretamente rotulados;
12. explicar cada penalização;
13. dizer o que falta para o próximo nível;
14. mostrar acertos;
15. gerar DO NOT CHANGE;
16. priorizar correções;
17. informar confidence;
18. registrar limitações;
19. gerar Executive + Forensic + JSON;
20. reproduzir a auditoria posteriormente.

---

# 67. REGRA-MÃE

> **A skill não existe para dizer se o site é bom. Ela existe para demonstrar, com evidência e comparação contextual, onde o site está, por que está ali, o que está funcionando, o que está prejudicando o resultado, o que falta para o próximo nível e qual é o caminho de maior impacto para chegar lá.**

E, complementarmente:

> **Nenhuma nota sem evidência. Nenhuma penalização sem justificativa. Nenhuma recomendação sem impacto. Nenhuma comparação sem coorte adequada. Nenhuma tendência tratada como requisito por mera recorrência. Nenhuma tecnologia premiada apenas por existir.**

---

# 68. REFERÊNCIAS VERIFICADAS PARA ESTA ESPECIFICAÇÃO

## Awwwards

- Evaluation System: https://www.awwwards.com/about-evaluation/
- Winning Websites: https://www.awwwards.com/websites/
- Sites of the Day: https://www.awwwards.com/websites/sites_of_the_day/

## Webby Awards

- Judging Criteria: https://www.webbyawards.com/judging-criteria/
- Judging Process: https://www.webbyawards.com/judging-process/
- Winners — Websites and Mobile Sites: https://winners.webbyawards.com/winners/websites-and-mobile-sites

## CSS Design Awards

- About / award system: https://www.cssdesignawards.com/about

## FWA

- Main site: https://thefwa.com/
- Cases: https://thefwa.com/cases/

## Google Search

- Search Essentials: https://developers.google.com/search/docs/essentials
- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide

## Core Web Vitals

- Web Vitals: https://web.dev/articles/vitals
- LCP: https://web.dev/articles/lcp
- INP: https://web.dev/articles/inp
- CLS: https://web.dev/articles/cls

## Accessibility

- WCAG 2.2: https://www.w3.org/TR/WCAG22/

---

# 69. CHANGE CONTROL

Esta especificação é a **baseline arquitetural v1.0**.

A partir deste ponto:

- novas ideias entram como change request;
- mudanças de critério oficial geram nova rubric version;
- mudanças de fórmula interna geram calibration/rubric version;
- auditorias históricas preservam a versão utilizada;
- nenhuma alteração retroativa silenciosa é permitida.

**Concepção funcional: FECHADA.**  
**Próximo estágio: implementação dos arquivos reais da skill e motor de execução.**
