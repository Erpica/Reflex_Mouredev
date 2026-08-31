import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        # Cambiamos 'name' por 'fallback'
        rx.avatar(fallback="Pic", size="3", radius="full", color_scheme="orange"),
        rx.text("@erpica.es"), 
        rx.text("Hola Soy Antonio Martín. Me dedico a dar soporte a empresas en cuanto a automatización, organización de equipos, puesta en marcha de equipos y dispositivos... Actualmente me dedico a crear aplicaciones web con Python, Reflex y PostgreSQL."),
        align="center"
    ), 
    
