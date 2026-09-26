"""Create an exact knockout version from an approved Margô positive PNG."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_hex_color(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("color must use RRGGBB format")
    try:
        return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("color must use hexadecimal digits") from exc


def make_negative(source: Image.Image, color: tuple[int, int, int]) -> Image.Image:
    rgba = source.convert("RGBA")
    result = Image.new("RGBA", rgba.size, (*color, 0))
    output = []

    for red, green, blue, alpha in rgba.get_flattened_data():
        # Estimate the white contribution in the antialiased white-on-burgundy
        # source. Burgundy and colored halos have almost no green/blue content.
        white_coverage = min(red, green, blue)
        out_alpha = round(alpha * white_coverage / 254) if alpha else 0
        if out_alpha >= 250:
            out_alpha = 255
        elif out_alpha <= 2:
            out_alpha = 0
        output.append((*color, out_alpha))

    result.putdata(output)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert an approved Margô positive PNG into an exact negative."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--color",
        type=parse_hex_color,
        default=parse_hex_color("81010E"),
        help="output color in RRGGBB format (default: 81010E)",
    )
    args = parser.parse_args()

    source = Image.open(args.input)
    result = make_negative(source, args.color)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.save(args.output, "PNG", optimize=True)


if __name__ == "__main__":
    main()
