
SVG_BLOCK_SIZE = 100
STROKE_WIDTH = 5
RECT_BLOCK_STYLE = f' rx="10" ry="10" fill-opacity="0.8" stroke-width="{STROKE_WIDTH}" '

BACKGROUND_OK = "white"
BACKGROUND_NOK = "black"


__colors = [
    "aqua",
    "coral",
    "crimson",
    "darkorange",
    "deepskyblue",
    "dodgerblue",
    "firebrick",
    "forestgreen",
    "fuchsia",
    "gold",
    "indigo",
    "lime",
    "mediumseagreen",
    "mediumvioletred",
    "navy",
    "orangered",
    "purple",
    "saddlebrown",
    "teal",
    "tomato"
]

if BACKGROUND_OK in __colors: __colors.remove(BACKGROUND_OK)
if BACKGROUND_NOK in __colors: __colors.remove(BACKGROUND_NOK)


def color(id:int = 0) -> str:
    return __colors[id % len(__colors)]
