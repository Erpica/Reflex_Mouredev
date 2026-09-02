import reflex as rx
from Reflex_by_Mouredev.components.link_button import link_button
from Reflex_by_Mouredev.components.title import title
import Reflex_by_Mouredev.styles.styles as styles


def links() -> rx.Component:
    return rx.vstack(
        title("Mi portfolio como programador:"),
        link_button(
            "Linkedin", 
            "CV extendido online", 
            "img/linkedin.svg",
            "https://www.linkedin.com/in/antoniomapic/",
            "Botón de Linkedin"
        ),
        link_button(
            "GitHub", 
            "Portfolio de mis proyectos", 
            "img/github.svg",
            "https://github.com/erpica",
            "Botón de GitHub"
        ),
        link_button(
            "Vercel", 
            "", 
            "img/linkedin.svg",
            "",
            "Botón de Vercel"
        ),
        link_button(
            "Netlify", 
            "", 
            "img/linkedin.svg",
            "",
            "Botón de Netlify"
        ),


        title("Mis mentores:"),
        link_button(
            "Brais Moure", 
            "Ingeniero de software y divulgador",
            "img/linkedin.svg",
            "https://moure.dev/",
            "Botón de Brais Moure"
        ),
        link_button(
            "Miguel Ángel Durán", 
            "Ingeniero de Software y Creador de Contenido sobre Programación", 
            "img/linkedin.svg",
            "https://midu.dev/",
            "Botón de Miguel Ángel Durán"
        ),
        link_button(
            "Vacante", 
            "", 
            "img/linkedin.svg",
            "",
            "Botón de vacante"
        ),
        link_button(
            "Vacante", 
            "", 
            "img/linkedin.svg",
            "",
            "Botón de vacante"
        ),

        title("Contacto:"),
        link_button(
            "Email", 
            styles.EMAIL,
            "img/linkedin.svg",
            f"mailto:{styles.EMAIL}",
            "Botón de contacto"
        ),


        width="100%"
    )