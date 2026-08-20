# NAIST Information Science Essay Workspace

This workspace contains a two-page English draft for the NAIST information
science essay and the notes used to select its topic. The LaTeX layout
currently follows the compact `naist1.pdf`-style header used in the local
reference proposal:

- the name in the upper-right corner;
- one right-aligned header line for exam category, preferred laboratory, and
  current specialization;
- a horizontal rule below the header;
- a centered page number in the footer;
- the proposed research topic line; and
- the two required numbered sections.

## Draft topic

`Evaluating Host-Level Context for Detecting Short-Lived DNS-over-HTTPS Traffic`

The draft intentionally limits the core scope to DoH. QUIC-based encrypted DNS
transports such as DoQ are mentioned only as future extensions. This keeps the
proposal aligned with current research trends without making the interview
depend on protocol details that still need to be learned.

## Layout

The current PDF follows the compact local reference style from `naist1.pdf`:

- a two-column body across both pages, interrupted on the first page by a
  full-width undergraduate framework figure for readability;
- the compact `naist1.pdf`-style header repeated on each page;
- Figure 1 for the undergraduate TAC-Seq framework, copied from the thesis
  `fig_3_1()` layout without structural simplification and translated to
  English labels;
- Figure 2 for the proposed host-level DoH evaluation pipeline;
- Table 1 for the research questions; and
- Table 2 for the controlled evaluation variables.

## Files

- `proposal-doh/main.tex`: two-page LaTeX draft.
- `proposal-doh/build.ps1`: build command.
- `proposal-doh/generate_proposal_figures.py`: figure generator. The TAC-Seq
  figure preserves the thesis layout and changes labels only.
- `proposal-doh/assets/tacseq-framework-en.pdf`: English-label TAC-Seq figure.
- `proposal-doh/assets/doh-host-context-en.pdf`: English-label DoH pipeline.
- `proposal-doh/current-essay-zh-translation.md`: Chinese translation and
  explanation for understanding and interview preparation.
- `proposal-doh/topic-selection.md`: reasoning behind the selected topic.
- `proposal-doh/interview-checklist.md`: knowledge and interview preparation.
- `reference/official-info-science-template.docx`: official reference template
  downloaded from the NAIST application page on 2026-06-01.

## Build

From `proposal-doh`:

```powershell
.\build.ps1
```

The generated `main.pdf` must remain exactly two A4 pages. The build script
uses TeX Live XeLaTeX because the official template header contains Japanese
labels. It also uses TeX Live `pdfinfo` to enforce the two-page requirement.
