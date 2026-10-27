# Publications markdown generator for AcademicPages
#
# Takes a TSV / CSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io).
# Can be called via the command prompt by using `python3 publications.py [filename]`.

# Data format
#
# The file needs to have the following columns as a header at the top:
# pub_date, title, venue, excerpt, citation, url_slug, paper_url, slides_url
# - `excerpt`, `paper_url`, and slides_url can be blank, but the others must have values.
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the paper.
#    The .md file will be `YYYY-MM-DD-[url_slug].md`
import csv
import os
import re
import sys
from pathlib import Path

EXIT_ERROR = 0

HEADER_LEGACY = ['pub_date', 'title', 'venue', 'excerpt', 'citation', 'url_slug', 'paper_url', 'slides_url']
HEADER_UPDATED = ['pub_date', 'title', 'venue', 'excerpt', 'citation', 'url_slug', 'paper_url', 'slides_url', 'category']

HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    """Produce entities within text."""
    return "".join(HTML_ESCAPE_TABLE.get(c, c) for c in str(text))

def create_md(lines: list, layout: list):
    repo_root = Path(__file__).resolve().parent.parent
    output_dir = repo_root / "_publications"
    output_dir.mkdir(exist_ok=True)

    for item in lines:
        pub_date = str(item[layout.index('pub_date')]).strip()
        title = str(item[layout.index('title')]).strip()
        url_slug = str(item[layout.index('url_slug')]).strip()
        venue = str(item[layout.index('venue')]).strip()
        excerpt = str(item[layout.index('excerpt')]).strip()
        citation = str(item[layout.index('citation')]).strip()
        paper_url = str(item[layout.index('paper_url')]).strip()
        category = str(item[layout.index('category')]).strip() if len(layout) == len(HEADER_UPDATED) else "manuscripts"

        if not url_slug:
            url_slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

        md_filename = f"{pub_date}-{url_slug}.md"
        html_filename = f"{pub_date}-{url_slug}"

        md = f"---\ntitle: \"{title}\"\n"
        md += "collection: publications"
        md += f"\ncategory: {category}"
        md += f"\npermalink: /publication/{html_filename}"
        if len(excerpt) > 5:
            md += f"\nexcerpt: '{html_escape(excerpt)}'"
        md += f"\ndate: {pub_date}"
        md += f"\nvenue: '{html_escape(venue)}'"
        if len(paper_url) > 5:
            md += f"\npaperurl: '{paper_url}'"
        md += f"\ncitation: '{html_escape(citation)}'"
        md += "\n---"

        if len(paper_url) > 5:
            md += f"\n<a href='{paper_url}'>Download paper here</a>\n"
        if len(excerpt) > 5:
            md += f"\n{html_escape(excerpt)}\n"
        md += f"\nRecommended citation: {citation}"

        output_path = output_dir / os.path.basename(md_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)

def read(filename: str) -> tuple[list, list]:
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        delimiter = ',' if filename.endswith('.csv') else '\t'
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            row = [(cell or "").strip() for cell in row]
            lines.append(row)

    if len(lines) <= 1:
        print(f'Not enough lines in the file to process, found {len(lines)}', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    layout = HEADER_UPDATED
    if HEADER_LEGACY == lines[0]:
        layout = HEADER_LEGACY
    elif HEADER_UPDATED != lines[0]:
        print(lines[0])
        print('The header of the file does not match the expected format', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    lines = lines[1:]
    return lines, layout

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 publications.py [filename]', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    filename = sys.argv[1]
    if not (filename.endswith('.csv') or filename.endswith('.tsv')):
        print(f'Expected a TSV or CSV file, got {filename}', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    lines, layout = read(filename)
    create_md(lines, layout)
