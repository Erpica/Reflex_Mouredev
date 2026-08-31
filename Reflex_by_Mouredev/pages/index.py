import reflex as rx
from Reflex_by_Mouredev.components.navbar import navbar
from Reflex_by_Mouredev.components.footer import footer
from Reflex_by_Mouredev.views.header.header import header
from Reflex_by_Mouredev.views.links.links import links
import Reflex_by_Mouredev.styles.styles as styles
from Reflex_by_Mouredev.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(), 
        rx.center(
            rx.vstack(
                header(),
                links(),
                width="100%",
                max_width=styles.MAX_WIDTH,
                align="center",
                margin_y=Size.BIG.value
            ),
            width="100%"
        ),
        footer()
    )
