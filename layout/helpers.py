def draw_grid(draw, spacing, height, width):
    i = 1
    #horizontal lines
    while i * spacing < height:
        draw.line((0, i * spacing, width, i * spacing),fill="black",width=1)
        i += 1
    
    i = 1  
    #vertical lines
    while i * spacing < width:
            draw.line((i * spacing, 0, i * spacing, height),fill="black",width=1)
            i += 1
    
    return draw