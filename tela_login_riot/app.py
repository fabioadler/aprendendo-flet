import flet as ft, time

class my_app():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.title = "Login RIOT"
        self.page.window.title_bar_hidden = True
        self.page.window.resizable = True
        self.page.window.left = 20
        self.page.on_resized = self.update()

    def home(self):
        self.stack = ft.Stack(
            expand = True,
            controls=[
                ft.Container(
                    expand = True,
                    content=ft.Row(
                        spacing = 0,
                        controls = [
                            ft.Container(
                                width = (0.25*self.page.window.width),
                                height = (1*self.page.window.height),
                                padding = 0,
                                gradient = ft.LinearGradient(
                                    begin = ft.alignment.top_center,
                                    end = ft.alignment.bottom_center,
                                    colors = ["#09121D","#162437","#152943","#193457"]
                                ),
                                content = ft.Column(
                                    horizontal_alignment = "center",
                                    controls = [
                                        ft.Container(
                                            content = ft.Image(
                                                src = "riot-games-new-logo-qhg.png",
                                                width = (0.7*self.page.window.width),
                                                height = (0.2*self.page.window.height),
                                                fit = ft.ImageFit.COVER
                                            )
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                width = (0.75*self.page.window.width),
                                height = (1*self.page.window.height),
                                padding = 0,
                                content = ft.Image(
                                    src = "background.jpg",
                                    width = (0.75*self.page.window.width),
                                    height = (1*self.page.window.height),
                                    fit = ft.ImageFit.COVER
                                )
                                
                            )
                        ]
                    )
                ),
                ft.Row(
                    width=(1*self.page.window.width),
                    controls=[
                        ft.WindowDragArea(
                            width = (0.9*self.page.window.width),
                            height = 30,
                            content = ft.Container(bgcolor="transparent")
                        ),
                        ft.IconButton(
                            icon = ft.Icons.REMOVE,
                            icon_color = ft.Colors.WHITE,
                            on_click = self.mini
                        ),
                        ft.IconButton(
                            icon = ft.Icons.CLOSE,
                            icon_color = ft.Colors.WHITE,
                            on_click = lambda e: self.page.window.close()
                        )
                    ]
                )
            ]
        )
        self.page.add(self.stack)
        

    def mini(self, e):
        self.page.window.minimized = True
        self.page.update()

    def update(self):
        self.page.clean()
        self.home()
        self.page.padding=0
        self.page.update()
        time.sleep(1)
        self.page.on_resized = self.update()


ft.app(target=my_app,assets_dir="./assets")