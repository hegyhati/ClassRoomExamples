
SVG_BLOCK_SIZE = 100
STROKE_WIDTH = 5
RECT_BLOCK_STYLE = f' rx="10" ry="10" fill-opacity="0.9" stroke-width="{STROKE_WIDTH}" '
RECT_BLOCK_HIGHLIGHT_STYLE = f' stroke-width="{STROKE_WIDTH*2}" '


BACKGROUND_OK = "white"
BACKGROUND_NOK = "black"
BACKGROUND_HIGHLIGHT = "khaki"


__colors = [
    "tomato",
    "navy",
    "yellowgreen",
    "lightskyblue",
    "orchid",
    "orange",
    "gray",
    "forestgreen",
    "deepskyblue",
    "gold",
    "orangered",
    "indigo",
    "dodgerblue",
    "darkorange",
    "crimson",
    "yellow",
    "forestgreen",
    "fuchsia",
    "firebrick",
    "teal"
]

if BACKGROUND_OK in __colors: __colors.remove(BACKGROUND_OK)
if BACKGROUND_NOK in __colors: __colors.remove(BACKGROUND_NOK)
if BACKGROUND_HIGHLIGHT in __colors: __colors.remove(BACKGROUND_HIGHLIGHT)


def color(id:int = 0) -> str:
    return __colors[id % len(__colors)]
