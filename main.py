# app.py
import flet as ft

URL = "https://sites.google.com/view/amr-app?usp=sharing"

def main(page: ft.Page):
    page.title = "الشهرة"
    page.window_width = 1000
    page.window_height = 700
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    web = ft.WebView(src=URL, expand=True)

    page.add(web)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)  # يمكنك تغيير view إذا أردت نافذة سطح مكتب
