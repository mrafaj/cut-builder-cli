from typing import List, Tuple

# TODO: make this platform agnostic (currently Windows only)

def write_script_file(cutlist: List[Tuple[str, str, str]]) -> str:

    script: str = ""

    script += "mkdir cuts\n"

    digits: int = len(str(len(cutlist) - 1))

    for id, element in enumerate(cutlist):

        input, start, duration = element

        id_string: str = str(id).zfill(digits)

        script += f"ffmpeg -y -ss {start} -i {input} -t {duration} -avoid_negative_ts make_zero -c copy cuts/cut{id_string}.mp4\n"
        script += f"echo file cuts/cut{id_string}.mp4 >> cutlist.txt\n"

    script += "ffmpeg -safe 0 -f concat -i cutlist.txt -c copy output.mp4\n"

    script += "del cutlist.txt\n"
    script += "del /Q cuts\n"

    return script
