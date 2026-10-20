(() => {
  'use strict';

  const helpRequests = {
    concept: 'Explain the concept at my level, define unfamiliar terms, and use one small example.',
    comparison: 'Compare the ideas I am mixing up. State what differs and what stays the same.',
    diagnosis: 'Help me interpret the error or result. Ask for missing evidence before proposing a change.',
    hint: 'Give me one useful hint, then wait for my attempt before revealing a solution.'
  };

  function buildQuestion(input) {
    const clean = value => String(value || '').trim();
    const stuck = clean(input.stuck);
    if (!stuck) throw new Error('Describe the point where you are stuck.');
    const parts = [`I am studying ${clean(input.chapter) || 'computational chemistry'}.`];
    if (clean(input.known)) parts.push(`What I already understand: ${clean(input.known)}`);
    parts.push(`Where I am stuck: ${stuck}`);
    if (clean(input.evidence)) parts.push(`My evidence and context: ${clean(input.evidence)}`);
    parts.push(helpRequests[input.help] || helpRequests.concept);
    parts.push('State the assumptions you use. If essential context is missing, ask me for it. Use the information I provide and do not invent calculation outputs.');
    parts.push(input.help === 'hint'
      ? 'After I try the hint, help me check my reasoning against a reference or a small calculation.'
      : 'Explain how I can check the answer against a reference or a small calculation. Finish with one question to test my understanding, and wait for my answer.');
    return parts.join('\n\n');
  }

  globalThis.AI4CompChemStudy = Object.freeze({ buildQuestion });
  if (typeof document === 'undefined') return;

  const copyStatus = document.querySelector('[data-copy-status]');
  let statusTimer;
  document.querySelectorAll('[data-copy-target]').forEach(button => { button.hidden = false; });
  document.addEventListener('click', async event => {
    const button = event.target.closest('[data-copy-target]');
    if (!button) return;
    const target = document.getElementById(button.dataset.copyTarget);
    if (!target) return;
    let message;
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(target.textContent.trim());
      message = 'Question copied. Paste it into your AI tool and adapt it to your situation.';
    } catch {
      const selection = window.getSelection();
      if (selection) {
        const range = document.createRange();
        range.selectNodeContents(target);
        selection.removeAllRanges();
        selection.addRange(range);
      }
      message = 'Automatic copy is unavailable. The question is selected; copy it with your keyboard or device menu.';
    }
    if (copyStatus) {
      clearTimeout(statusTimer);
      copyStatus.textContent = message;
      statusTimer = setTimeout(() => { copyStatus.textContent = ''; }, 8000);
    }
  });

  document.querySelectorAll('[data-question-builder]').forEach(form => {
    form.hidden = false;
    form.addEventListener('submit', event => {
      event.preventDefault();
      const values = new FormData(form);
      const result = form.querySelector('.builder-result');
      const output = result.querySelector('pre');
      const status = result.querySelector('[data-builder-status]');
      try {
        output.textContent = buildQuestion({
          chapter: document.querySelector('.chapter-heading h1')?.textContent,
          known: values.get('known'),
          stuck: values.get('stuck'),
          evidence: values.get('evidence'),
          help: values.get('help')
        });
        result.hidden = false;
        status.textContent = 'Your draft question is ready. Read it, adapt it, and copy it when it describes your problem accurately.';
        output.focus();
      } catch (error) {
        result.hidden = false;
        output.textContent = '';
        status.textContent = error.message;
        form.querySelector('[name="stuck"]').focus();
      }
    });
  });
})();
