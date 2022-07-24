import flet
from flet import Column, ElevatedButton, Page, Row, Text, TextField, UserControl

class Counter(UserControl):
    def __init__(self, initial_count):
        super().__init__()
        self.counter = initial_count

    def build(self):
        text = Text(str(self.counter))
        def add_click(e):
            self.counter += 1
            text.value = str(self.counter)
            self.update()

        return Row([text, ElevatedButton("Add", on_click=add_click)])

# then use the control
def main(page):
    page.add(
        Counter(100),
        Counter(200))

flet.app(target=main)