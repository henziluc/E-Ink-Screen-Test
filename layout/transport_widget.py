from .fonts import font_small, font_normal, font_medium, font_large, fill_main


def display_schedule_complet(draw, station_name_1, df_1, station_name_2, df_2, x_start, y_start):
    y = y_start
    spacing_small = font_small.size + 10
    spacing_normal = font_medium.size + 10
    spacing_large = font_large.size + 10
    
    draw.text((x_start, y), "Next Trains", font=font_large, fill=fill_main)
    y += spacing_large
    draw, y = display_schedule(draw, station_name_1, df_1, x_start, y, spacing_small)
    y += 10
    draw, y = display_schedule(draw, station_name_2, df_2, x_start , y, spacing_small)
    
    
    return draw



def display_schedule(draw, station_name, df, x_start, y_start, spacing):
    y = y_start
    
    #Size of the squares around the route short name
    sq_width = 31
    sq_height = 24
    draw.text((x_start, y),"Station " + station_name,font=font_normal,fill=fill_main)
    
    y += spacing
    
    for _, row in df.iterrows():
        route = str(row["route_short_name"])

        # Choose background and text color depending on route number
        if route == "3":
            route_bg = "green"
            route_text = "white"

        elif route == "S11":
            route_bg = "black"
            route_text = "white"

        elif route == "S26":
            route_bg = "black"
            route_text = "white"

        else:
            route_bg = "gray"
            route_text = "white"
        #display route short name with a colored square around it
        draw.rounded_rectangle((x_start, y, x_start + sq_width, y + sq_height),radius=1,fill=route_bg)
        draw.text((x_start + sq_width/2 , y + sq_height/2), route,font=font_small,fill=route_text, anchor="mm")
        #display trip headsign with out leading Winterthur
        headsign = row["trip_headsign"].replace("Winterthur, ", "")
        draw.text((x_start + 35, y),headsign ,font=font_small,fill=fill_main) 
        #display delays in rounded minutes in a red font
        delay = round(int(row['delay'])/60)
        if delay > 1:
            draw.text((x_start + 150, y),f"+{delay}min",font=font_small,fill="red") 
        #display departure time    
        draw.text((x_start + 200, y),row['departure_time'][:-3],font=font_small,fill=fill_main)
      
        y += spacing
        
    return draw, y