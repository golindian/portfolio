from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Aquí podrías enviar email con send_mail
        messages.success(request, '¡Gracias! Tu mensaje fue enviado correctamente.')
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
                'demo_url': '#',
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
            },
            {
                'nombre': 'Gestión de Recursos Integrales',
                'tecnologias': ['Django', 'JavaScript', 'Bootstrap'],
                'descripcion': 'Plataforma administrativa para la gestión de proyectos fabriles y comerciales.',
                'imagen': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800',
                'link': '#'
            },
            {
                'nombre': 'Analizador de Remitos con IA',
                'tecnologias': ['Python', 'Azure AI', 'HTMX'],
                'descripcion': 'Herramienta de OCR y análisis automatizado de documentos para logística industrial.',
                'imagen': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=800',
                'link': '#'
            },
        ],
    }
    return render(request, 'landing/index.html', context)