import flet as ft
import pandas as pd
from sqlalchemy import create_engine
import win32com.client as client
import datetime as dt

outlook = client.Dispatch('Outlook.Application')
emissor = outlook.session.Accounts['luzo.neto@sicoob.com.br']
# emissor = outlook.session.Accounts['5004.performance@sicoob.com.br']
hoje = dt.datetime.now()




def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        print(e.files)
        for x in e.files:
            base = pd.read_excel(x.path)
        print(digitar_email.value)


    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    digitar_email = ft.TextField(label='Digite o E-mail')
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Arquivo",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
                digitar_email,
            ]
        )
    )
#    pd.read_excel(selected_files)

ft.app(target=main)