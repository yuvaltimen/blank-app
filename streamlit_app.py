import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import os
from PIL import Image, ImageDraw, ImageFont

FONT_LOCAL_PATH = "fonts/Anonymous/Anonymous.ttf"

def ensure_font(font_path: str = FONT_LOCAL_PATH) -> str:
    """Ensure the monospaced font file exists locally; if not, download it."""
    os.makedirs(os.path.dirname(font_path), exist_ok=True)
    if not os.path.isfile(font_path):
        raise Exception("Fuck")
    return font_path

def text_to_ascii_image_with_font(
    text: str,
    font_size: int = 14,
    padding: int = 10,
    bg_color: str = "white",
    text_color: str = "black",
) -> Image.Image:
    """
    Renders text (ASCII, code, etc) using a guaranteed monospaced font into a JPEG image.
    """
    # Ensure font is available
    font_path = ensure_font()
    try:
        font = ImageFont.truetype(font_path, font_size)

        lines = text.splitlines() or [""]
        # Measure by using a representative character
        # Use "M" or some typical wide char
        (char_width, char_height) = font.getbbox("M")[2:4]
        print(char_width, char_height)
        max_line_len = max(len(line) for line in lines)
        img_width = char_width * max_line_len + 2 * padding
        img_height = char_height * len(lines) + 2 * padding

        img = Image.new("RGB", (img_width, img_height), color=bg_color)
        draw = ImageDraw.Draw(img)

        y = padding
        for line in lines:
            draw.text((padding, y), line, font=font, fill=text_color)
            y += char_height

        return img

    except Exception as e:
        print(f"Warning: could not load monospaced font: {e}")
        raise e


def image_to_ascii(image: Image.Image, new_width: int = 600) -> str:
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
    new_height = int(aspect_ratio * new_width * 0.8)  # 0.8 compensates font aspect ratio
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

max_width = st.slider("Line width (in ASCII characters)", min_value=50, max_value=400, value=300)


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Convert to ASCII
    ascii_art = image_to_ascii(image, new_width=max_width)
    im2 = text_to_ascii_image_with_font(ascii_art, font_size=18)

    # Create two columns
    col1, col2 = st.columns(2)

    # Place the first image in the first column
    with col1:
        # Open the uploaded image
        st.subheader("Original Image")
        st.image(image, width='content', caption="Original Image")

    # Place the second image in the second column
    with col2:
        st.subheader("ASCII Image")
        st.image(im2, width='content',)

    with st.expander("Click to reveal and copy the ASCII text"):
        st.subheader("ASCII Image")
        st.text("Copy to clipboard...")
        st_copy_to_clipboard(ascii_art)
        st.markdown(f"```{ascii_art}```")




