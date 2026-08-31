import reflex as rx
import datetime

def footer():
    return rx.hstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© {datetime.date.today().year} Antonio Martín. ",
            href="https://github.com/erpica"
        ),
        rx.text("Diseño y desarrollo web.")
    )