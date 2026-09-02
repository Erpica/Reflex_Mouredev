import reflex as rx
import Reflex_by_Mouredev.styles.styles as styles

def link_icon(url: str, src: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=src,
            width="24px",
            height="24px",
            alt="Icono",
        ),
        href=url,
        is_external=True, 
    )
        