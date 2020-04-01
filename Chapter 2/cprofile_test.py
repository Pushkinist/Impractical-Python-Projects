"""Simple cProfile example."""

import cProfile
import palingram

cProfile.run("palingram.main()")

# python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)
