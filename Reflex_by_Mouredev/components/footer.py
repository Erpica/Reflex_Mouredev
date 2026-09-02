import reflex as rx
import datetime
from Reflex_by_Mouredev.components.link_button import link_button
from Reflex_by_Mouredev.styles.styles import Size

def footer():
    return rx.hstack(
        rx.image(
            src="/img/barco.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de un barco en el océano."
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