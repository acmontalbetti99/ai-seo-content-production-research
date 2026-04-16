#!/usr/bin/env python3
"""
fetch_transcripts.py
--------------------
Fetches YouTube transcripts for the 10 AI-powered SEO content production experts
using the Supadata API (https://supadata.ai).

SETUP:
    1. Sign up at https://supadata.ai (100 free credits/month, no CC required)
    2. Copy your API key from the dashboard
    3. Run: SUPADATA_KEY="your_key_here" python3 scripts/fetch_transcripts.py

OUTPUT:
    Saves transcripts to research/youtube-transcripts/<author>/<video-id>.md
"""

import os, sys, time, requests
from pathlib import Path

API_KEY = os.environ.get("SUPADATA_KEY", "")
BASE_URL = "https://api.supadata.ai/v1/youtube/transcript"
OUTPUT_DIR = Path(__file__).parent.parent / "research" / "youtube-transcripts"

VIDEOS = [
    # Nathan Gotch — youtube.com/@nathangotch
    ("nathan-gotch", "AI-SEO-checklist-2025",    "AI SEO & GEO: The Ultimate Checklist for 2025", "2025"),
    ("nathan-gotch", "seo-for-2026-guide",        "SEO for 2026: The Complete Guide",              "2025"),
    ("nathan-gotch", "ai-seo-for-dummies-intro",  "AI SEO For Dummies - Introduction",             "2025"),
    # Kyle Roof — youtube.com/@PageOptimizerPro
    ("kyle-roof", "pop-ai-writer-tutorial",       "POP AI Writer Tutorial - NLP-optimized content",  "2024"),
    ("kyle-roof", "eeat-future-seo-ai",           "EEAT and the Future of SEO with AI",               "2023"),
    # Aleyda Solis — youtube.com/crawlingmondaysbyaleyda
    ("aleyda-solis", "crawling-mondays-ai-search", "Crawling Mondays: AI Search Optimization",    "2025"),
    # Surfer SEO — youtube.com/@surferseo
    ("surfer-seo", "ai-content-workflow",          "AI + Surfer SEO: Full Content Workflow",       "2024"),
    ("surfer-seo", "nlp-content-optimization",     "Why AI Content Fails Without NLP Grounding",   "2024"),
    # Clearscope — youtube.com/@clearscope
    ("clearscope", "ai-content-ops-enterprise",   "Enterprise AI Content Operations",             "2024"),
    # Ahrefs — youtube.com/@AhrefsOnlineSEOtools
    ("ahrefs", "geo-aeo-llmo-explainer",           "GEO? AEO? LLMO? What's with all this AI SEO?", "2025"),
]

def fetch_transcript(video_id):
    params = {"videoId": video_id, "text": "true"}
    headers = {"x-api-key": API_KEY}
    try:
        resp = requests.get(BASE_URL, params=params, headers=headers, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        print(f"  [HTTP {resp.status_code}] {video_id}")
    except requests.exceptions.RequestException as e:
        print(f"  [ERROR] {e}")
    return None

def save_transcript(author, video_id, title, year, data):
    folder = OUTPUT_DIR / author
    folder.mkdir(parents=True, exist_ok=True)
    content = data.get("content", "")
    if isinstance(content, list):
        content = " ".join(seg.get("text", "") for seg in content)
    md = f"# Transcript: {title}\n## Author: {author}\n\n**Year:** {year}\n**Video:** https://www.youtube.com/watch?v={video_id}\n\n---\n\n{content}\n"
    (folder / f"{video_id}.md").write_text(md, encoding="utf-8")
    print(f"  Saved: {author}/{video_id}.md ({len(content)/1024:.1f}KB)")

def main():
    if not API_KEY:
        print("ERROR: SUPADATA_KEY not set. Get free key at https://supadata.ai")
        sys.exit(1)
    print(f"Fetching {len(VIDEOS)} transcripts via Supadata API...\n")
    success = failed = 0
    for author, vid, title, year in VIDEOS:
        print(f"-> [{author}] {title}")
        output_file = OUTPUT_DIR / author / f"{vid}.md"
        if output_file.exists():
            print(f"  Already exists, skipping.")
            success += 1
            continue
        data = fetch_transcript(vid)
        if data:
            save_transcript(author, vid, title, year, data)
            success += 1
        else:
            print(f"  Failed: {vid}")
            failed += 1
        time.sleep(2.5)
    print(f"\nDone. {success} succeeded, {failed} failed.")

if __name__ == "__main__":
    main()
