# print('Hello world')

import flet as ft 

def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.DARK

    greeting_history = []
    history_text = ft.Text(value='История приветствий: ')

    text_hello = ft.Text(value='Hello')

    def on_click_func(_): 
        #print(name_input.value)
        name = name_input.value

        if name:
            # text_hello.value = 'Hello ' + name_input.value 
            text_hello.value = f'Hello {name}'
            text_hello.color = None

            greeting_history.append(name)
            
            name_input.value = None
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите корректное имя!'

        page.update()

    name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_click_func)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)

    # text_button = ft.TextButton(text='send', icon=ft.Icons.SEND, icon_color=ft.Colors.GREEN)
    # icon_button = ft.IconButton(icon=ft.Icons.SEND, icon_color=ft.Colors.RED)
    def delete_history(_):
        greeting_history.clear()
        history_text.value = "Greetings:"
        page.update()

    def edit_theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)
    delete_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED, on_click=delete_history)

    main_objects = ft.Row([name_input, elevated_button, delete_button, theme_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(text_hello, main_objects, history_text)



ft.app(main)
#ft.app(main, view=ft.AppView.WEB_BROWSER)git push -u origin main