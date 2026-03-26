from nicegui import ui
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    client_name = Column(String)
    service = Column(String)
    date = Column(Date)

engine = create_engine('sqlite:///cammseb.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Funciones (Robustas y Eficientes)
def add_appointment(client, service, date_str):
    if not client or not service or not date_str:
        ui.notify('Por favor, complete todos los campos.', type='warning')
        return

    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        app = Appointment(client_name=client, service=service, date=date)
        session.add(app)
        session.commit()
        update_table()
        ui.notify('🌸 Cita agregada exitosamente 🌸', type='positive')
        # Limpiar campos tras agregar
        client_input.value = ''
        service_input.value = ''
        date_input.value = ''
    except ValueError:
        ui.notify('Formato de fecha inválido. Use YYYY-MM-DD', type='negative')

def update_table():
    rows = [{'ID': a.id, 'Cliente': a.client_name, 'Servicio': a.service, 'Fecha': str(a.date)} for a in session.query(Appointment).all()]
    table.rows = rows
    table.update()

# Diagnóstico (Lógica de IA Simplificada)
diagnoses = {
    'seca': 'Hidratar profundamente con cremas y mascarillas.',
    'grasa': 'Limpiar con productos astringentes y seborreguladores.',
    'mixta': 'Balancear con tratamientos combinados y limpieza T.',
    'cabello seco': 'Nutrir intensamente con aceites y mascarillas.',
    'cabello graso': 'Lavar con shampoo específico y evitar aceites.',
    'cabello normal': 'Mantenimiento básico y protección térmica.'
}

def diagnose(skin, hair):
    if not skin and not hair:
        ui.notify('Por favor, seleccione al menos un tipo de piel o cabello.', type='warning')
        return
    
    rec = 'Recomendación 🌿: '
    if skin:
        rec += diagnoses.get(skin, 'Consulta personalizada para piel.')
    if hair:
        rec += ' ' + diagnoses.get('cabello ' + hair, 'Consulta personalizada para cabello.')
    ui.notify(rec, type='info', position='center')

# Calculadora de Costos (Robusta)
def calculate(cost, time, margin):
    try:
        # Usamos 0 si el campo está vacío para evitar errores
        rate_hr = 50  
        cost_float = float(cost or 0)
        time_float = float(time or 0)
        margin_float = float(margin or 0)

        # Fórmula: (Costo Insumos + Costo Tiempo) * Margen Ganancia
        price = (cost_float + (time_float * rate_hr)) * (1 + (margin_float / 100))
        ui.notify(f'💰 Precio final sugerido: ${price:.2f}', type='positive', position='center')
    except ValueError:
        ui.notify('Ingrese valores numéricos válidos.', type='negative')

# --- UI con DISEÑO MEJORADO y FORMULARIO CENTRADO ---
ui.page_title('cammseb - Gestión de Estética')

# CSS Personalizado (Colores de Spa)
ui.add_css('''
    body {
        background: linear-gradient(135deg, #e1bee7 0%, #f3e5f5 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .spa-header {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 30px;
        border-radius: 0 0 20px 20px;
        text-align: center;
        color: #4a148c;
    }
    .main-tab-panel {
        background: transparent !important;
        display: flex;
        justify-content: center;
        padding-top: 20px;
    }
    .spa-card-form {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        padding: 40px;
        max-width: 500px; /* Ancho máximo para mantenerlo estilizado */
        width: 100%;
    }
    .spa-button {
        background: linear-gradient(45deg, #ab47bc, #ba68c8);
        color: white !important;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .spa-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(171, 71, 188, 0.4);
    }
    .ui-tabs .q-tab {
        color: #4a148c;
    }
    .ui-tabs .q-tab--active {
        color: #ab47bc;
    }
''')

# Encabezado (Ya estaba centrado)
with ui.column().classes('spa-header'):
    ui.label('🌸 cammseb 🌸').classes('text-h2 font-bold')
    ui.label('Centro de Estética y Cosmetología').classes('text-h5 text-purple-700')

# Sistema de Pestañas
with ui.tabs().classes('w-full justify-center') as tabs:
    ui.tab('Citas', icon='event_note')
    ui.tab('Diagnóstico', icon='spa')
    ui.tab('Calculadora', icon='calculate')
    ui.tab('Visualización', icon='table_chart')

# Paneles de las pestañas
with ui.tab_panels(tabs, value='Citas').classes('main-tab-panel w-full'):
    
    # --- Pestaña: CITAS (¡ESTA ES LA QUE HEMOS CENTRADO!) ---
    with ui.tab_panel('Citas').classes('items-center'):
        # ui.row() y classes('justify-center') hacen la magia
        with ui.row().classes('justify-center w-full'):
            with ui.card().classes('spa-card-form'):
                ui.label('Gestión de Citas').classes('text-h4 text-center text-purple-900 q-mb-lg font-bold')
                
                # Campos de entrada
                client_input = ui.input('Nombre de la Cliente').classes('w-full q-mb-md')
                service_input = ui.input('Servicio').classes('w-full q-mb-md')
                date_input = ui.input('Fecha (YYYY-MM-DD)', placeholder='AAAA-MM-DD').classes('w-full q-mb-lg')
                
                # Botón de acción
                ui.button('AGREGAR CITA', on_click=lambda: add_appointment(client_input.value, service_input.value, date_input.value)).classes('spa-button w-full q-py-sm text-subtitle1')

    # --- Pestaña: DIAGNÓSTICO (También centrada) ---
    with ui.tab_panel('Diagnóstico').classes('items-center'):
        with ui.row().classes('justify-center w-full'):
            with ui.card().classes('spa-card-form'):
                ui.label('Asistente de Diagnóstico').classes('text-h4 text-center text-purple-900 q-mb-lg font-bold')
                
                skin_select = ui.select(['seca', 'grasa', 'mixta'], label='Tipo de Piel').classes('w-full q-mb-md')
                hair_select = ui.select(['seco', 'graso', 'normal'], label='Estado del Cabello').classes('w-full q-mb-lg')
                
                ui.button('OBTENER RECOMENDACIÓN', on_click=lambda: diagnose(skin_select.value, hair_select.value)).classes('spa-button w-full q-py-sm text-subtitle1')

    # --- Pestaña: CALCULADORA (También centrada) ---
    with ui.tab_panel('Calculadora').classes('items-center'):
        with ui.row().classes('justify-center w-full'):
            with ui.card().classes('spa-card-form'):
                ui.label('Calculadora de Precios').classes('text-h4 text-center text-purple-900 q-mb-lg font-bold')
                
                cost_input = ui.number('Costo Materiales ($)', format='%.2f').classes('w-full q-mb-md')
                time_input = ui.number('Tiempo (horas)', format='%.1f').classes('w-full q-mb-md')
                margin_input = ui.number('Margen de Ganancia (%)', format='%.0f').classes('w-full q-mb-lg')
                
                ui.button('CALCULAR PRECIO FINAL', on_click=lambda: calculate(cost_input.value, time_input.value, margin_input.value)).classes('spa-button w-full q-py-sm text-subtitle1')

    # --- Pestaña: VISUALIZACIÓN ---
    with ui.tab_panel('Visualización'):
        ui.label('Registros de Citas').classes('text-h4 text-center text-purple-900 q-mb-lg font-bold')
        
        with ui.card().classes('spa-card w-full q-pa-lg'):
            table = ui.table(
                columns=[
                    {'name': 'ID', 'label': 'ID', 'field': 'ID', 'align': 'left'},
                    {'name': 'Cliente', 'label': 'Cliente', 'field': 'Cliente', 'align': 'left'},
                    {'name': 'Servicio', 'label': 'Servicio', 'field': 'Servicio', 'align': 'left'},
                    {'name': 'Fecha', 'label': 'Fecha', 'field': 'Fecha', 'align': 'left'}
                ],
                rows=[]
            ).classes('w-full')
            # Cargar datos iniciales
            update_table()

# Ejecutar la aplicación
ui.run()