import flet as ft
from fletcarousel import BasicAnimatedHorizontalCarousel as bc, HintLine, AutoCycle

def my_app(page:ft.Page):
    page.window.width=400
    page.window.height=600
    page.window.resizable=False
    page.padding = 0
    page.title = "Carrosel teste 01"
    page.theme_mode = "dark"
    page.horizontal_alignment=ft.alignment.center

    carrosel =  bc(
        page=page,
        auto_cycle=AutoCycle(duration=4),
        expand=True,
        padding=10,
        hint_lines=HintLine(
            active_color=ft.Colors.BLUE_100,
            inactive_color=ft.Colors.GREY_100,
            alignment="center",
            max_list_size=40
        ),
        items=[
            ft.Container(
                alignment=ft.alignment.center,
                width=(0.85*page.window.width),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.alignment.center,
                    height=(0.3*page.window.height),
                    spacing=20,
                    controls=[
                        ft.Text("Acompanhe as novidades", size=20),
                        ft.Button(
                            text="Conferir!",
                            icon=ft.Icons.FORWARD,
                            icon_color=ft.Colors.WHITE,
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE_900,
                            width=(0.4*page.window.width),
                        )
                    ]
                )
            ),
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                content=ft.Image(
                    width=(0.85*page.window.width),
                    height=(0.3*page.window.height),
                    src="1.jpg",
                    fit=ft.ImageFit.FILL,
                    border_radius=10
                ) 
            ),
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                content=ft.Image(
                    width=(0.85*page.window.width),
                    height=(0.3*page.window.height),
                    src="2.jpg",
                    fit=ft.ImageFit.FILL,
                    border_radius=10
                ) 
            )
        ]
    )

    page.add(carrosel)
    page.update()

ft.app(target=my_app, assets_dir="./assets")