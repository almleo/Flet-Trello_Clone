import flet

from flet import(
    Page,
    PopupMenuItem,
    AppBar,
    Icon,
    icons,
    Text,
    colors,
    Container,
    PopupMenuButton,
    margin
)

class TrelloApp(AppBar):
    def __init__(self):
        super().__init__()
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(), 
            PopupMenuItem(text="Settings")
        ]
        self.leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED)
        self.leading_width=100
        self.title=Text("Trolli", size=32, text_align="start")
        self.center_title=False
        self.toolbar_height=75
        self.bgcolor=colors.LIGHT_BLUE_ACCENT_700
        self.actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50,right=25)
                )
            ]

if __name__ == "__main__":
    def main(page: Page):
        page.Title = "Flet Trello Clone"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = TrelloApp()
        page.update()
        
        page.add(app)
        
    flet.app(main, view=flet.WEB_BROWSER)