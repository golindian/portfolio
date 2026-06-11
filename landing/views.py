import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

logger = logging.getLogger(__name__)

def index(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']

        asunto = f'Nuevo mensaje desde el portfolio: {nombre}'
        cuerpo = (
            f'Nombre: {nombre}\n'
            f'Email: {email}\n\n'
            f'Mensaje:\n{mensaje}'
        )

        try:
            mensaje_email = EmailMessage(
                asunto,
                cuerpo,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                reply_to=[email],
            )
            mensaje_email.send(fail_silently=False)
            messages.success(request, '¡Gracias! Tu mensaje fue enviado correctamente.')
        except Exception as e:
            logger.exception('Error al enviar email de contacto: %s', e)
            messages.error(
                request,
                'No se pudo enviar el mensaje. Verifica en Render: EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS y DEFAULT_FROM_EMAIL.'
            )

        return redirect('landing:index')

    context = {
        'form': form,
        'perfil': {
            'nombre': 'Gaspar Irrazabal',
            'titulo': 'Técnico Programador · Full Stack Developer',
            'resumen': (
                'Técnico Programador con enfoque multidisciplinario orientado a desarrollo '
                'full stack. Actualmente profesor de secundaria en "Algoritmo y Programación", '
                '"Entornos Digitales" y "Club de Ciencias". '
                'Técnico Superior en Desarrollo de Software'),
            'email': 'gasparirrazabal@gmail.com',
            'telefono': '+54 3544 464992',
            'ubicacion': 'Córdoba, Argentina',
        },
        'skills_tecnicas': [
            {'nombre': 'Python', 'nivel': 85, 'icono': 'bi-filetype-py'},
            {'nombre': 'Django', 'nivel': 80, 'icono': 'bi-server'},
            {'nombre': 'HTML5 & CSS3', 'nivel': 90, 'icono': 'bi-filetype-html'},
            {'nombre': 'JavaScript', 'nivel': 75, 'icono': 'bi-filetype-js'},
            {'nombre': 'Bootstrap', 'nivel': 85, 'icono': 'bi-bootstrap'},
            {'nombre': 'SQL / Bases de Datos', 'nivel': 75, 'icono': 'bi-database'},
            {'nombre': 'Git & GitHub', 'nivel': 80, 'icono': 'bi-git'},
            {'nombre': 'Integración de IA', 'nivel': 70, 'icono': 'bi-cpu'},
        ],
        'skills_blandas': [
            'Enseñanza técnica', 'Planificación de proyectos', 'Trabajo en equipo',
            'Resolución de conflictos', 'Comunicación efectiva', 'Aprendizaje continuo',
            'Diseño de apps modernas', 'Supervisión multidisciplinaria',
        ],
        'experiencias': [
            {
                'puesto': 'Profesor de Programación',
                'empresa': 'Educación Secundaria',
                'fechas': 'Actualidad',
                'descripcion': (
                    'Docente en las materias "Algoritmo y Programación", "Entornos Digitales" '
                    'y "Club de Ciencias". Formación de estudiantes en fundamentos de software.'
                ),
            },
            {
                'puesto': 'Técnico Gestión de Recursos Integrales',
                'empresa': 'El Indio',
                'fechas': 'Junio 2008 - Actualidad',
                'descripcion': (
                    'Diseño de estrategias para proyectos fabriles y comerciales. Elaboración de '
                    'informes técnicos, refrigeración industrial y soluciones integrales.'
                ),
            },
            {
                'puesto': 'Mantenimiento de Tragamonedas',
                'empresa': 'Casino Mina Clavero',
                'fechas': 'Experiencia previa',
                'descripcion': (
                    'Diagnóstico y reparación de máquinas IGT, BALLY y ARISTOCRAT. '
                    'Configuración de puertos, routers y placas de comunicación.'
                ),
            },
        ],
        'educacion': [
            {
                'titulo': 'Técnico Superior en Desarrollo de Software',
                'institucion': 'Universidad Provincial de Córdoba',
                'fechas': '2023 - 2026',
            },
            {
                'titulo': 'Técnico Programador',
                'institucion': 'Instituto Superior Carlos María Carena',
                'fechas': '2023 - 2024',
            },
            {
                'titulo': 'Operador Office Full',
                'institucion': 'Instituto IAC',
                'fechas': '2001 - 2002',
            },
        ],
        'idiomas': [
            {'idioma': 'Español', 'nivel': 'Nativo'},
            {'idioma': 'Inglés', 'nivel': 'Intermedio (B1)'},
        ],
          'proyectos': [
            {
                'slug': 'evoswarm-ai',
                'nombre': 'EvoSwarm AI',
                'subtitulo': 'Enjambre Evolutivo de Modelos LLM Locales',
                'periodo': '2025 — En desarrollo',
                'rol': 'Arquitecto & Full Stack Developer',
                'thumb_gradient': 'linear-gradient(135deg, #0ea5e9 0%, #10b981 100%)',
                'tags_cortos': ['IA', 'FastAPI', 'LLM', 'RAG'],
                'descripcion_breve': (
                    'Sistema autónomo de IA que orquesta múltiples LLMs locales en hardware '
                    'limitado (GPU 8GB VRAM). Los modelos colaboran, se auto-evalúan y mejoran '
                    'mediante ciclos evolutivos controlados con memoria persistente por usuario.'
                ),
                'problema': (
                    'Ejecutar múltiples LLMs grandes en hardware doméstico sin depender de APIs '
                    'en la nube, manteniendo calidad, privacidad y capacidad de adaptación.'
                ),
                'caracteristicas': [
                    {'icono': 'bi-diagram-3', 'titulo': 'Orquestación multi-modelo', 'desc': 'Planner, Executor, Critic y Memory Manager coordinan 5 LLMs especializados.'},
                    {'icono': 'bi-arrow-repeat', 'titulo': 'Ciclo evolutivo controlado', 'desc': 'Datasets sintéticos + entrenamiento LoRA semanal con benchmarks fijos.'},
                    {'icono': 'bi-search', 'titulo': 'RAG híbrido avanzado', 'desc': 'Búsqueda semántica + keyword con re-ranking y caché por usuario.'},
                    {'icono': 'bi-cpu', 'titulo': 'Gestión dinámica de VRAM', 'desc': 'Carga/descarga bajo demanda con cuantización 4-bit GGUF.'},
                    {'icono': 'bi-bar-chart', 'titulo': 'Observabilidad completa', 'desc': 'Dashboard de latencia, uso de recursos y calidad de respuestas.'},
                ],
                'tecnologias': [
                    {'nombre': 'FastAPI', 'icono': 'bi-lightning-charge'},
                    {'nombre': 'Ollama', 'icono': 'bi-box'},
                    {'nombre': 'ChromaDB', 'icono': 'bi-database'},
                    {'nombre': 'PostgreSQL', 'icono': 'bi-hdd-stack'},
                    {'nombre': 'Llama 3 / Gemma / Qwen', 'icono': 'bi-robot'},
                    {'nombre': 'LoRA / PEFT', 'icono': 'bi-sliders'},
                    {'nombre': 'Docker', 'icono': 'bi-boxes'},
                    {'nombre': 'Kubernetes', 'icono': 'bi-hdd-network'},
                ],
                'demo_url': 'https://evo-ai-frontend-dti6.onrender.com/',
                'repo_url': '#',
                'aporte': [
                    'Diseño de la arquitectura modular (Orquestador + 5 modelos especializados).',
                    'Implementación del pipeline RAG (chunking semántico, embeddings, retriever híbrido).',
                    'Módulo de routing inteligente según complejidad de tarea y costo computacional.',
                    'Scheduler de recursos GPU con carga/descarga dinámica de modelos.',
                    'Pipeline automatizado de entrenamiento LoRA con versionado y rollback.',
                    'Dockerización y orquestación con Docker Compose (fase 1) y Kubernetes (fase 2).',
                ],
                'resultados': [
                    {'metrica': '8GB', 'label': 'VRAM máxima utilizada (GPU RTX 4060)'},
                    {'metrica': '5', 'label': 'Modelos LLM coordinados simultáneamente'},
                    {'metrica': '100%', 'label': 'Procesamiento local, sin dependencia cloud'},
                    {'metrica': '4-bit', 'label': 'Cuantización GGUF para optimización'},
                ],
                'aprendizajes': (
                    'Comprobé que la inteligencia de un sistema de IA depende más de la orquestación '
                    'que del tamaño de los modelos. La modularidad (Planner / Executor / Critic) y la '
                    'evaluación continua son clave para evitar drift y garantizar mejora sostenida.'
                ),
                'video_filename': 'Evoswarm.mp4',
            },

            {
                'slug': 'evo-ai',
                'nombre': 'EVO-AI',
                'subtitulo': 'Gateway SaaS gestionado para EvoSwarm',
                'periodo': '2025 — En desarrollo',
                'rol': 'Full Stack Developer · Backend & DevOps',
                'thumb_gradient': 'linear-gradient(135deg, #6366f1 0%, #14b8a6 100%)',
                'tags_cortos': ['Django', 'FastAPI', 'JWT', 'SaaS'],
                'descripcion_breve': (
                    'Puerta de acceso gestionada al sistema EvoSwarm. Plataforma SaaS que permite '
                    'consumir EvoSwarm de forma segura mediante autenticación JWT, API keys, '
                    'historial paginado, contextos persistentes y un dashboard administrativo '
                    'con KPIs en tiempo real.'
                ),
                'problema': (
                    'EvoSwarm necesitaba una interfaz centralizada, segura y administrable para '
                    'su consumo en producción. No contaba con autenticación robusta, gestión de '
                    'usuarios, historial ni capacidad de integraciones server-to-server.'
                ),
                'caracteristicas': [
                    {'icono': 'bi-shield-lock', 'titulo': 'Auth JWT + API Keys', 'desc': 'Registro, login, refresh tokens y API keys con hashing SHA-256, rotación y rate-limiting.'},
                    {'icono': 'bi-chat-square-dots', 'titulo': 'Panel de consultas', 'desc': 'Envío de prompts a EvoSwarm con respuestas en Markdown y metadatos (latencia, tokens, modelo).'},
                    {'icono': 'bi-clock-history', 'titulo': 'Historial & export', 'desc': 'Listado paginado con filtros, descarga en Markdown y re-ejecución de consultas previas.'},
                    {'icono': 'bi-bookmark-star', 'titulo': 'Contextos persistentes', 'desc': 'CRUD de contextos por usuario que se pre-penden a los prompts para mantener estado.'},
                    {'icono': 'bi-speedometer2', 'titulo': 'Dashboard de KPIs', 'desc': 'Totales, métricas de 7 días, latencia promedio, tasa de éxito, top users y logs del sistema.'},
                ],
                'tecnologias': [
                    {'nombre': 'Django', 'icono': 'bi-filetype-py'},
                    {'nombre': 'FastAPI', 'icono': 'bi-lightning-charge'},
                    {'nombre': 'PostgreSQL', 'icono': 'bi-database'},
                    {'nombre': 'SQLAlchemy', 'icono': 'bi-link-45deg'},
                    {'nombre': 'Alembic', 'icono': 'bi-arrow-repeat'},
                    {'nombre': 'JWT', 'icono': 'bi-shield-check'},
                    {'nombre': 'Docker Compose', 'icono': 'bi-boxes'},
                    {'nombre': 'Gunicorn + Nginx', 'icono': 'bi-server'},
                    {'nombre': 'httpx async', 'icono': 'bi-arrow-left-right'},
                ],
                'demo_url': 'https://evo-ai-frontend-dti6.onrender.com/',
                'repo_url': '#',
                'aporte': [
                    'Diseño full-stack: frontend con Django (templates, sesiones, i18n) + backend API REST con FastAPI asíncrono.',
                    'Implementación del módulo de seguridad: JWT con refresh tokens, API keys hasheadas con SHA-256 y rate-limiting.',
                    'Desarrollo del cliente asíncrono `evoswarm_client.py` para comunicación HTTP con EvoSwarm.',
                    'Estructura de routers FastAPI: auth, queries, history, store y api_keys con responsabilidades separadas.',
                    'Modelado de BD con SQLAlchemy + migraciones versionadas con Alembic sobre PostgreSQL.',
                    'Dockerización completa y guías de deploy (Docker Compose, systemd/Gunicorn+Nginx, PaaS).',
                    'Sistema de métricas y KPIs administrativos para monitoreo de uso, latencia y tasa de éxito.',
                ],
                'resultados': [
                    {'metrica': 'SaaS', 'label': 'Listo para producción e integraciones'},
                    {'metrica': '5', 'label': 'Routers FastAPI desacoplados'},
                    {'metrica': 'JWT', 'label': 'Auth + refresh + API keys server-to-server'},
                    {'metrica': '100%', 'label': 'Async I/O con httpx + FastAPI'},
                ],
                'aprendizajes': (
                    'Profundicé en arquitecturas híbridas Django + FastAPI, combinando lo mejor de '
                    'ambos mundos: panel admin maduro y API asíncrona de alto rendimiento. Aprendí '
                    'a diseñar sistemas SaaS seguros desde cero — autenticación multi-capa, '
                    'rate-limiting, observabilidad y deploy reproducible con Docker.'
                ),
                'video_filename': 'evosuwarm.mp4',
            },

            {
                'slug': 'agente-ia',
                'nombre': 'Microservicio OCR-COOPER',
                'subtitulo': 'Visión artificial + análisis estratégico con EVOSWARM & ANTHROPIC',
                'periodo': '2025 — Integrado a Sistema de Gestión',
                'rol': 'Desarrollador de IA · Integración & Prompts',
                'thumb_gradient': 'linear-gradient(135deg, #7c3aed 0%, #2563eb 100%)',
                'tags_cortos': ['Claude IA', 'OCR', 'Django', 'Analytics'],
                'descripcion_breve': (
                    'Módulo inteligente que transforma el Sistema de Gestión en una herramienta '
                    'proactiva. Automatiza la carga de remitos mediante visión artificial y genera '
                    'análisis estratégicos cruzando datos de inventario, fabricación, pedidos y '
                    'entregas con modelos Evoswarm & Anthropic.'
                ),
                'problema': (
                    'La carga manual de remitos físicos es tediosa y propensa a errores. Además, '
                    'los módulos operativos generaban datos crudos sin una capa de inteligencia '
                    'que los transforme en decisiones accionables.'
                ),
                'caracteristicas': [
                    {'icono': 'bi-camera', 'titulo': 'OCR con llama3.2-vision & Claude Vision', 'desc': 'Procesa fotos de remitos y extrae proveedor, fecha, productos, cantidades y vencimientos automáticamente.'},
                    {'icono': 'bi-search-heart', 'titulo': 'Match inteligente', 'desc': 'Sugiere coincidencias en la base de datos para proveedores, clientes y productos existentes.'},
                    {'icono': 'bi-clipboard-data', 'titulo': 'Resumen ejecutivo IA', 'desc': 'Genera un snapshot estratégico del estado de la fábrica cruzando métricas de todos los módulos.'},
                    {'icono': 'bi-exclamation-triangle', 'titulo': 'Alertas críticas', 'desc': 'Detección automática de stock faltante, lotes próximos a vencer y demoras en pedidos.'},
                    {'icono': 'bi-lightbulb', 'titulo': 'Sugerencias accionables', 'desc': 'Recomienda qué fabricar, qué comprar y a quién reclamar, detectando patrones ocultos.'},
                ],
                'tecnologias': [
                    {'nombre': 'llama3.2-vision', 'icono': 'bi-image'},
                    {'nombre': 'Evoswarm', 'icono': 'bi-robot'},
                    {'nombre': 'Claude Vision', 'icono': 'bi-eye'},
                    {'nombre': 'Anthropic API', 'icono': 'bi-cloud'},
                    {'nombre': 'Django', 'icono': 'bi-filetype-py'},
                    {'nombre': 'HTMX', 'icono': 'bi-arrow-left-right'},
                    {'nombre': 'PostgreSQL', 'icono': 'bi-database'},
                    {'nombre': 'Prompt Engineering', 'icono': 'bi-chat-square-text'},
                ],
                'demo_url': '#',
                'repo_url': '#',
                'aporte': [
                    'Diseño de la arquitectura del módulo: servicios separados para OCR, analytics y análisis estratégico.',
                    'Desarrollo de `ocr_service.py`: prompts especializados para visión artificial y algoritmo de match con BD.',
                    'Implementación de `analytics_service.py`: motor de recolección de métricas y serialización del estado del sistema.',
                    'Construcción de `analysis_service.py`: orquestador principal de la comunicación con Evoswarm & Claude.',
                    'Ingeniería de prompts contextual con reglas de negocio (estacionalidad, lógica de fábrica).',
                    'Integración con los módulos Inventario, Fabricación, Pedidos y Entregas del sistema principal.',
                ],
                'resultados': [
                    {'metrica': '3', 'label': 'Servicios especializados desacoplados'},
                    {'metrica': '4', 'label': 'Módulos operativos integrados'},
                    {'metrica': 'OCR', 'label': 'Automatización de carga de remitos'},
                    {'metrica': 'IA', 'label': 'Decisiones accionables en tiempo real'},
                ],
                'aprendizajes': (
                    'Aprendí a diseñar arquitecturas de servicios desacoplados para IA, aplicar '
                    'ingeniería de prompts con contexto de negocio, y transformar datos operativos '
                    'crudos en inteligencia accionable. La clave fue estructurar la comunicación '
                    'con el LLM en capas (recolección → contextualización → análisis → acción).'
                ),
                'video_filename': 'OCR-COOPER.mp4',
            },
            {
                'slug': 'milac-cream',
                'nombre': 'Sistema Milac Cream',
                'subtitulo': 'Gestión integral para fábrica de helados',
                'periodo': 'Marzo 2024 — Mayo 2026',
                'rol': 'Full Stack Developer · Equipo de 3',
                'thumb_gradient': 'linear-gradient(135deg, #ec4899 0%, #f59e0b 100%)',
                'tags_cortos': ['Django', 'PostgreSQL', 'HTMX', 'Docker'],
                'descripcion_breve': (
                    'Sistema integral que informatiza los procesos de manufactura, distribución, '
                    'ventas y control de inventario de la fábrica Milac Cream. Integra 12 módulos '
                    'especializados con dashboards en tiempo real, auditoría completa y un agente '
                    'de IA para análisis y recomendaciones.'
                ),
                'problema': (
                    'La fábrica operaba con procesos manuales que generaban faltantes en puntos de '
                    'venta, pérdida de trazabilidad de lotes, y falta de visibilidad sobre los '
                    'niveles óptimos de producción y ventas.'
                ),
                'caracteristicas': [
                    {'icono': 'bi-box-seam', 'titulo': 'Inventario por lote', 'desc': 'Stock con fechas de vencimiento, alertas de seguridad y extracción automática para producción y entregas.'},
                    {'icono': 'bi-journal-text', 'titulo': 'Recetas versionadas', 'desc': 'Versionado de recetas con clonación, ingredientes categorizados y descuento automático de insumos.'},
                    {'icono': 'bi-cart-check', 'titulo': 'Pedidos & entregas', 'desc': 'CRUD completo con sincronización automática de estados entre entregas e inventario.'},
                    {'icono': 'bi-graph-up-arrow', 'titulo': '7 KPIs en tiempo real', 'desc': 'Dashboard de fabricación con gráficos de distribución, tendencias mensuales y tasa de cumplimiento.'},
                    {'icono': 'bi-robot', 'titulo': 'Agente IA integrado', 'desc': 'Módulo con API de Anthropic para análisis inteligente y recomendaciones operativas.'},
                ],
                'tecnologias': [
                    {'nombre': 'Django 4.2', 'icono': 'bi-filetype-py'},
                    {'nombre': 'Python 3.12', 'icono': 'bi-code-slash'},
                    {'nombre': 'PostgreSQL 16', 'icono': 'bi-database'},
                    {'nombre': 'Bootstrap 5', 'icono': 'bi-bootstrap'},
                    {'nombre': 'HTMX', 'icono': 'bi-arrow-left-right'},
                    {'nombre': 'Docker Compose', 'icono': 'bi-boxes'},
                    {'nombre': 'Gunicorn + Nginx', 'icono': 'bi-server'},
                    {'nombre': 'Anthropic API', 'icono': 'bi-robot'},
                    {'nombre': 'django-simple-history', 'icono': 'bi-clock-history'},
                    {'nombre': 'Supervisor / systemd', 'icono': 'bi-gear-wide-connected'},
                ],
                'demo_url': 'https://sistema-milac-cream-demo.onrender.com',
                'repo_url': '#',
                'aporte': [
                    'Diseño de modelos de Inventario con stock por lote, trazabilidad y extracciones automáticas.',
                    'Implementación del módulo Pedidos: CRUD, dashboard con KPIs y creación automática de stock al recibir.',
                    'Desarrollo del módulo Entregas con descuento automático de inventario y sincronización de estados.',
                    'Integración de django-simple-history para auditoría completa sobre modelos críticos.',
                    'Configuración del stack Docker (dev + prod) con PostgreSQL, Gunicorn y Nginx.',
                    'Sistema de notificaciones por email con cola de procesamiento y reintentos.',
                    'Implementación de tests unitarios y de integración para Entregas y Core_Scheduler.',
                ],
                'resultados': [
                    {'metrica': '12', 'label': 'Módulos integrados'},
                    {'metrica': '28+', 'label': 'Tablas relacionales diseñadas'},
                    {'metrica': '7', 'label': 'KPIs de fabricación en tiempo real'},
                    {'metrica': '100%', 'label': 'Automatización stock ↔ ventas'},
                ],
                'aprendizajes': (
                    'Aprendí a diseñar arquitecturas Django modulares escalables, aplicar el '
                    'principio de separación de responsabilidades entre apps, e integrar HTMX '
                    'para lograr UX fluida sin SPA. Trabajar en equipo de 3 desarrolladores me '
                    'enseñó la importancia de convenciones de código, versionado riguroso y '
                    'documentación técnica cruzada.'
                ),
                'video_filename': 'milac-cream.mp4',
            },
        ],
    }
    return render(request, 'index.html', context)