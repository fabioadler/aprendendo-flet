from flet import *


def my_app(page:Page):
    page.title = "Testando os alertas"
    alerta = AlertDialog(
        modal=True,
        title=Text("Teste de alerta"),
        content=Text("Nosso alerta bem sucedido!"),
        actions=[
            TextButton("Deu certo",on_click=lambda e:page.close(alerta)),
            TextButton("Não deu certo",on_click=lambda e:(page.close(alerta),page.open(alerta2)))
        ]
    )

    alerta2 = AlertDialog(
        modal=True,
        title=Text("Hum..."),
        content=Text("Como não deu certo? E como você chegou aqui?"),
        actions=[
            TextButton("Adimito que deu certo",on_click=lambda e:page.close(alerta2)),
        ]
    )

    def alert(e):
        page.open(alerta)
        page.update

    page.add(
        Row([
            Text("Vamos testar o nosso alerta"),
            ElevatedButton("Clique aqui", on_click=alert)
        ])
    )
    page.update()

app(target=my_app)