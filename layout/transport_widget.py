def display_schedule(draw, station_name, df, x_start, y_start, font, fill):
    y = y_start
    spacing = 30
    #Size of the squares around the route short name
    sq_width = 31
    sq_height = 25
    draw.text((x_start, y),"Station " + station_name,font=font,fill=fill)
    
    y += 20
    
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
        draw.text((x_start + sq_width/2 , y + sq_height/2), route,font=font,fill=route_text, anchor="mm")
        #display trip headsign with out leading Winterthur
        headsign = row["trip_headsign"].replace("Winterthur, ", "")
        draw.text((x_start + 35, y),headsign ,font=font,fill=fill) 
        #display delays in rounded minutes in a red font
        delay = round(int(row['delay'])/60)
        if delay > 1:
            draw.text((x_start + 150, y),f"+{delay}min",font=font,fill="red") 
        #display departure time    
        draw.text((x_start + 200, y),row['departure_time'][:-3],font=font,fill=fill)
      
        y += spacing
    return draw