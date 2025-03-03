import flet as ft
from fletcarousel import BasicAnimatedHorizontalCarousel as bc, HintLine, AutoCycle

def my_app(page:ft.Page):
    page.window.width = 720
    page.window.height = 1024
    page.padding = 0
    page.title = "Carrosel teste 01"
    page.update()

ft.app(target=my_app, assets_dir="./assets")