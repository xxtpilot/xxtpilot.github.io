"""Check the generated website using only the Python standard library."""

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1] / "site"
SITE_HOST = "xxtpilot.github.io"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


def main():
    pages = {p.resolve(): Page(p) for p in ROOT.rglob("*.html")}
    errors = []
    checked = 0
    for path, page in pages.items():
        # 404.html uses site-relative runtime paths outside a normal page route.
        if path.name == "404.html":
            continue
        for link in page.links:
            url = urlsplit(link)
            if url.scheme and url.scheme not in ("http", "https"):
                continue
            if url.netloc and url.netloc != SITE_HOST:
                continue
            target = unquote(url.path)
            if target.startswith("/") or url.netloc:
                dest = ROOT / target.lstrip("/")
            elif target:
                dest = path.parent / target
            else:
                dest = path
            if dest.is_dir():
                dest /= "index.html"
            dest = dest.resolve()
            checked += 1
            if not dest.is_relative_to(ROOT.resolve()) or not dest.is_file():
                errors.append(f"{path.relative_to(ROOT)}: missing {link}")
            elif url.fragment and dest in pages and unquote(url.fragment) not in pages[dest].ids:
                errors.append(f"{path.relative_to(ROOT)}: missing anchor {link}")
    index = json.loads((ROOT / "search/search_index.json").read_text(encoding="utf-8"))
    if not index.get("docs") or "zh" not in index.get("config", {}).get("lang", []):
        errors.append("Chinese search index is missing or empty")
    expected_images = {"study-queue.png", "catalog.png", "other-features.png", "tools.png",
                       "questions.png", "entry-original.png", "course-selection.png"}
    for image in expected_images:
        if not (ROOT / "assets/images" / image).is_file():
            errors.append(f"Missing product image: {image}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Website checked: {len(pages)} HTML pages, {checked} local links/assets, "
          f"{len(index['docs'])} search entries, 7 screenshots.")


if __name__ == "__main__":
    main()
