from enum import Enum
import reflex as rx
from .fonts import Font as Font
from .colors import Color, TextColor

# Constants
MAX_WIDTH="600px"

# Sizes
class Size(Enum):
    ZERO="0em"
    SMALL="0.5em"
    MEDIUM = "0.8em"
    DEFAULT="1em"
    LARGE = "1.5em"
    BIG="2em"
    VERY_BIG="4em"

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    rx.button:{
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width = "100%",
    font_family = Font.TITLE.value,
    padding_top = Size.LARGE.value,
    color = TextColor.DARK.value
)

button_tittle_style = dict(
    font_family = Font.TITLE.value,
    font_size = Size.LARGE.value,
    color = Color.DARK.value,
    font_weight="bold"
)

button_body_style = dict(
    font_family = Font.DEFAULT.value,
    font_size = Size.DEFAULT.value,
    color = Color.PRIMARY.value,
    font_weight="bold"
)

# Contact
EMAIL = "antoniomartinpica@gmail.com"