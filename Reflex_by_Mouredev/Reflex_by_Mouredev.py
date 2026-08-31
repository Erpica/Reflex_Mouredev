import reflex as rx
from .pages.index import index
import Reflex_by_Mouredev.styles.styles as styles

app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
