import flet
from flet import Container, Draggable, DragTarget, Page, Row, Text, alignment, colors

def main(page: Page):
    page.title = "Drag and Drop example"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.data)
        # update text inside draggable control
        src.content.content.value = "0"
        # update text inside drag target control
        e.control.content.content.value = "1"
        page.update()

    page.add(
        Row(
            [
                Draggable(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN_200,
                        border_radius=5,
                        content=Text("1", size=20),
                        alignment=alignment.center,
                    ),
                ),
                Container(width=100),
                DragTarget(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_200,
                        border_radius=5,
                        content=Text("0", size=20),
                        alignment=alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )

flet.app(target=main,view=flet.WEB_BROWSER)