import flet as ft


class MyButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text

def main(page: ft.Page):

    # say hello input
    def btn_click(e):
      if not txt_name.value:
        txt_name.error_text = "Please enter your name"
        page.update()
      else:
        name = txt_name.value
        page.clean()
        page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")
    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

    # click me button
    btn = ft.ElevatedButton("Click me")
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.add(btn)

    def checkbox_changed(e):
        output_text.value = f"You have learned how to ski: {todo_check.value}"
        page.update()
    output_text = ft.Text()
    todo_check = ft.Checkbox(label="Todo: Learn how to ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

    page.add(MyButton(text="Custom Button"), MyButton(text="Another custom button"))

ft.app(main)
