import reflex as rx
from reflex.config import SitemapPlugin
from reflex_components_radix.plugin import RadixThemesPlugin
from reflex.plugins import TailwindV4Plugin

config = rx.Config(
    app_name="Reflex_by_Mouredev",
    plugins=[
        SitemapPlugin(trailing_slash='preserve'),
        TailwindV4Plugin(config={'plugins': ['@tailwindcss/typography@0.5.20']}),
        RadixThemesPlugin(),
    ],
    # ... resto de tu configuración
)