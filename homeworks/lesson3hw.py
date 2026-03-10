from datetime import datetime
import flet as ft 

def main(page: ft.Page):
    page.title = 'My first app!'
    page.theme_mode = ft.ThemeMode.DARK

    greeting_history = []
    history_text = ft.Text(value='Greetings: ')

    text_hello = ft.Text(value='Hello')

    def on_click_func(_): 
    
        name = name_input.value

        if name:
            current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

            text_hello.value = f"{current_time} - Hello, {name}!"
            text_hello.color = None

            greeting_history.append(f"{name} - {current_time}")
            
            name_input.value = ""
            history_text.value = "Greetings:\n" + "\n".join(greeting_history)

        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Please enter a valid name!'
        page.update()

    name_input = ft.TextField(label='Enter name', expand=True, on_submit=on_click_func)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.PINK_400, icon_color=ft.Colors.PINK_200, on_click=on_click_func)

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

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, icon_color=ft.Colors.PINK_100, on_click=edit_theme)
    delete_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.PINK, on_click=delete_history)

    main_objects = ft.Row([name_input, elevated_button, delete_button, theme_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(text_hello, main_objects, history_text)



ft.app(main)