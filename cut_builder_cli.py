from my_io.cutlist_reader.cutlist_reader import read_cutlist
from my_io.scipt_writer.script_writer import write_script_file

cutlist = read_cutlist("test.txt")
# TODO: validate and format timestamps in cutlist
msg: str = write_script_file(cutlist)

with open("ffmpeg-script.bat", "w") as f:
    f.write(msg)