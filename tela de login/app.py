import flet as ft

def App(page:ft.Page):

    page.title="testando"
    page.scroll="always"
    page.bgcolor=ft.Colors.WHITE
    linha1 = ft.Row(wrap=True,expand=True,spacing=2)
    page.add(linha1)
    for c in range(20):
        linha1.controls.append(
            ft.Container(
                ft.Text(value=f"ITEM {c}",size=20,text_align=ft.TextAlign.CENTER),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.GREEN_400,
                border=ft.border.all(2,ft.Colors.GREEN_800),
                border_radius=ft.border_radius.all(9)
            )
        )
    page.update()
    
ft.app(target=App,view=ft.FLET_APP)