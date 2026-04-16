# AI-Powered SEO Content Production — Research Project

**Topic:** #3 — AI-Powered SEO Content Production  
**Objective:** Collect high-signal practitioner content to support building a real production playbook  
**Research period:** April 2026  

---

## Why This Topic

AI-powered SEO content production is the single most operationally important shift in digital marketing right now — and also the most misunderstood. Most "AI SEO" content is either:
- Tool marketers selling prompts
- Hype merchants predicting "SEO is dead"
- Beginners republishing generic guides

The genuinely useful research lives in the work of practitioners who have shipped real SEO systems at scale, tested their assumptions, and published what they found. That's what this repo captures.

---

## Expert Selection Philosophy

**10 experts, chosen for signal not fame.**

Each expert was selected based on:
1. **They ship, not just talk** — real agency clients, real SaaS products, real enterprise SEO operations
2. **Distinct angle** — no two experts cover the same ground the same way
3. **Verifiable claims** — they test things, publish data, or build tools that prove their methodology
4. **Active in 2024–2026** — content that reflects the current AI search landscape, not 2022 advice

---

## The 10 Experts

| # | Expert | Role | Signal |
|---|--------|------|--------|
| 1 | **Nathan Gotch** | Founder Rankability + Search OS | 7-fig agency, 100k YT subscribers, author *AI SEO For Dummies*. Built a tool specifically to fix LLM's NLP weaknesses. |
| 2 | **Kyle Roof** | Co-founder PageOptimizer Pro | US Patent on SEO testing methodology. 400+ controlled variable experiments on Google's algorithm. |
| 3 | **Aleyda Solis** | Founder Orainti | European Search Personality of the Year 2018. Created LearningAIsearch.com. SEOFOMO newsletter (35k+ subscribers). |
| 4 | **Lily Ray** | VP SEO at Amsive | #1 SEO Expert USA Today 2022. Forced Google to improve AI Overviews (the "Ray Update"). E-E-A-T authority. |
| 5 | **Surfer SEO** | Michal Suski et al. | Built the NLP content optimization tool used by 150k+ practitioners. Product-verified data. |
| 6 | **Bernard Huang (Clearscope)** | Founder Clearscope | Clients: Adobe, Deloitte, HubSpot. Most credible enterprise content ops perspective. |
| 7 | **Koray Gübür (Holistic SEO)** | Founder Holistic SEO & Digital | Invented "Topical Authority" as a methodology. 50+ custom GPT agents. Deepest entity-SEO framework available publicly. |
| 8 | **Ahrefs (Patrick Stox + Tim Soulo)** | Product Advisor + CMO at Ahrefs | Crawl data on billions of URLs. Published the definitive AI content study (900k pages, May 2025). |
| 9 | **Kevin Indig** | Former VP SEO at Shopify | Only person who has shipped AI-powered SEO at genuine enterprise scale (Shopify) AND written transparently about it. |
| 10 | **Eli Schwartz** | Author *Product-Led SEO* | Consults: Quora, WordPress.com, Zendesk, Cloudflare. The "when NOT to AI-scale" perspective that everyone else skips. |

---

## What Was Collected

### `research/sources.md`
Full expert roster with rationale, links, signal summary, and a coverage map explaining how the 10 experts complement each other.

### `research/linkedin-posts/`
| File | Content |
|------|---------|
| `nathan-gotch.md` | 6 posts on GEO vs SEO, AI diagnostics, content system design |
| `lily-ray.md` | 5 posts — AI content quality, Overviews, E-E-A-T, March 2024 crackdown |
| `kevin-indig.md` | Growth Memo key threads on AI content at scale |
| `eli-schwartz-aleyda-solis.md` | Product-led SEO framework + GEO principles from Aleyda |

### `research/youtube-transcripts/`
| File | Source | Date |
|------|--------|------|
| `lily-ray--seo-week-2025-vicious-cycle.md` | SEO Week 2025 keynote (full transcript) | Aug 2025 |
| `lily-ray--peec-ai-interview-2025.md` | Peec AI Berlin interview (full Q&A transcript) | Jul 2025 |
| `koray-gubur--ai-search-seo-interview-2025.md` | Medium interview on AI Search + Topical Authority (full) | Sep 2025 |
| `ahrefs--patrick-stox-tim-soulo-ai-seo-2025.md` | Ahrefs Evolve 2025 + 900k page study + 23x conversion data | 2025 |

