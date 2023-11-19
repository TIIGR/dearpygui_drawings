import dearpygui.dearpygui as dpg
from point import Point

dpg.create_context()
dpg.create_viewport(title='Fractals', width=700, height=700)
dpg.setup_dearpygui()

def update():
    
    global Tags
    
    def coch(n):
        if n == 0:
            Tags.append(dpg.generate_uuid())
            dpg.draw_line(P.toTuple(), P.sum(D).toTuple(), color=(255, 0, 0, 255), thickness=1, parent='drawlist', tag=Tags[-1])
        else:
            for angle in [0, 60, -120, 60]:
                D.turn(angle)
                coch(n - 1)
        
    for tags in Tags:
        dpg.delete_item(tags)
    
    level = dpg.get_value("level")
    size = dpg.get_value("size")
    P = Point((500 - size) / 2, 250 + size * (3) ** (1/2) / 6)
    D = Point(size / (3 ** level), 0)
    Tags = []
    
    for i in range(3):
        coch(level)
        D.turn(-120)

with dpg.window(label="Koch's snowflake"):
    
    dpg.add_slider_int(label="Level", min_value=0, max_value=4, default_value=3, tag="level", callback=update)
    dpg.add_slider_float(label="Size", min_value=50, max_value=400, default_value=300, tag="size", callback=update)
    
    with dpg.drawlist(width=500, height=500, tag='drawlist'):
        
        def coch(n):
            if n == 0:
                Tags.append(dpg.generate_uuid())
                dpg.draw_line(P.toTuple(), P.sum(D).toTuple(), color=(255, 0, 0, 255), thickness=1, tag=Tags[-1])
            else:
                for angle in [0, 60, -120, 60]:
                    D.turn(angle)
                    coch(n - 1)
        
        level = dpg.get_value("level")
        size = dpg.get_value("size")
        P = Point((500 - size) / 2, 250 + size * (3) ** (1/2) / 6)
        D = Point(size / (3 ** level), 0)
        Tags = []
        
        for i in range(3):
            coch(level)
            D.turn(-120)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()