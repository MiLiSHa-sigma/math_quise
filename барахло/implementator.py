import dearpygui.dearpygui as dpg

def graphic_version():
    dpg.create_context()
    dpg.create_viewport(width=332, height=342)
    with dpg.font_registry():
        with dpg.font("./ofont.ru_Zeitmax.ttf",20,tag = "ofont"):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    with dpg.window():
        dpg.add_text('Тут будет пример')
        dpg.add_input_float()
        dpg.add_button(label='Здесь будет ответ')
    dpg.bind_font("ofont")
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

graphic_version()