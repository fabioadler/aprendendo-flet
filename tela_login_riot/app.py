import flet as ft

class my_app():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.title = "Login RIOT"
        self.page.window.title_bar_hidden = True
        self.page.window.resizable = False
        self.page.window.width = 1200
        self.page.window.height = 600
        self.page.window.left = 20
        self.page.padding = 0

        self.stack = ft.Stack(
            expand = True,
            controls=[
                ft.Container(
                    expand = True,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                width = 300,
                                height = 600,
                                padding=0,
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                    colors=["#09121D","#162437","#152943","#193457"]
                                ),
                                content=ft.Column(
                                    horizontal_alignment = "center",
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(
                                                src = "riot-games-new-logo-qhg.png",
                                                width = 200,
                                                height = 200,
                                                fit=ft.ImageFit.COVER
                                            )
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=0,
                                content=ft.Image(
                                    src = "background.jpg",
                                    width = 900,
                                    height = 600,
                                    fit=ft.ImageFit.COVER
                                )
                                
                            )
                        ]
                    )
                ),
                ft.Row(
                    controls=[
                        ft.WindowDragArea(
                            width=self.page.window.width - 120,
                            height=30,
                            content=ft.Container(bgcolor="transparent")
                        ),
                        ft.IconButton(
                            icon=ft.Icons.REMOVE,
                            icon_color=ft.Colors.WHITE,
                            on_click=self.mini
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.WHITE,
                            on_click=lambda e: self.page.window.close()
                        )
                    ]
                )
            ]
        )
        self.page.add(self.stack)
        self.page.update()

    def mini(self, e):
        self.page.window.minimized = True
        self.page.update()

ft.app(target=my_app,assets_dir="./assets")