import reflex as rx

config = rx.Config(
    app_name="Reflex_by_Mouredev",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)