#!/usr/bin/env python3
"""Build the static chapter pages and matching Markdown Ask AI sections.

Run from any directory: python3 scripts/build_chapters.py
Edit content/ai_questions.json for questions and tutorials/*/README.md for outlines.
"""

from html import escape
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
GROUP_ANCHORS = {
    "Foundations": "foundations",
    "Electronic structure": "electronic-structure",
    "Potential energy and reactions": "energy-and-reactions",
    "Molecular simulation": "molecular-simulation",
}


def section(text, heading):
    match = re.search(r"^## " + re.escape(heading) + r"\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else ""


def reference_links(references):
    return "".join(
        f'<li><a href="{escape(url, quote=True)}">{escape(label)}</a></li>'
        for label, url in references
    )


def markdown_questions(chapter, data):
    lines = [
        "## Ask AI when you get stuck", "",
        "Practise asking a precise question, examining the explanation, and checking your understanding.", "",
        "**Example-answer provenance:** " + data["answer_provenance"], "",
        data["model_guidance"], "",
        "### Build a useful question", "",
    ]
    lines += [f'{i}. **{item["label"]}:** {item["description"]}'
              for i, item in enumerate(data["prompt_framework"], 1)]
    for i, question in enumerate(chapter["questions"], 1):
        lines += [
            "", f'### {i}. {question["title"]}', "",
            f'**Starting question:** “{question["confusion"]}”', "",
            "**A more useful question to ask:**", "", "> " + question["prompt"], "",
            "**Why this helps:** " + question["why"], "",
            "**Example answer:** " + question["answer"], "",
            "**Follow-up to ask:**", "", "> " + question["follow_up"], "",
            "**Check your understanding:** " + question["check_question"], "",
            "<details>", "<summary>Reveal the check answer</summary>", "",
            question["check_answer"], "", "</details>",
        ]
    return "\n".join(lines) + "\n\n"


def question_html(question, index):
    prompt_id = f"prompt-{index}"
    return f'''      <article class="question-card" id="question-{index}" aria-labelledby="question-title-{index}">
        <p class="section-label">Sticking point {index:02d}</p>
        <h3 id="question-title-{index}">{escape(question["title"])}</h3>
        <p class="starting-question"><strong>Starting question</strong> “{escape(question["confusion"])}”</p>
        <div class="prompt-box">
          <div class="prompt-box-heading"><h4>A more useful question</h4><button class="copy-button" type="button" data-copy-target="{prompt_id}" hidden>Copy question</button></div>
          <p class="prompt-text" id="{prompt_id}">{escape(question["prompt"])}</p>
        </div>
        <p class="question-reason"><strong>Why this helps:</strong> {escape(question["why"])}</p>
        <details class="example-answer"><summary>Compare with an example answer</summary><div class="answer-content"><p>{escape(question["answer"])}</p><p class="answer-provenance">Course-authored teaching example. Your AI response may differ.</p></div></details>
        <div class="follow-up"><h4>Follow-up to ask</h4><p>{escape(question["follow_up"])}</p></div>
        <details class="self-check"><summary>Check your understanding</summary><div class="answer-content"><p>{escape(question["check_question"])}</p><details class="check-answer"><summary>Reveal the check answer</summary><p>{escape(question["check_answer"])}</p></details></div></details>
      </article>'''


def builder_html():
    return '''    <section class="question-builder chapter-section" aria-labelledby="builder-title">
      <p class="section-label">Practise the skill</p><h2 id="builder-title">Build your own question.</h2>
      <p>Complete the prompts below, then paste your draft into ChatGPT or another AI tutor. Your text stays on this page; the builder does not send it to an AI service.</p>
      <noscript><p>Use this pattern: what I know → where I am stuck → my evidence → help I need → how I will check.</p></noscript>
      <form data-question-builder hidden>
        <div class="builder-fields">
          <label>What I already understand<textarea name="known" rows="3" placeholder="For example: I know that HF uses orbitals."></textarea></label>
          <label>Where I am stuck <span>(required)</span><textarea name="stuck" rows="3" required placeholder="Name the step, term, result, or contradiction that confuses you."></textarea></label>
          <label>Evidence and context<textarea name="evidence" rows="3" placeholder="Relevant molecule, charge, spin, method, basis, units, code, or output."></textarea></label>
          <label>What would help me?<select name="help"><option value="concept">A conceptual explanation</option><option value="comparison">A comparison of two ideas</option><option value="diagnosis">Help interpreting an error or result</option><option value="hint">One hint before the solution</option></select></label>
        </div>
        <button class="button primary" type="submit">Build my question</button>
        <div class="builder-result" hidden><h3>Your question to copy</h3><pre id="built-question" tabindex="0"></pre><button class="copy-button" type="button" data-copy-target="built-question">Copy my question</button><p role="status" data-builder-status></p></div>
      </form>
    </section>
    <section class="study-record chapter-section" aria-labelledby="record-title">
      <h2 id="record-title">Keep a learning record.</h2>
      <p>When you try a question, note the tool, model name shown in the app, and date. Save your question, the actual AI answer, the follow-up, and what you verified.</p>
      <div class="record-fields"><label>Tool<input type="text" placeholder="For example: ChatGPT" autocomplete="off"></label><label>Model shown in your app<input type="text" placeholder="Enter the displayed model name" autocomplete="off"></label><label>Date<input type="date"></label></div>
      <p class="chapter-note">These fields are a temporary reminder on this page. Copy them into your own notes before leaving; they are not saved.</p>
    </section>'''


def render_chapter(chapter, chapters, index, data):
    title, group = chapter["title"], chapter["group"]
    goals = "".join(f'<li>{escape(goal)}</li>' for goal in chapter["goals"])
    videos = "".join(f'<li>{escape(video)}</li>' for video in chapter["videos"])
    question_index = "".join(
        f'<a href="#question-{i}">{i:02d} · {escape(question["title"])}</a>'
        for i, question in enumerate(chapter["questions"], 1)
    )
    navigation = ['<a href="../index.html#curriculum">All chapters</a>']
    if index:
        previous = chapters[index - 1]
        navigation.append(f'<a rel="prev" href="{previous["directory"]}.html">← {escape(previous["title"])}</a>')
    if index + 1 < len(chapters):
        following = chapters[index + 1]
        navigation.append(f'<a rel="next" href="{following["directory"]}.html">{escape(following["title"])} →</a>')
    framework = "".join(
        f'<li><strong>{escape(item["label"])}</strong><span>{escape(item["description"])}</span></li>'
        for item in data["prompt_framework"]
    )
    questions = "\n".join(question_html(question, i) for i, question in enumerate(chapter["questions"], 1))
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="Learn {escape(title, quote=True)} by asking better AI questions, comparing worked answers, and checking your understanding.">
  <title>{escape(title)} | Ask AI | AI4CompChem</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&amp;family=Manrope:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css"><link rel="stylesheet" href="../chapters.css">
</head>
<body>
  <header class="site-header">
    <a class="brand" href="../index.html"><span class="brand-mark"><i></i><i></i><i></i></span><span>AI4<span>CompChem</span></span></a>
    <button class="menu-button" aria-label="Open navigation" aria-expanded="false"><span></span><span></span></button>
    <nav class="site-nav"><a href="../index.html#curriculum">All chapters</a><a href="#ask-ai">Ask AI</a><a href="#references">References</a><a class="github-link" href="https://github.com/xueyongshef/AI4CompChem">GitHub ↗</a></nav>
  </header>
  <main class="chapter-main" id="top">
    <header class="chapter-heading">
      <a class="chapter-back" href="../index.html#{GROUP_ANCHORS[group]}">← {escape(group)}</a>
      <p class="section-label">Chapter {index + 1:02d} · {escape(group)}</p>
      <h1>{escape(title)}</h1>
      <p class="chapter-subtitle">{escape(chapter["subtitle"])}</p>
      <p class="chapter-intro">Learn the chemistry by turning a sticking point into a precise question, examining an answer, and explaining the idea yourself.</p>
      <a class="button primary" href="#ask-ai">Explore three worked questions ↓</a>
    </header>
    <section class="chapter-overview chapter-section" aria-label="Chapter outline">
      <div><h2>What you will learn</h2><ul>{goals}</ul></div>
      <details class="lesson-plan"><summary>Video and exercise plan</summary><p>Videos, full explanatory lessons, and runnable exercises are in preparation. The Ask AI examples below are available to study now.</p><h3>Planned short videos</h3><ol>{videos}</ol><h3>Planned exercise</h3><p>{escape(chapter["exercise"])}</p></details>
    </section>
    <section class="chapter-section" id="ask-ai" aria-labelledby="ask-ai-title">
      <p class="section-label">A separate space for your questions</p><h2 id="ask-ai-title">Ask AI when you get stuck.</h2>
      <p>Choose a problem below. Adapt the question to your situation, try it in your AI tool, then compare the explanation and use the self-check.</p>
      <p class="example-note"><strong>About the answers:</strong> {escape(data["answer_provenance"])} {escape(data["model_guidance"])}</p>
      <ol class="question-framework">{framework}</ol>
      <nav class="question-index" aria-label="Common sticking points">{question_index}</nav>
{questions}
    </section>
{builder_html()}
    <section class="chapter-section chapter-references" id="references"><h2>Check the explanation.</h2><p>Use these references together with the actual inputs and outputs of your calculation.</p><ul>{reference_links(chapter["references"])}</ul><p><a href="{escape(data["prompting_reference"][1], quote=True)}">General prompting guidance from OpenAI</a></p></section>
    <nav class="chapter-navigation" aria-label="Chapter navigation">{"".join(navigation)}</nav>
    <p class="copy-status" role="status" aria-live="polite" data-copy-status></p>
  </main>
  <section class="supporters" aria-label="Project support and affiliation">
    <div class="supporter supporter-rsc"><p class="supporter-label">Supported by RSC – EDI</p><a class="supporter-logo" href="https://www.rsc.org/policy-and-campaigning/science-culture"><img src="../assets/royal-society-of-chemistry.svg" alt="Royal Society of Chemistry" width="252" height="71"></a><p class="supporter-detail">Equality, Diversity &amp; Inclusion</p></div>
    <div class="supporter supporter-liverpool"><a class="supporter-logo" href="https://www.liverpool.ac.uk/"><img src="../assets/university-of-liverpool.svg" alt="University of Liverpool" width="284" height="72"></a></div>
  </section>
  <footer class="chapter-footer"><a href="../index.html">AI4CompChem</a><p>Ask a better question. Build a clearer understanding.</p><a href="https://github.com/xueyongshef/AI4CompChem">Source on GitHub ↗</a></footer>
  <script src="../script.js"></script><script src="../chapters.js"></script>
</body>
</html>
'''


def build():
    data = json.loads((ROOT / "content/ai_questions.json").read_text())
    chapters = data["chapters"]
    chapter_directories = sorted(p.name for p in (ROOT / "tutorials").iterdir() if p.is_dir())
    if [chapter["directory"] for chapter in chapters] != chapter_directories:
        raise ValueError("Question bank and tutorial directories must match in learning order")
    required = {"title", "confusion", "prompt", "why", "answer", "follow_up", "check_question", "check_answer"}
    for chapter in chapters:
        if len(chapter["questions"]) != 3:
            raise ValueError(f'{chapter["directory"]}: expected three worked examples')
        for question in chapter["questions"]:
            if not required <= question.keys() or not all(question[key].strip() for key in required):
                raise ValueError(f'{chapter["directory"]}: incomplete worked example')
        path = ROOT / "tutorials" / chapter["directory"] / "README.md"
        original = path.read_text()
        heading = re.match(r"# \d+\. (.+)", original).group(1)
        group_line = original.splitlines()[2]
        group, subtitle = group_line.split(" · ", 1)
        chapter.update(title=heading, group=group, subtitle=subtitle)
        chapter["goals"] = re.findall(r"^- (.+)", section(original, "Learning goals"), re.M)
        chapter["videos"] = re.findall(r"^\d+\. (.+)", section(original, "Planned short videos"), re.M)
        chapter["exercise"] = section(original, "Planned exercise")
        references = re.findall(r"\[([^\]]+)\]\((https://[^)]+)\)", section(original, "References"))
        for reference in chapter["references"]:
            if reference[1] not in {url for _, url in references}:
                references.append(tuple(reference))
        chapter["references"] = references
        updated = original.replace(
            "**Status: topic outline.** Videos, explanatory lessons, and runnable exercises are in preparation.",
            "**Status: chapter outline with worked Ask AI examples.** Videos, full explanatory lessons, and runnable exercises are in preparation.",
        )
        updated, count = re.subn(
            r"^## (?:AI study prompt|Ask AI when you get stuck)\n.*?(?=^## |\Z)",
            lambda _: markdown_questions(chapter, data), updated, count=1, flags=re.M | re.S,
        )
        if count != 1:
            raise ValueError(f'{path}: expected one Ask AI section')
        reference_section = "## References\n\n" + "\n".join(f"- [{label}]({url})" for label, url in references) + "\n\n"
        if re.search(r"^## References$", updated, re.M):
            updated = re.sub(r"^## References\n.*?(?=^## |\Z)", lambda _: reference_section, updated, count=1, flags=re.M | re.S)
        else:
            updated = updated.replace("## Learning path", reference_section + "## Learning path", 1)
        path.write_text(updated)
    destination = ROOT / "docs/chapters"
    destination.mkdir(exist_ok=True)
    for index, chapter in enumerate(chapters):
        (destination / f'{chapter["directory"]}.html').write_text(render_chapter(chapter, chapters, index, data))
    print(f'Built {len(chapters)} static chapter pages and {sum(len(c["questions"]) for c in chapters)} worked Ask AI examples.')


if __name__ == "__main__":
    build()
