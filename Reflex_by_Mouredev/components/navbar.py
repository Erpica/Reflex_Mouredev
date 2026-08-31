import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Hola Reflex",
            color="white" # Eliminado height="40px" para alineación vertical limpia
        ),
        position="sticky",
        bg="#00a2d3",
        padding_x="100px",
        padding_y="8px",
        z_index="999",
        border_radius="4px",
        justify="center",
        align="center"
)