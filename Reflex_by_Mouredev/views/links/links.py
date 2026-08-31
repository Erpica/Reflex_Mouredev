import reflex as rx
from Reflex_by_Mouredev.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Linkedin", "https://www.linkedin.com/in/antoniomapic/"),
        link_button("GitHub", "https://github.com/erpica"),
        link_button("Vercel", ""),
        link_button("Netlify", ""),

        width="100%"
    )