import os

file_path = "/Users/andrezconz/Library/Mobile Documents/com~apple~CloudDocs/Antigravity/orion/orion/portfolio-government-solutions.html"
out_path = "/Users/andrezconz/Library/Mobile Documents/com~apple~CloudDocs/Antigravity/orion/orion/portfolio-government-solutions-en.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Translations map
translations = {
    '<html lang="es">': '<html lang="en">',
    'Soluciones Gubernamentales — Portafolio de Servicios': 'Government Solutions — Service Portfolio',
    'ORION INTELLIGENCE · PORTAFOLIO DE SERVICIOS · 2026': 'ORION INTELLIGENCE · SERVICE PORTFOLIO · 2026',
    'Las decisiones públicas de hoy<br>exigen <span>Decision Intelligence</span>': 'Today\'s public decisions<br>demand <span>Decision Intelligence</span>',
    'Orion Intelligence transforma datos complejos en decisiones estratégicas mediante analítica avanzada, inteligencia artificial y diseño de políticas públicas basadas en evidencia. Acompañamos al sector público y organizaciones de desarrollo en la transición hacia la autonomía técnica real.': 'Orion Intelligence transforms complex data into strategic decisions through advanced analytics, artificial intelligence, and evidence-based public policy design. We accompany the public sector and development organizations in the transition towards real technical autonomy.',
    'Especialidad': 'Specialty',
    'Políticas Públicas & Datos': 'Public Policy & Data',
    'Mercado': 'Market',
    'Colombia · Cooperación Internacional': 'Colombia · International Cooperation',
    'Modalidad': 'Modality',
    'Proyecto · Retainer · Formación': 'Project · Retainer · Training',
    'Primera edad – La Tierra': 'First Age – The Earth',
    'Comunidad y pertenencia como valor central.': 'Community and belonging as a central value.',
    'Segunda edad – El Trabajo': 'Second Age – Labor',
    'Orden institucional y expansión del Estado.': 'Institutional order and State expansion.',
    'Tercera edad – El Capital': 'Third Age – Capital',
    'Crecimiento económico como medida del éxito.': 'Economic growth as a measure of success.',
    'Cuarta edad – Las Decisiones': 'Fourth Age – Decisions',
    'Decision Intelligence, evidencia y bienestar institucional.': 'Decision Intelligence, evidence, and institutional well-being.',
    'Fichas técnicas': 'Technical Data Sheets',
    'Líneas de Servicio': 'Service Lines',
    
    # L-01
    'Inteligencia Política': 'Political Intelligence',
    '"¿Cómo anticipar dinámicas de poder, incentivos electorales y riesgos de gobernabilidad?"': '"How to anticipate power dynamics, electoral incentives, and governance risks?"',
    'Análisis avanzado de comportamiento electoral, estabilidad de coaliciones, riesgo político y opinión pública. Ayudamos a gobiernos y campañas a mapear el territorio político, interpretar incentivos de actores locales e identificar señales de polarización y cambios en el electorado para tomar decisiones estratégicas de comunicación y posicionamiento basadas en evidencia.': 'Advanced analysis of electoral behavior, coalition stability, political risk, and public opinion. We help governments and campaigns map the political territory, interpret the incentives of local actors, and identify signals of polarization and shifts in the electorate to make evidence-based strategic communication and positioning decisions.',
    '<span class="card-col-title">Actividades</span>': '<span class="card-col-title">Activities</span>',
    '<li>Análisis de comportamiento electoral a nivel de mesa y puesto de votación</li>': '<li>Analysis of electoral behavior at the polling station and table level</li>',
    '<li>Modelación de estabilidad de partidos y coaliciones legislativas</li>': '<li>Modeling the stability of parties and legislative coalitions</li>',
    '<li>Monitoreo cuali-cuantitativo de polarización y opinión pública</li>': '<li>Quali-quantitative monitoring of polarization and public opinion</li>',
    '<li>Evaluación continua de riesgo político y gobernabilidad territorial</li>': '<li>Continuous assessment of political risk and territorial governance</li>',
    '<li>Mapeo de incentivos y relaciones de actores locales clave</li>': '<li>Mapping incentives and relationships of key local actors</li>',
    '<span class="card-col-title">Productos</span>': '<span class="card-col-title">Deliverables</span>',
    '<li>Tableros dinámicos de análisis electoral histórico y en tiempo real</li>': '<li>Dynamic dashboards of historical and real-time electoral analysis</li>',
    '<li>Mapeo interactivo de actores e influencia territorial</li>': '<li>Interactive mapping of actors and territorial influence</li>',
    '<li>Reportes periódicos (Briefings) de riesgo de gobernabilidad</li>': '<li>Periodic reports (briefings) on governance risk</li>',
    '<li>Modelos de simulación de escenarios de coaliciones políticas</li>': '<li>Simulation models of political coalition scenarios</li>',
    '<span class="card-col-title">Clientes típicos</span>': '<span class="card-col-title">Typical Clients</span>',
    '<li>Campañas electorales nacionales y territoriales</li>': '<li>National and territorial electoral campaigns</li>',
    '<li>Secretarías de Gobierno y oficinas de asuntos políticos</li>': '<li>Government Secretariats and political affairs offices</li>',
    '<li>Think tanks y firmas de consultoría estratégica nacional</li>': '<li>Think tanks and national strategic consulting firms</li>',
    '<li>Gremios sectoriales y ONGs interesadas en coyuntura</li>': '<li>Sectoral associations and NGOs interested in current affairs</li>',
    '<strong>Duración:</strong>': '<strong>Duration:</strong>',
    'semanas': 'weeks',
    '<strong>Equipo:</strong>': '<strong>Team:</strong>',
    'consultores analistas': 'analyst consultants',
    
    # L-02
    'Inteligencia de Políticas Públicas': 'Public Policy Intelligence',
    '"¿Cómo diseñar y evaluar intervenciones públicas con impacto medible en el territorio?"': '"How to design and evaluate public interventions with measurable impact in the territory?"',
    'Diagnóstico socioeconómico granular, diseño de políticas basadas en evidencia y evaluación rigurosa de impacto. Combinamos métodos econométricos aplicados con una lectura territorial profunda para identificar brechas de desarrollo, focalizar subsidios y demostrar de manera cuantitativa la efectividad de los programas públicos.': 'Granular socioeconomic diagnostic, evidence-based policy design, and rigorous impact evaluation. We combine applied econometric methods with a deep territorial reading to identify development gaps, target subsidies, and quantitatively demonstrate the effectiveness of public programs.',
    '<li>Evaluación de impacto cuasiexperimental de programas sociales</li>': '<li>Quasi-experimental impact evaluation of social programs</li>',
    '<li>Diagnósticos granulares de vulnerabilidad socioeconómica</li>': '<li>Granular diagnostics of socioeconomic vulnerability</li>',
    '<li>Definición de KPIs y estructuración de marcos lógicos</li>': '<li>Definition of KPIs and structuring of logical frameworks</li>',
    '<li>Análisis de brechas de capacidad institucional y territorio</li>': '<li>Analysis of institutional capacity gaps and territory</li>',
    '<li>Levantamiento y limpieza de datos en territorio (surveys)</li>': '<li>Collection and cleaning of data in the field (surveys)</li>',
    '<li>Informe de evaluación de impacto para organismos de control</li>': '<li>Impact evaluation report for oversight bodies</li>',
    '<li>Índice digital de priorización y focalización territorial</li>': '<li>Digital index of territorial prioritization and targeting</li>',
    '<li>Fichas metodológicas y matrices de indicadores de impacto</li>': '<li>Methodological sheets and matrices of impact indicators</li>',
    '<li>Policy Briefs ejecutivos con recomendaciones de política</li>': '<li>Executive Policy Briefs with policy recommendations</li>',
    '<li>Secretarías de Planeación, Desarrollo Social y Hacienda</li>': '<li>Secretariats of Planning, Social Development, and Finance</li>',
    '<li>Agencias de planeación del nivel nacional (DNP) y ministerios</li>': '<li>National planning agencies (DNP) and ministries</li>',
    '<li>Organismos multilaterales (BID, Banco Mundial, PNUD)</li>': '<li>Multilateral organizations (IDB, World Bank, UNDP)</li>',
    '<li>Fundaciones y ONGs ejecutoras de programas sociales</li>': '<li>Foundations and NGOs executing social programs</li>',
    'consultores especializados': 'specialized consultants',
    
    # L-03
    'Inteligencia Artificial Gubernamental': 'Government AI',
    '"¿Cómo automatizar procesos, analizar normativas y gestionar información masiva en el sector público?"': '"How to automate processes, analyze regulations, and manage massive information in the public sector?"',
    'Implementación práctica de Inteligencia Artificial para el fortalecimiento de la gestión gubernamental. Desarrollamos asistentes de IA normativa, herramientas de IA documental, asistentes inteligentes para planes de desarrollo y sistemas de automatización de reportes que multiplican la capacidad técnica y operativa de los equipos del Estado.': 'Practical implementation of Artificial Intelligence to strengthen government management. We develop regulatory AI assistants, document AI tools, smart assistants for development plans, and report automation systems that multiply the technical and operational capacity of State teams.',
    '<li>Fine-tuning de Modelos de Lenguaje (LLMs) con datos normativos</li>': '<li>Fine-tuning of Language Models (LLMs) with regulatory data</li>',
    '<li>Implementación de sistemas RAG para búsqueda de gacetas jurídicas</li>': '<li>Implementation of RAG systems for legal gazette search</li>',
    '<li>Extracción automatizada de información en documentos públicos</li>': '<li>Automated extraction of information from public documents</li>',
    '<li>Formulación de asistentes de IA para proyectos de inversión</li>': '<li>Formulation of AI assistants for investment projects</li>',
    '<li>Automatización de flujos de trabajo e informes de control</li>': '<li>Automation of workflows and control reports</li>',
    '<li>Aplicativo Web (Chatbot) de consulta y análisis normativo</li>': '<li>Web Application (Chatbot) for consultation and regulatory analysis</li>',
    '<li>Pipeline automatizado de procesamiento y extracción documental</li>': '<li>Automated pipeline for processing and document extraction</li>',
    '<li>Dashboards interactivos con alertas de seguimiento automáticas</li>': '<li>Interactive dashboards with automatic tracking alerts</li>',
    '<li>Guía de gobernanza de datos y principios de IA ética</li>': '<li>Data governance guide and ethical AI principles</li>',
    '<li>Oficinas jurídicas y secretarías generales del sector público</li>': '<li>Legal offices and general secretariats of the public sector</li>',
    '<li>Secretarías de Planeación municipal, distrital o departamental</li>': '<li>Municipal, district, or departmental Planning Secretariats</li>',
    '<li>Unidades de contratación del Estado y control interno</li>': '<li>State contracting and internal control units</li>',
    '<li>Entidades descentralizadas con alto volumen de peticiones y trámites</li>': '<li>Decentralized entities with a high volume of requests and procedures</li>',
    '1 consultor senior + 1 ingeniero de datos/IA': '1 senior consultant + 1 data/AI engineer',
    
    # L-04
    'Inteligencia de Decisiones': 'Decision Intelligence',
    '"¿Cómo tomar decisiones óptimas bajo altos niveles de incertidumbre y riesgo?"': '"How to make optimal decisions under high levels of uncertainty and risk?"',
    'Diseñamos modelos matemáticos y simulaciones para anticipar los efectos de decisiones críticas, optimizar la asignación de recursos limitados, analizar riesgos financieros/operativos y priorizar intervenciones territoriales. Transformamos modelos analíticos descriptivos en rutas claras de recomendación y acción.': 'We design mathematical models and simulations to anticipate the effects of critical decisions, optimize the allocation of limited resources, analyze financial/operational risks, and prioritize territorial interventions. We transform descriptive analytical models into clear recommendation and action paths.',
    '<li>Modelación de escenarios de choques socioeconómicos y financieros</li>': '<li>Modeling scenarios of socioeconomic and financial shocks</li>',
    '<li>Modelos de optimización matemática para distribución presupuestal</li>': '<li>Mathematical optimization models for budget distribution</li>',
    '<li>Evaluación y cuantificación de riesgos de proyectos estratégicos</li>': '<li>Evaluation and quantification of risks of strategic projects</li>',
    '<li>Análisis de sensibilidad y prospectiva de largo plazo</li>': '<li>Sensitivity analysis and long-term foresight</li>',
    '<li>Talleres ejecutivos de simulación de crisis y juegos de rol</li>': '<li>Executive workshops on crisis simulation and role-playing</li>',
    '<li>Decision Briefs orientados a gabinetes y juntas directivas</li>': '<li>Decision Briefs oriented to cabinets and boards of directors</li>',
    '<li>Simuladores interactivos de impacto presupuestal y social</li>': '<li>Interactive budget and social impact simulators</li>',
    '<li>Matriz analítica de riesgos con modelación de probabilidad</li>': '<li>Analytical risk matrix with probability modeling</li>',
    '<li>Ruta crítica de recomendaciones priorizadas con restricciones</li>': '<li>Critical path of prioritized recommendations with constraints</li>',
    '<li>Alcaldes, Gobernadores y equipos directivos centrales</li>': '<li>Mayors, Governors, and central management teams</li>',
    '<li>Directores de empresas de servicios públicos y fondos de inversión</li>': '<li>Directors of public utility companies and investment funds</li>',
    '<li>Comités de respuesta rápida ante emergencias y shocks</li>': '<li>Rapid response committees for emergencies and shocks</li>',
    '<li>Gerencias de megaproyectos de infraestructura y APP</li>': '<li>Management of infrastructure megaprojects and PPPs</li>',
    '2 consultores de decisión': '2 decision consultants',
    
    # Pricing & Clients
    'Modalidades de contratación': 'Contracting Modalities',
    'Estructura de Precios': 'Pricing Structure',
    'Modalidad A': 'Modality A',
    'Proyecto por Contrato': 'Project by Contract',
    '<li>Alcance y entregables definidos</li>': '<li>Defined scope and deliverables</li>',
    '<li>Pago por hitos (30/40/30)</li>': '<li>Payment by milestones (30/40/30)</li>',
    '<li>Ideal para diagnósticos y evaluaciones</li>': '<li>Ideal for diagnostics and evaluations</li>',
    '<li>Informe final + presentación ejecutiva</li>': '<li>Final report + executive presentation</li>',
    'Modalidad B': 'Modality B',
    'Retainer Mensual': 'Monthly Retainer',
    '<li>Acompañamiento técnico continuo</li>': '<li>Continuous technical support</li>',
    '<li>Disponibilidad garantizada</li>': '<li>Guaranteed availability</li>',
    '<li>Ideal para secretarías en gestión activa</li>': '<li>Ideal for secretariats in active management</li>',
    '<li>Revisiones y alertas periódicas incluidas</li>': '<li>Periodic reviews and alerts included</li>',
    'Modalidad C': 'Modality C',
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
    'Soluciones Gubernamentales · Consultoría en Políticas Públicas y Analítica Aplicada': 'Government Solutions · Consulting in Public Policy and Applied Analytics',
}

for k, v in translations.items():
    content = content.replace(k, v)

# Fix switcher active states
content = content.replace(
    '<a href="portfolio-government-solutions.html" class="lang-btn active">ES</a>',
    '<a href="portfolio-government-solutions.html" class="lang-btn">ES</a>'
)
content = content.replace(
    '<a href="portfolio-government-solutions-en.html" class="lang-btn">EN</a>',
    '<a href="portfolio-government-solutions-en.html" class="lang-btn active">EN</a>'
)

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)

print("English portfolio compiled successfully!")
