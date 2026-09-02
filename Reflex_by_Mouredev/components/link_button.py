import reflex as rx
import Reflex_by_Mouredev.styles.styles as styles
from Reflex_by_Mouredev.styles.colors import Color as Color

def link_button (tittle: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image, 
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(tittle, style=styles.button_tittle_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="1",
                    align_items="start",
                ),
                align="center"
            ),
            bg_color=Color.LIGHT.value,
        ),
    href=url,
    is_external=True, 
    width="100%"
    )