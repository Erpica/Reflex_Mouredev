import reflex as rx
import datetime
from Reflex_by_Mouredev.components.link_button import link_button
from Reflex_by_Mouredev.styles.styles import Size

def footer():
    return rx.hstack(
        rx.image(
            src="/img/barco.png",
            height=Size.VERY_BIG.value
        ),
        rx.link(
            f"© {datetime.date.today().year} Antonio Martín Pica. ",
            href="https://github.com/erpica"
        ),
        rx.text("Diseño y desarrollo web."),
        align="center",
        justify="center",   # <-- Centra horizontalmente el contenido
        width="100%",       # <-- Ocupa todo el ancho disponible
    )