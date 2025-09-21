import streamlit as st
from PIL import Image
from st_copy_to_clipboard import st_copy_to_clipboard


def image_to_ascii(image: Image.Image, new_width: int = 100) -> str:
    """
    Convert a PIL Image to an ASCII art string.

    Args:
        image (PIL.Image.Image): Input image.
        new_width (int): Maximum output width in characters.

    Returns:
        str: ASCII representation of the image.
    """

    # ASCII characters from dark to light
    ASCII_CHARS = "@0#Oo*+~=-. "

    # Resize image to maintain aspect ratio (height adjusted for char proportions)
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 compensates font aspect ratio
    image = image.resize((new_width, new_height))

    # Convert to grayscale
    image = image.convert("L")

    # Map pixels to ASCII chars
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels)

    # Break into lines
    ascii_art = "\n".join(
        ascii_str[i:(i + new_width)] for i in range(0, len(ascii_str), new_width)
    )

    return ascii_art


st.title("Image -> ASCII Art")

# Upload image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image, use_column_width=True)

    # Convert to ASCII
    ascii_art = image_to_ascii(image, new_width=80)
#     ascii_art = """
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxcddddddddvxxxxxxJddddddddddddxxxxxxxdddddddddddpxxxxxxxxxxddddddddddqxxxxxxxxxxx.
# .xxxxxxxxxxxxxxdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddZxxxxxx.
# .xxxxxxxxxxxxddddddd.U@@@q.0dddddddq.d@@@@@@@@[-ddddddd.;@@@@@@@8.]dddddddddd'@@@@@@@`(dddddddxxxx.
# .xxxxxxxxxxxddddd.@@@@@@@@@..ddd.@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@.ddd.@@@@@@@@@@@@@@@@.dddddxxx.
# .xxxxxxxxxpdddd.^@@@@@@@@@@....@@@@@@@@@@@@@@@@@@;@@@@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@.wdddxxx.
# .xxxxxxxxddddd.@@@@@@@@@@@>...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@..dddxxx.
# .xxxxxxxddddp.@@@@@@@@@@@/...@@@@@@@@@@........@@@@@@@@@@...@@@@@@@@@`@@@@@@@@@B..@@@@@@@@@..dddxxx.
# .xxxxxxdddd}.@@@@@@@@@@@\.."@@@@@@@@@@@@@@@@..@@@@@@@@@p..z@@@@@@@@.^@@@@@@@@@"..M@@@@@@@@@.ddddxxx.
# .xxxxxdddd`.@@@@@@@@@@@....@@@@@@@@@@@@@@@@@.@@@@@@@@@}@@@@@@@@@@@..@@@@@@@@@...}@@@@@@@@@..ddddxxx.
# .xxxxddddI.@@@@@@@@@@@....@@@@@@@@@@@@@@@@@.@@@@@@@@@\.@@@@@@@@@@@.@@@@@@@@@"..l@@@@@@@@@..ddddxxxx.
# .xxxYdddY.@@@@@@@@@@@....@@@@@@@@@@@@@@@m..W@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@Z../@@@@@@@@@(.ddddxxxxx.
# .xxxdddd.`@@@@@@@@@@@@@?.@@@@@@@@@@@@@@@@..@@@@@@@@@...@@@@@@@@@@.@@@@@@@@@..@@@@@@@@@@l.ddddxxxxxx.
# .xxxddd..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@.]ddddxxxxxxx.
# .xxxddd..@@@@@@@@@@@@@@@0@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@b...@@@@@@@@@@@@@@@@@@@.dddddxxxxxxxx.
# .xxxdddd.|@@@@@@@@@@@@@C..@@@@@@@@@@@@@@@.].@@@@@@@@@@@@@@@@.ddddp.@@@@@@@@@@@@@@@&;dddddXxxxxxxxxx.
# .xxxxdddddd.\@@@@@@!,ddddddd.c@@@@@@&.0dddddddt.@@@@@@@]`dddddddddddd.f@@@@@@@`fdddddddOxxxxxxxxxxx.
# .xxxxxJdddddddddddddddddddddddddddddddddddddddddddddddddddddddnxdddddddddddddddddddddxxxxxxxxxxxxxx.
# .xxxxxxxxxxdddddddddOxxxxxxnddddddddddUxxxxxxx0ddddddddddxxxxxxxxxxxxddddddddddmxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# .xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
# ....................................................................................................
# """


    st.subheader("ASCII Image")
    st.text("Copy to clipboard...")
    st_copy_to_clipboard(ascii_art)
    st.markdown(f"```{ascii_art}```")
