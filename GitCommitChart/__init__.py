from typing import List
from PIL import Image, ImageDraw
from PIL.Image import Image as ImageType

def _hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[j:j+2], 16) for j in (0, 2, 4))

def create_git_commit_chart(
    data:List[int],
    tile_end_color="#56d364",
    tile_start_color="#033a16",
    background_color="#0d1117",
    tile_background_color="#151b23",
    tile_border_color="#ffffff1f",
    border_radius=5,
    tile_size=40,
    rows_per_column=7,
    inner_padding=15,
    outer_vertical_padding=75,
    outer_horizontal_padding=50,
) -> ImageType:
    # Calculate the number of columns needed
    size = len(data)
    num_columns = (size + rows_per_column - 1) // rows_per_column

    total_horizontal_gap = inner_padding * (num_columns - 1)
    total_width = num_columns * tile_size + total_horizontal_gap + 2 * outer_horizontal_padding
    total_vertical_gap = inner_padding * (rows_per_column - 1)
    total_height = rows_per_column * tile_size + total_vertical_gap + 2 * outer_vertical_padding

    # Create a new image with the specified background color
    image = Image.new("RGBA", (total_width, total_height), background_color)
    tile_layer = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 0))
    tile_draw = ImageDraw.Draw(tile_layer)

    # Draw only the background tiles
    for i in range(size):
        row = i % rows_per_column
        column = i // rows_per_column
        x = outer_horizontal_padding + column * (tile_size + inner_padding)
        y = outer_vertical_padding + row * (tile_size + inner_padding)

        tile_draw.rounded_rectangle(
            [x, y, x + tile_size, y + tile_size],
            fill=tile_background_color,
            outline=tile_border_color,
            width=1,
            radius=border_radius
        )
    # Blend with main image
    image = Image.alpha_composite(image, tile_layer)

    # Normalize the data to fit within the range of 0 to 1
    max_value = max(data) if data else 1 
    normalized_data = [min(value / max_value, 1) for value in data]

    # New layer for the actual data
    data_layer = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 0))
    data_draw = ImageDraw.Draw(data_layer)
    for i, value in enumerate(normalized_data):
        row = i % rows_per_column
        column = i // rows_per_column
        x = outer_horizontal_padding + column * (tile_size + inner_padding)
        y = outer_vertical_padding + row * (tile_size + inner_padding)

        start_rgb = _hex_to_rgb(tile_start_color)
        end_rgb = _hex_to_rgb(tile_end_color)
        interp_rgb = tuple(
            int(start + (end - start) * value)
            for start, end in zip(start_rgb, end_rgb)
        )
        alpha = int(value * (255)) 
        color = (*interp_rgb, alpha)

        data_draw.rounded_rectangle(
            [x, y, x + tile_size, y + tile_size],
            fill=color,
            outline=tile_border_color,
            width=1,
            radius=border_radius
        )

    # Blend the data layer onto the main image
    image = Image.alpha_composite(image, data_layer)
    
    return image
