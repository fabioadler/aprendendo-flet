import flet as ft

class meu_app():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.title="meu app de tarefas"
        self.page.theme_mode="dark"
        self.page.bgcolor="#fff",
        self.page.vertical_alignment=ft.MainAxisAlignment.CENTER
        self.page.padding=0
        self.page.on_resized=self.resize
        self.input_tarefa = ft.TextField(
            width=self.page.width*0.8,
            label="Crie uma tarefa"
        )
        self.icon_button=ft.IconButton(
            width=self.page.width*0.1,
            icon=ft.Icons.ADD,
            on_click=self.add_tarefa
        )
        self.conteudo_tarefas = [
            ft.Container(
                margin=ft.Margin(left=10,top=50,right=10,bottom=0),
                alignment=ft.alignment.center,
                content=ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=self.input_tarefa
                        ),
                        ft.Container(
                            content=self.icon_button
                        )
                    ]
                )
            )    
        ]

        self.conteudo_app = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=10,
            controls=self.conteudo_tarefas
        )
        self.page.add(
            self.conteudo_app
        )
        self.page.update()
    
    def resize(self,e):
        self.input_tarefa.width=self.page.width*0.8
        self.icon_button.width=self.page.width*0.1
        self.page.update()

    def add_tarefa(self,e):
        class tarefa(ft.Container):
            def __init__(self,page,text_tarefa):
                super().__init__()
                self.text_tarefa=text_tarefa
                self.checkbox = ft.Checkbox()
                self.page=page
                self.expand=True
                self.padding=20
                self.content=ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.checkbox,
                        ft.Text(self.text_tarefa),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            on_click=self.del_tarefa
                        )
                    ]
                )
            def del_tarefa(self,e):
                self.visible=False
                self.page.update()

        self.conteudo_tarefas.append(tarefa(self.page,self.input_tarefa.value))
        self.conteudo_app.controls=self.conteudo_tarefas
        self.page.controls=[self.conteudo_app]
        self.input_tarefa.value=""
        self.page.update()

ft.app(target=meu_app)