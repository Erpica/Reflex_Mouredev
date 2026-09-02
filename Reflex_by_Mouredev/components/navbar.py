import reflex as rx
from Reflex_by_Mouredev.styles.styles import Size as Size
from Reflex_by_Mouredev.styles.colors import Color as Color
import Reflex_by_Mouredev.styles.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text("Portfolio", color=Color.DARK.value),
            rx.text(" by Reflex", color=Color.PRIMARY.value),
            style=styles.navbar_title_style
        ),


        position="sticky",
        bg=Color.LIGHT.value,
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        z_index="999",
        border_radius="4px",
        justify="center",
        align="center",
        top = "0"
)