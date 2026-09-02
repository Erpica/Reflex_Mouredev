import reflex as rx
from Reflex_by_Mouredev.components.link_icon import link_icon
from Reflex_by_Mouredev.styles.styles import Size as Size
from Reflex_by_Mouredev.styles.styles import Color as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                size="6", 
                radius="full", 
                color=Color.DARK,
                bg_color=Color.LIGHT,
                src="/img/foto_programar.png",
                padding="2px",
                border="4px"
            ),
            rx.vstack(
                rx.heading(
                    "Antonio Martín", 
                    size="6",
                    
                ), 

                
                rx.hstack(
                    rx.text("\"ErPica\""),
                    rx.link(
                        rx.avatar(fallback="in", size="1", radius="full", color_scheme="blue"),
                        href="https://www.linkedin.com/in/antoniomapic/",
                        is_external=True
                    ),

                    link_icon("https://github.com/erpica", src="/icons/github_ico.svg"),
                ),

                align="center",
                spacing="0"
            ),

            
        ),

        

        rx.text("Hola Soy Antonio Martín. Me dedico a dar soporte a empresas en cuanto a automatización, organización de equipos, " \
        "puesta en marcha de equipos y dispositivos... Actualmente me dedico a crear aplicaciones web con Python, Reflex y PostgreSQL."),
        spacing="5",
        
    ), 
    
