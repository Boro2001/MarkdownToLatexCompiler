import grammar
import sys


def convert_to_pdf(filename, child_dir="out"):
    import os
    import subprocess

    try:
        os.makedirs(child_dir)
    except:
        pass

    # Markdown source filename
    md_filename = filename
    print("--------------------------------")
    # Filename without path
    filename, ext = os.path.splitext(md_filename)
    filename = os.path.normpath(filename).split(os.path.sep)[-1]
    tex_filename_no_dir = filename + ".tex"
    # Path to TeX output
    tex_filename = os.path.join(child_dir, tex_filename_no_dir)

    # Read Markdown file
    with open(md_filename) as f:
        lines = f.read()

    # Parse
    parser = grammar.get_parser()
    result = parser.parse(lines)

    # Save TeX
    with open(tex_filename, 'w') as f:
        f.write(result)

    # Run MiKTeX command
    os.chdir(child_dir)
    command = "pdflatex " + tex_filename_no_dir
    subprocess.call(command)


if len(sys.argv) == 2:
    convert_to_pdf(sys.argv[1])
elif len(sys.argv) == 3:
    convert_to_pdf(sys.argv[1], sys.argv[2])
else:
    print("Please provide markdown file to compile and optional directory name for output as arguments")