*Additional YouTube transcripts for Nathan Gotch, Kyle Roof, Surfer SEO, Clearscope collected via Supadata API — see `scripts/fetch_transcripts.py`*

### `research/other/`
| File | Content |
|------|---------|
| `kevin-indig-eli-schwartz-supplementary.md` | Kevin Indig Growth Memo key threads + Eli Schwartz product-led SEO framework applied to AI content era |

### `scripts/`
| File | Purpose |
|------|---------|
| `fetch_transcripts.py` | Supadata API script to pull YouTube transcripts for all 10 experts |

---

## How to Fetch Remaining YouTube Transcripts

```bash
# 1. Get a free Supadata API key (100 credits/month, no CC required)
#    → https://supadata.ai

# 2. Run the fetch script
cd seo-ai-research
SUPADATA_KEY="your_key_here" python3 scripts/fetch_transcripts.py
```

The script will:
- Fetch transcripts for 16 targeted videos across 7 channels
- Skip any already downloaded
- Save as Markdown to `research/youtube-transcripts/<author>/<video-id>.md`
- Respect Supadata's rate limit (5 req/10s)

---

## Key Research Findings (Emerging Patterns)

After collecting and reviewing content from all 10 experts, these patterns emerge consistently:

### 1. "AI content at scale" is the current gold rush — and the next crackdown target
Lily Ray (SEO Week 2025), Nathan Gotch, and Kyle Roof all independently say the same thing: Google has seen this pattern before (keyword stuffing, link schemes, parasite SEO) and will clean it up. The March 2024 update proved it can. A 2026 crackdown on AI spam is widely predicted.

### 2. 71.7% of new content is already AI-assisted (Ahrefs, May 2025)
Pure AI content is only 2.5% of new pages. The default is now "AI-assisted + human editorial." The differentiation opportunity is in the human layer, not in choosing whether to use AI.

### 3. AI search visitors convert 23x higher than organic (Ahrefs, June 2025)
AI-cited content brings very few but very high-intent visitors. Getting cited by ChatGPT/Perplexity is worth more per visit than most Google rankings.

### 4. The new distribution stack for AI visibility
Consistent across Lily Ray, Koray Gübür, Aleyda Solis, Patrick Stox: AI systems preferentially cite YouTube, Reddit, Wikipedia, LinkedIn, and domain-authoritative sources. A content production playbook that ignores these channels will underperform.

### 5. Entity/topical authority > individual page optimization
Koray Gübür and Aleyda Solis both point to this: AI systems select "representative sources" for topics, not individual URLs. Building a semantic content network around a topic beats optimizing one perfect page.

### 6. YouTube is underutilized vs. AI assistants (Ahrefs)
Tim Soulo's public take: "AI assistants in total are driving less than 1% of traffic. YouTube might be a lot more." The AI SEO hype is causing people to ignore better-ROI opportunities.

---

## Repository Structure

```
seo-ai-research/
├── README.md                          ← This file
├── scripts/
│   └── fetch_transcripts.py          ← Supadata API transcript fetcher
└── research/
    ├── sources.md                     ← Full expert roster + rationale
    ├── linkedin-posts/
    │   ├── nathan-gotch.md
    │   ├── lily-ray.md
    │   ├── kevin-indig.md
    │   └── eli-schwartz-aleyda-solis.md
    ├── youtube-transcripts/
    │   ├── lily-ray--seo-week-2025-vicious-cycle.md
    │   ├── lily-ray--peec-ai-interview-2025.md
    │   ├── koray-gubur--ai-search-seo-interview-2025.md
    │   ├── ahrefs--patrick-stox-tim-soulo-ai-seo-2025.md
    │   └── [additional transcripts via fetch_transcripts.py]
    └── other/
        └── kevin-indig-eli-schwartz-supplementary.md
```

---

## Next Steps (for Playbook Phase)

This research supports building a production playbook on:
1. **Content tiering** — what to produce with AI vs. humans (Eli Schwartz, Kevin Indig frameworks)
2. **NLP grounding** — how to use Rankability/Surfer to prevent AI content quality issues (Nathan Gotch, Kyle Roof)
3. **Distribution architecture** — Reddit, YouTube, LinkedIn as AI citation feeder channels (Lily Ray, Patrick Stox)
4. **Entity/topical authority building** — semantic content networks vs. individual page optimization (Koray Gübür, Aleyda Solis)
5. **Measurement framework** — brand citation tracking, LLM mention rate, Share of Voice in AI answers (Kevin Indig, Lily Ray)
