import flet as ft

positions = [1, 2, 4, 8, 16, 32, 64, 128]

def main(page: ft.Page):
    input = ft.Ref[ft.TextField]()
    output = ft.Ref[ft.Text]()
    history = []

    def handleClear(_):
        history.clear()
        input.current.label = "Input"
        input.current.value = ""
        input.current.disabled = False
        input.current.focus()
        page.update()

    def handleCalculate(_):
        history.append(
            ft.Container(content = ft.Row(controls=[
                ft.Text(input.current.value)
            ])
        ))
        input.current.value = ""
        input.current.focus()
        page.update()

    def handleChange(event):
        output.current.value = event.control.value
        page.update()

    class CustomButton(ft.ElevatedButton):
        def __init__(self, text, icon, on_click):
            super().__init__()
            self.bgcolor = ft.colors.GREEN_500
            self.color = ft.colors.WHITE
            self.text = text
            self.icon = icon
            self.on_click = on_click

    button_send = CustomButton("Convert", ft.icons.CALCULATE, handleCalculate)
    button_clear = CustomButton("Clear", ft.icons.CLEAR, handleClear)

    buttons = [ button_send, button_clear, ]

    def makeSquare(number: int):
        return ft.Container(content = ft.Column(controls=[
            ft.Row([ft.Text(str(number))],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Checkbox()],
                   alignment=ft.MainAxisAlignment.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, width=40 ))


    def makeSquares():
        squares = []

        for position in positions:
            squares.append(makeSquare(position))

        return squares

    page.add(
        ft.Text(ref=output, text_align = ft.TextAlign.CENTER, width = page.width),
        #ft.Container(ref=tasks_container, content = ft.Column(controls=history)),
        ft.TextField(
            ref=input,
            label="",
            autofocus=True,
            autocorrect = False,
            enable_suggestions = False,
            text_align = ft.TextAlign.CENTER,
            input_filter = ft.NumbersOnlyInputFilter(),
            on_submit=handleCalculate,
            on_change=handleChange), # pyright: ignore reportArgumentType
        ft.Container(content = ft.Row(controls=buttons)), # pyright: ignore reportArgumentType

        ft.Container(content = ft.Row(controls=makeSquares(),
          alignment=ft.MainAxisAlignment.CENTER, width=page.width),
                                      margin = ft.Margin(0, 40, 0, 0))
    )

ft.app(main)
