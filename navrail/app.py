from flet import *


def my_app(page:Page):
    rail = NavigationRail(
        min_width=100,
        min_extended_width=400,
        label_type=NavigationRailLabelType.ALL,
        leading=FloatingActionButton(icon=Icons.MENU,text="Menu"),
        selected_index=0,
        destinations=[
            NavigationRailDestination(
                icon=Icons.HOME_OUTLINED,
                selected_icon=Icons.HOME,
                label="Home"
            ),
            NavigationRailDestination(
                icon=Icons.ADD_LOCATION_OUTLINED,
                selected_icon=Icons.ADD_LOCATION,
                label="Adicionar Local"
            ),
            NavigationRailDestination(
                icon=Icons.LOCATION_ON_OUTLINED,
                selected_icon=Icons.LOCATION_PIN,
                label="Local"
            ),
            NavigationRailDestination(
                icon=Icons.SETTINGS_OUTLINED,
                selected_icon=Icons.SETTINGS,
                label="Consfigurações"
            )
        ],
        on_change= lambda e: print(f"Página selecionada: {e.control.selected_index}")
    )
    page.add(
        Row(controls=[
            rail,
            VerticalDivider(width=1)
        ],expand=True)
    )
    page.update()

app(target=my_app)