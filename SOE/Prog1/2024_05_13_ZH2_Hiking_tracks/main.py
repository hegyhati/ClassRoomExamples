#! /usr/bin/env python3
import os
import sys
import matplotlib.pyplot as plt
import argparse
from xml import fetch_arg_values, fetch_tag_values


def get_hikes(path: str) -> list[str]:
    tracks = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext = os.path.splitext(os.path.join(path, file))
            if ext == ".gpx":
                tracks.append(file)
    return tracks


def generate_track_overlay(path: str, outfile: str) -> None:
    gpx_files = get_hikes(path)
    fig, ax = plt.subplots()
    for gpx in gpx_files:
        with open(os.path.join(path, gpx)) as f:
            track = [fetch_arg_values(line.strip()) for line in f if "<trkpt" in line]
        lon = [float(tp["lon"]) for tp in track]
        lat = [float(tp["lat"]) for tp in track]
        ax.scatter(lon, lat, s=1, label=gpx)
    ax.axis("off")
    fig.legend(bbox_to_anchor=(1, 0.9))
    fig.suptitle(f"Hiking tracks in {path}")
    fig.tight_layout()
    fig.savefig(os.path.join(path, outfile), dpi=600)


def generate_analysis(file: str, outfile: str) -> None:
    fig, ax = plt.subplots(2)
    hr = fetch_tag_values(file, "ns3:hr")
    ele = fetch_tag_values(file, "ele", float)
    ax[0].plot(hr, color="red")
    ax[0].set_title("Heart rate")
    ax[0].set_xticklabels([])
    ax[1].plot(ele, color="green")
    ax[1].set_title("Elevation")
    ax[1].fill_between(range(len(ele)), ele, color="green", alpha=0.5)
    ax[1].set_xticklabels([])
    fig.suptitle(f"Analysis of {file}")
    fig.tight_layout()
    fig.savefig(outfile, dpi=600)


if __name__ == "__main__":
    COMMANDS = ["overlay", "analyze"]
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=COMMANDS)
    parser.add_argument(
        "--path",
        "-p",
        required="overlay" in sys.argv,
        help="[Overlay] path to the directory containing the GPX files",
    )
    parser.add_argument(
        "--file",
        "-f",
        required="analyze" in sys.argv,
        help="[Analyze] the GPX file to analyze",
    )
    parser.add_argument("--output", "-o", help="name for the generated diagram")
    args = parser.parse_args()

    if args.command == "overlay" and args.path:
        outfile = args.output if args.output else "overlay.png"
        try:
            generate_track_overlay(args.path, outfile)
        except FileNotFoundError:
            print("The specified path does not exist.")
    elif args.command == "analyze" and args.file:
        outfile = (
            args.output if args.output else os.path.splitext(args.file)[0] + ".png"
        )
        try:
            generate_analysis(args.file, outfile)
        except FileNotFoundError:
            print("The specified file does not exist.")
