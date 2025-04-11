import json
import markdown
import shutil
import yaml

from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

POSTS_DIR = Path('./posts')
OUTPUT_DIR = Path('./output')
TEMPLATES_DIR = Path('./includes')

site_title = "jb"
site_url = "https://jonathanbuys.com"


class Post:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.title = None
        self.date = None
        self.tags = None
        self.text = None
        self.slug = self.filepath.stem

        self._parse_file()

    def _parse_file(self):
        content = self.filepath.read_text(encoding='utf-8')
        parts = content.split('---')

        if len(parts) >= 3:
            header_text = parts[1].strip()
            body_text = '---'.join(parts[2:]).strip()

            metadata = yaml.safe_load(header_text)

            self.title = metadata.get('title')
            self.tags = metadata.get('tags')
            self.slug = metadata.get('slug', self.slug)
            self.text = markdown.markdown(body_text)

            date_val = metadata.get('date')
            if isinstance(date_val, datetime):
                self.date = date_val
            elif isinstance(date_val, str):
                try:
                    self.date = datetime.strptime(date_val, "%Y-%m-%d %H:%M:%S")
                except ValueError as e:
                    raise ValueError(f"Invalid date format in {self.filepath.name}: {date_val}") from e
            else:
                raise TypeError(f"Unrecognized date format in {self.filepath.name}: {date_val}")


class TemplateRenderer:
    def __init__(self):
        self.templates = {
            'head': (TEMPLATES_DIR / 'head.html').read_text(),
            'foot': (TEMPLATES_DIR / 'foot.html').read_text(),
            'article': (TEMPLATES_DIR / 'article.html').read_text(),
            'index': (TEMPLATES_DIR / 'index.html').read_text(),
            'archive': (TEMPLATES_DIR / 'archive.html').read_text()
        }

    def render_post(self, post: Post) -> str:
        head = self.templates['head'].replace('QQTITLE', post.title or '')
        mapping = {
            'QQHEAD': head,
            'QQTITLE': post.title or '',
            'QQPOSTTEXT': post.text or '',
            'QQFOOT': self.templates['foot']
        }
        html = self._fill_template(self.templates['article'], mapping)
        return html

    def render_index(self, posts) -> str:
        head = self.templates['head'].replace('QQTITLE', 'Home')
        foot = self.templates['foot']

        items_html = ""
        for post in posts:
            items_html += f"<article><h2><a href='{post.slug}.html'>{post.title}</a></h2>\n{post.text}\n</article>"

        mapping = {
            'QQHEAD': head,
            'QQPOSTTEXT': items_html,
            'QQTITLE': 'Home',
            'QQFOOT': foot
        }
        return self._fill_template(self.templates['index'], mapping)

    def render_archive(self, posts) -> str:
        head = self.templates['head'].replace('QQTITLE', 'Home')
        foot = self.templates['foot']

        items_html = ""
        for post in posts:
            items_html += f"<li><a href='{post.slug}.html'>{post.title}</a> - {post.date.strftime('%Y-%m-%d')}</li>\n"

        mapping = {
            'QQHEAD': head,
            'QQPOSTTEXT': f"<ul>{items_html}</ul>",
            'QQTITLE': 'Home',
            'QQFOOT': foot
        }
        return self._fill_template(self.templates['archive'], mapping)

    @staticmethod
    def _fill_template(template: str, mapping: dict) -> str:
        for key, value in mapping.items():
            template = template.replace(key, value)
        return template


def generate_atom_feed(posts, site_title, site_url):
    feed_items = []
    for post in posts:
        feed_items.append(f"""
  <entry>
    <title>{escape(post.title)}</title>
    <link href="{site_url}/{post.slug}.html"/>
    <id>{site_url}/{post.slug}.html</id>
    <updated>{post.date.isoformat()}Z</updated>
    <content type="html">{escape(post.text)}</content>
  </entry>
""")

    return f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>{escape(site_title)}</title>
  <link href="{site_url}/atom.xml" rel="self"/>
  <link href="{site_url}"/>
  <updated>{posts[0].date.isoformat()}Z</updated>
  <id>{site_url}/</id>
  {''.join(feed_items)}
</feed>
"""


def generate_json_feed(posts, site_title, site_url):
    feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": site_title,
        "home_page_url": site_url,
        "feed_url": f"{site_url}/feed.json",
        "items": []
    }

    for post in posts:
        feed["items"].append({
            "id": f"{site_url}/{post.slug}.html",
            "url": f"{site_url}/{post.slug}.html",
            "title": post.title,
            "content_html": post.text,
            "date_published": post.date.isoformat() + "Z"
        })

    return json.dumps(feed, indent=2)

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    renderer = TemplateRenderer()
    posts = []

    for file in POSTS_DIR.iterdir():
        if file.is_file():
            try:
                post = Post(file)
                posts.append(post)
            except Exception as e:
                print(f"Skipping {file.name}: {e}")

    posts.sort(key=lambda p: p.date, reverse=True)

    # Generate individual post pages
    for post in posts:
        html = renderer.render_post(post)
        output_file = OUTPUT_DIR / f"{post.slug}.html"
        output_file.write_text(html, encoding='utf-8')
        print(f"Wrote {output_file}")

    # Generate index page
    html = renderer.render_index(posts)
    output_file = OUTPUT_DIR / 'index.html'
    output_file.write_text(html, encoding='utf-8')
    print(f"Wrote {output_file}")

    # Generate archive page
    html = renderer.render_archive(posts)
    output_file = OUTPUT_DIR / 'archive.html'
    output_file.write_text(html, encoding='utf-8')
    print(f"Wrote {output_file}")
    
    source = Path('media')
    destination = Path('output/media')

    # Copy the entire folder into the subfolder
    shutil.copytree(source, destination, dirs_exist_ok=True)

    source_css = Path('style.css')
    dest_css = OUTPUT_DIR / 'style.css'
    shutil.copy2(source_css, dest_css)

    atom = generate_atom_feed(posts, site_title, site_url)
    (OUTPUT_DIR / "atom.xml").write_text(atom, encoding="utf-8")
    
    # JSON feed
    json_feed = generate_json_feed(posts, site_title, site_url)
    (OUTPUT_DIR / "feed.json").write_text(json_feed, encoding="utf-8")
    
    print("Wrote atom.xml and feed.json")


if __name__ == '__main__':
    main()
