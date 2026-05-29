import os

file_path = "/Users/andrezconz/Library/Mobile Documents/com~apple~CloudDocs/Antigravity/orion/orion/portfolio-government-solutions.html"
out_path = "/Users/andrezconz/Library/Mobile Documents/com~apple~CloudDocs/Antigravity/orion/orion/portfolio-government-solutions-en.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Translations map
translations = {
    '<html lang="es">': '<html lang="en">',
    'Portafolio de Servicios': 'Service Portfolio',
    'Analítica aplicada y estrategia para el sector público colombiano. Transformamos datos territoriales en decisiones de política basadas en evidencia.': 'Applied analytics and strategy for the public sector. We transform territorial data into evidence-based policy decisions.',
    'Especialidad': 'Specialty',
    'Políticas Públicas & Datos': 'Public Policy & Data',
    'Mercado': 'Market',
    'Colombia · Cooperación Internacional': 'Colombia · International Cooperation',
    'Modalidad': 'Modality',
    'Proyecto · Retainer · Formación': 'Project · Retainer · Training',
    'Propuesta de valor': 'Value Proposition',
    'Lo que nos hace diferentes': 'What makes us different',
    'Combinamos el lenguaje institucional del sector público con capacidad analítica rigurosa. No somos una firma de datos que no entiende el gobierno, ni una consultora política que no entiende los datos.': 'We combine the institutional language of the public sector with rigorous analytical capacity. We are not a data firm that doesn\'t understand government, nor a political consultancy that doesn\'t understand data.',
    'Entendemos cómo funciona una secretaría, una mesa técnica y un proceso normativo — y al mismo tiempo diseñamos evaluaciones de impacto, modelos econométricos y dashboards de monitoreo.': 'We understand how a secretariat, a technical round table, and a regulatory process work — and at the same time we design impact evaluations, econometric models, and monitoring dashboards.',
    'Desde adentro': 'From the inside',
    'Experiencia directa en Secretarías distritales y Consejo de Planeación.': 'Direct experience in district Secretariats and Planning Councils.',
    'Rigor cuantitativo': 'Quantitative rigor',
    'Econometría, evaluación de impacto, ML aplicado al sector público.': 'Econometrics, impact evaluation, ML applied to the public sector.',
    'Red internacional': 'International network',
    'Vínculos activos con CAF, Hanns Seidel, cooperación alemana y americana.': 'Active links with CAF, Hanns Seidel, German and American cooperation.',
    'Credenciales élite': 'Elite credentials',
    'Uniandes + Externado. Certificaciones CAF, evaluación de impacto y Big Data.': 'Uniandes + Externado. CAF certifications, impact evaluation and Big Data.',
    'Fichas técnicas': 'Technical data sheets',
    'Líneas de Servicio': 'Service Lines',
    'Analítica Territorial': 'Territorial Analytics',
    'Diagnóstico de Efectividad Institucional': 'Institutional Effectiveness Diagnostic',
    '"¿Cómo saber si los servicios que prestamos realmente están funcionando?"': '"How do we know if the services we provide are really working?"',
    'Medición rigurosa de resultados de programas y servicios públicos mediante metodología mixta. Combinamos análisis cuantitativo de indicadores con evaluación cualitativa de procesos para ofrecer un diagnóstico integral, accionable y presentable ante tomadores de decisión y organismos de control.': 'Rigorous measurement of results of public programs and services using a mixed methodology. We combine quantitative analysis of indicators with qualitative evaluation of processes to offer a comprehensive, actionable diagnostic, ready to present to decision-makers and oversight bodies.',
    '<span class="card-col-title">Actividades</span>': '<span class="card-col-title">Activities</span>',
    '<li>Levantamiento y limpieza de datos institucionales</li>': '<li>Collection and cleaning of institutional data</li>',
    '<li>Análisis estadístico descriptivo e inferencial</li>': '<li>Descriptive and inferential statistical analysis</li>',
    '<li>Entrevistas a actores clave y grupos focales</li>': '<li>Interviews with key actors and focus groups</li>',
    '<li>Benchmarking con casos comparables</li>': '<li>Benchmarking against comparable cases</li>',
    '<li>Formulación de recomendaciones priorizadas</li>': '<li>Formulation of prioritized recommendations</li>',
    '<span class="card-col-title">Entregables</span>': '<span class="card-col-title">Deliverables</span>',
    '<li>Informe ejecutivo (máx. 30 páginas)</li>': '<li>Executive report (max. 30 pages)</li>',
    '<li>Dashboard interactivo de indicadores</li>': '<li>Interactive dashboard of indicators</li>',
    '<li>Presentación para directivos</li>': '<li>Presentation for directors</li>',
    '<li>Plan de mejora con hoja de ruta</li>': '<li>Improvement plan with roadmap</li>',
    '<span class="card-col-title">Clientes típicos</span>': '<span class="card-col-title">Typical Clients</span>',
    '<li>Secretarías distritales y municipales</li>': '<li>District and municipal secretariats</li>',
    '<li>Entidades descentralizadas</li>': '<li>Decentralized entities</li>',
    '<li>Organismos de cooperación</li>': '<li>Cooperation agencies</li>',
    '<li>Contralorías y veedurías</li>': '<li>Comptrollers and oversight bodies</li>',
    '<strong>Duración:</strong>': '<strong>Duration:</strong>',
    'semanas': 'weeks',
    '<strong>Equipo:</strong>': '<strong>Team:</strong>',
    'consultores': 'consultants',
    'Evaluación de Impacto': 'Impact Evaluation',
    'Evaluación de Políticas y Programas Públicos': 'Evaluation of Public Policies and Programs',
    '"¿Cómo demostrar que nuestra política generó un cambio real y no fue coincidencia?"': '"How do we show that our policy generated real change and wasn\'t a coincidence?"',
    'Diseño y ejecución de evaluaciones de impacto con métodos cuasiexperimentales: diferencias en diferencias, regresión discontinua, variables instrumentales y emparejamiento estadístico. Generamos evidencia robusta sobre causalidad que resiste el escrutinio técnico y político.': 'Design and execution of impact evaluations with quasi-experimental methods: differences in differences, regression discontinuity, instrumental variables, and statistical matching. We generate robust evidence on causality that withstands technical and political scrutiny.',
    '<li>Diseño de la estrategia de identificación causal</li>': '<li>Design of the causal identification strategy</li>',
    '<li>Construcción de base de datos de panel</li>': '<li>Construction of panel database</li>',
    '<li>Estimación econométrica y pruebas de robustez</li>': '<li>Econometric estimation and robustness tests</li>',
    '<li>Análisis de heterogeneidad de efectos</li>': '<li>Heterogeneity of effects analysis</li>',
    '<li>Validación con pares académicos</li>': '<li>Validation with academic peers</li>',
    '<li>Informe técnico con metodología detallada</li>': '<li>Technical report with detailed methodology</li>',
    '<li>Resumen ejecutivo para tomadores de decisión</li>': '<li>Executive summary for decision makers</li>',
    '<li>Código reproducible (R / Stata / Python)</li>': '<li>Reproducible code (R / Stata / Python)</li>',
    '<li>Nota de política pública (policy brief)</li>': '<li>Public policy note (policy brief)</li>',
    '<li>DNP, Prosperidad Social</li>': '<li>DNP, Social Prosperity</li>',
    '<li>BID, Banco Mundial, PNUD</li>': '<li>IDB, World Bank, UNDP</li>',
    '<li>Ministerios sectoriales</li>': '<li>Sectoral ministries</li>',
    '<li>Fundaciones con programas sociales</li>': '<li>Foundations with social programs</li>',
    'Inteligencia Territorial': 'Territorial Intelligence',
    'Mapeo Socioeconómico Territorial': 'Territorial Socioeconomic Mapping',
    '"¿Cómo identificar con precisión dónde están las brechas y cómo priorizar la inversión?"': '"How do we accurately identify where the gaps are and prioritize investment?"',
    'Análisis geoespacial de indicadores socioeconómicos a nivel sublocal: pobreza multidimensional, acceso a servicios, brechas de género, concentración de vulnerabilidades. Producimos capas de información que permiten focalizar la inversión pública con criterios técnicos defensibles.': 'Geospatial analysis of socioeconomic indicators at the sub-local level: multidimensional poverty, access to services, gender gaps, concentration of vulnerabilities. We produce layers of information that allow targeting public investment with defensible technical criteria.',
    '<li>Integración de fuentes (DANE, SDP, SISBEN)</li>': '<li>Integration of sources (DANE, SDP, SISBEN)</li>',
    '<li>Análisis espacial y construcción de índices</li>': '<li>Spatial analysis and index construction</li>',
    '<li>Modelación de brechas por unidad territorial</li>': '<li>Modeling of gaps by territorial unit</li>',
    '<li>Cruce con datos de oferta institucional</li>': '<li>Cross-referencing with institutional supply data</li>',
    '<li>Talleres de validación con comunidad</li>': '<li>Validation workshops with the community</li>',
    '<li>Atlas territorial digital interactivo</li>': '<li>Interactive digital territorial atlas</li>',
    '<li>Índice de priorización territorial</li>': '<li>Territorial prioritization index</li>',
    '<li>Informe narrativo con hallazgos clave</li>': '<li>Narrative report with key findings</li>',
    '<li>Shapefile y datos en formato abierto</li>': '<li>Shapefile and open format data</li>',
    '<li>Secretarías de Planeación</li>': '<li>Planning Secretariats</li>',
    '<li>Alcaldías locales</li>': '<li>Local mayoralties</li>',
    '<li>Fondos de Desarrollo Local</li>': '<li>Local Development Funds</li>',
    '<li>USAID, GIZ, UE en Colombia</li>': '<li>USAID, GIZ, EU in Colombia</li>',
    '3 consultores + geomático': '3 consultants + geomatician',
    'Gestión de Crisis': 'Crisis Management',
    'Estrategia de Respuesta a Crisis Institucionales': 'Institutional Crisis Response Strategy',
    '"¿Cómo responder con rapidez y coordinación cuando todo pasa al mismo tiempo?"': '"How to respond with speed and coordination when everything happens at once?"',
    'Diseño de protocolos, mapeo de actores, simulaciones de escenarios y planes de contingencia para entidades con responsabilidad en gestión del riesgo, seguridad ciudadana o emergencias sociales. Integramos análisis de datos en tiempo real con marcos de coordinación interinstitucional.': 'Design of protocols, actor mapping, scenario simulations, and contingency plans for entities with responsibility in risk management, citizen security, or social emergencies. We integrate real-time data analysis with inter-institutional coordination frameworks.',
    '<li>Diagnóstico de capacidades institucionales</li>': '<li>Diagnostic of institutional capacities</li>',
    '<li>Mapeo de riesgos y actores críticos</li>': '<li>Mapping of risks and critical actors</li>',
    '<li>Diseño de protocolos de respuesta</li>': '<li>Design of response protocols</li>',
    '<li>Simulacros y ejercicios de mesa</li>': '<li>Simulations and tabletop exercises</li>',
    '<li>Plan de comunicación de crisis</li>': '<li>Crisis communication plan</li>',
    '<li>Manual de protocolos de crisis</li>': '<li>Crisis protocols manual</li>',
    '<li>Mapa de actores y rutas de coordinación</li>': '<li>Map of actors and coordination routes</li>',
    '<li>Informe de vulnerabilidades institucionales</li>': '<li>Report on institutional vulnerabilities</li>',
    '<li>Taller de simulación con equipo directivo</li>': '<li>Simulation workshop with management team</li>',
    '<li>Secretaría de Gobierno Distrital</li>': '<li>District Government Secretariat</li>',
    '<li>Unidad Nacional de Gestión del Riesgo</li>': '<li>National Disaster Risk Management Unit</li>',
    '<li>Gobernaciones con zonas de conflicto</li>': '<li>Governorships with conflict zones</li>',
    '<li>Entidades con mandato de orden público</li>': '<li>Entities with a public order mandate</li>',
    'Formación Institucional': 'Institutional Training',
    'Capacitación en Analítica y Política Basada en Evidencia': 'Training in Analytics and Evidence-Based Policy',
    '"¿Cómo fortalecer las capacidades internas de mi equipo sin contratar más gente?"': '"How do I strengthen my team\'s internal capacities without hiring more people?"',
    'Programas de formación diseñados específicamente para funcionarios públicos, líderes comunitarios y equipos técnicos. Desde talleres introductorios de análisis de datos hasta diplomados en formulación y evaluación de políticas públicas. Metodología activa, casos colombianos y entornos institucionales reales.': 'Training programs designed specifically for public officials, community leaders, and technical teams. From introductory data analysis workshops to diplomas in public policy formulation and evaluation. Active methodology, Colombian cases, and real institutional environments.',
    '<span class="card-col-title">Módulos disponibles</span>': '<span class="card-col-title">Available Modules</span>',
    '<li>Análisis de datos para no especialistas</li>': '<li>Data analysis for non-specialists</li>',
    '<li>Formulación de proyectos de inversión social</li>': '<li>Formulation of social investment projects</li>',
    '<li>Evaluación y monitoreo de programas</li>': '<li>Program evaluation and monitoring</li>',
    '<li>Participación ciudadana y territorio</li>': '<li>Citizen participation and territory</li>',
    '<li>Liderazgo institucional y toma de decisiones</li>': '<li>Institutional leadership and decision making</li>',
    '<span class="card-col-title">Formatos</span>': '<span class="card-col-title">Formats</span>',
    '<li>Taller intensivo (8–16 horas)</li>': '<li>Intensive workshop (8-16 hours)</li>',
    '<li>Diplomado (40–80 horas)</li>': '<li>Diploma (40-80 hours)</li>',
    '<li>Acompañamiento en cascada (ToT)</li>': '<li>Cascade coaching (ToT)</li>',
    '<li>Modalidad virtual, presencial o híbrida</li>': '<li>Virtual, in-person, or hybrid modality</li>',
    '<li>Secretarías y entidades distritales</li>': '<li>District secretariats and entities</li>',
    '<li>Escuelas de gobierno (ESAP)</li>': '<li>Schools of government (ESAP)</li>',
    '<li>ONGs con equipos territoriales</li>': '<li>NGOs with territorial teams</li>',
    '<li>Programas de cooperación técnica</li>': '<li>Technical cooperation programs</li>',
    '1 día – 3 meses': '1 day – 3 months',
    '1–2 facilitadores': '1–2 facilitators',
    'Modalidades de contratación': 'Contracting Modalities',
    'Estructura de Precios': 'Pricing Structure',
    '<span class="price-mode">Modalidad A</span>': '<span class="price-mode">Modality A</span>',
    'Proyecto por Contrato': 'Project by Contract',
    '<li>Alcance y entregables definidos</li>': '<li>Defined scope and deliverables</li>',
    '<li>Pago por hitos (30/40/30)</li>': '<li>Payment by milestones (30/40/30)</li>',
    '<li>Ideal para diagnósticos y evaluaciones</li>': '<li>Ideal for diagnostics and evaluations</li>',
    '<li>Informe final + presentación ejecutiva</li>': '<li>Final report + executive presentation</li>',
    'Recomendado': 'Recommended',
    '<span class="price-mode">Modalidad B</span>': '<span class="price-mode">Modality B</span>',
    'Retainer Mensual': 'Monthly Retainer',
    '<li>Acompañamiento técnico continuo</li>': '<li>Continuous technical support</li>',
    '<li>Disponibilidad garantizada</li>': '<li>Guaranteed availability</li>',
    '<li>Ideal para secretarías en gestión activa</li>': '<li>Ideal for secretariats in active management</li>',
    '<li>Revisiones y alertas periódicas incluidas</li>': '<li>Periodic reviews and alerts included</li>',
    '<span class="price-mode">Modalidad C</span>': '<span class="price-mode">Modality C</span>',
    'Cooperación Internacional': 'International Cooperation',
    '<li>Postulación a convocatorias abiertas</li>': '<li>Application to open calls</li>',
    '<li>Consorcios con universidades o ONGs</li>': '<li>Consortiums with universities or NGOs</li>',
    '<li>Informes en inglés disponibles</li>': '<li>Reports available in English</li>',
    'Mercado objetivo': 'Target Market',
    'Clientes Potenciales': 'Potential Clients',
    'Sector Público Nacional': 'National Public Sector',
    '<li>Departamento Nacional de Planeación (DNP)</li>': '<li>National Planning Department (DNP)</li>',
    '<li>Prosperidad Social</li>': '<li>Social Prosperity</li>',
    '<li>Ministerio del Interior</li>': '<li>Ministry of the Interior</li>',
    '<li>Ministerio de Hacienda</li>': '<li>Ministry of Finance</li>',
    '<li>Unidad Nacional de Gestión del Riesgo</li>': '<li>National Disaster Risk Management Unit</li>',
    '<li>DANE — proyectos de fortalecimiento</li>': '<li>DANE — strengthening projects</li>',
    'Gobierno Distrital y Local': 'District and Local Government',
    '<li>Secretaría Distrital de Gobierno</li>': '<li>District Government Secretariat</li>',
    '<li>Secretaría Distrital de Planeación</li>': '<li>District Planning Secretariat</li>',
    '<li>Fondos de Desarrollo Local</li>': '<li>Local Development Funds</li>',
    '<li>Alcaldías municipales en Colombia</li>': '<li>Municipal Mayoralties in Colombia</li>',
    '<li>Consejos de Planeación Distritales</li>': '<li>District Planning Councils</li>',
    '<li>Personerías y contralorías locales</li>': '<li>Local Personerías and Comptrollers</li>',
    'Cooperación y Tercer Sector': 'Cooperation and Third Sector',
    '<li>CAF — Banco de Desarrollo</li>': '<li>CAF — Development Bank of Latin America</li>',
    '<li>PNUD Colombia</li>': '<li>UNDP Colombia</li>',
    '<li>GIZ — Cooperación Alemana</li>': '<li>GIZ — German Cooperation</li>',
    '<li>USAID Colombia</li>': '<li>USAID Colombia</li>',
    '<li>Banco Interamericano de Desarrollo</li>': '<li>Inter-American Development Bank</li>',
    '<li>Fundación Hanns Seidel</li>': '<li>Hanns Seidel Foundation</li>',
    'Consultoría en Políticas Públicas y Analítica Aplicada': 'Consulting in Public Policy and Applied Analytics',
}

for k, v in translations.items():
    content = content.replace(k, v)

# Add Language Switcher HTML to the header
header_start = content.find('<header>')
if header_start != -1:
    lang_html = """
  <div class="lang-switch-portfolio">
    <a href="portfolio-government-solutions.html" class="lang-btn">ES</a>
    <span class="lang-sep">|</span>
    <a href="portfolio-government-solutions-en.html" class="lang-btn active">EN</a>
  </div>
"""
    content = content.replace('<header>', '<header>' + lang_html)

# Add Language Switcher CSS
css_start = content.find('  header {')
if css_start != -1:
    css_addition = """
  .lang-switch-portfolio {
    position: absolute;
    top: 40px;
    right: 60px;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 700;
    z-index: 10;
  }
  .lang-switch-portfolio a {
    text-decoration: none;
    color: rgba(255,255,255,0.6);
  }
  .lang-switch-portfolio a.active {
    color: var(--paper);
  }
  .lang-switch-portfolio a:hover {
    color: var(--paper);
  }
  .lang-switch-portfolio .lang-sep {
    margin: 0 8px;
    color: rgba(255,255,255,0.3);
  }
"""
    content = content.replace('  header {', css_addition + '  header {')

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)
