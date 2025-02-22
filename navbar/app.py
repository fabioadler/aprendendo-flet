from flet import *

def my_app(page:Page):
    page.title = "v1 nav_bar"
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationBarDestination(icon=Icons.HOME, label="Home"),
            NavigationBarDestination(icon=Icons.ADD_LOCATION, label="Locais"),
            NavigationBarDestination(icon=Icons.MENU, label="Configuração"),
        ]
    )
    page.update()

app(target=my_app)