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
                '"Entornos Digitales" y "Club de Ciencias". Estudiante avanzado del Técnico '
                'Superior en Desarrollo de Software en la Universidad Provincial de Córdoba.'
            ),
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
                'nombre': 'EvoSwarm AI',
                'tecnologias': ['Python', 'Django', 'PostgreSQL', 'Docker'],
                'descripcion': 'Sistema de entrenamiento evolutivo de modelos de lenguaje con gestión automática de VRAM.',
                'imagen': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800',
                'link': '#'
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