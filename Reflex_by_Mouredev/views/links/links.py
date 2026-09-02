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
            "https://www.linkedin.com/in/antoniomapic/"
        ),
        link_button(
            "GitHub", 
            "Portfolio de mis proyectos", 
            "img/github.svg",
            "https://github.com/erpica"
        ),
        link_button(
            "Vercel", 
            "", 
            "img/linkedin.svg",
            ""
        ),
        link_button(
            "Netlify", 
            "", 
            "img/linkedin.svg",
            ""
        ),


        title("Mis mentores:"),
        link_button(
            "Brais Moure", 
            "Ingeniero de software y divulgador",
            "img/linkedin.svg",
            "https://moure.dev/"
        ),
        link_button(
            "Miguel Ángel Durán", 
            "Ingeniero de Software y Creador de Contenido sobre Programación", 
            "img/linkedin.svg",
            "https://midu.dev/"
        ),
        link_button(
            "Vacante", 
            "", 
            "img/linkedin.svg",
            ""
        ),
        link_button(
            "Vacante", 
            "", 
            "img/linkedin.svg",
            ""
        ),

        title("Contacto:"),
        link_button(
            "Email", 
            styles.EMAIL,
            "img/linkedin.svg",
            f"mailto:{styles.EMAIL}"
        ),


        width="100%"
    )