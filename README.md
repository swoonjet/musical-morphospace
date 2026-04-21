# Musical Morphospace

A curiosity-driven agent that explores the space of possible musical *grammars* — not sounds. Each expedition locates a point in an empty region of morphospace, checks it for coherence, and produces two artifacts: an ethnographic field-note document describing the invented system, and a rendered audio specimen demonstrating it.

**The grammar is the artwork. The audio is a specimen.**

**Live site:** [jontoews.com/musical-morphospace](https://jontoews.com/musical-morphospace/)

## What is morphospace?

Every musical tradition on Earth occupies a specific point in a vast abstract space defined by choices about pitch, rhythm, form, texture, function. Gregorian plainchant is one point. Balinese gamelan is another. Delta blues is another. The world's traditions cluster in dense regions — pentatonic scales, duple meter, verse-refrain form. Vast regions remain empty.

This project encodes 84 real-world traditions as points in a 30-dimensional space, then samples unoccupied regions under a coherence constraint and documents what it finds.

## Morphospace schema

30 dimensions = **18 continuous** + **12 categorical**.

- **Continuous** (normalized 0.0–1.0): pitch density, microtonality, octave equivalence, interval hierarchy, pitch flexibility, metric periodicity, rhythmic density, polyrhythmic complexity, cycle length, tempo stability, piece duration, formal repetition, development arc, voice count, voice independence, drone presence, improvisation degree, ornament density.
- **Categorical**: tuning basis, scale topology, rhythmic structure, formal type, texture type, ornament grammar, transmission mode, ensemble topology, social function, listener role, silence treatment, temporal framing.

Hard coherence constraints prevent self-contradictory points (e.g. `non_octave_repeating` cannot coexist with high `octave_equivalence`). See [`schema/schema.json`](schema/schema.json).

## Directory layout

```
musical-morphospace/
├── index.html                   # public landing page
├── schema/
│   └── schema.json              # 30-dim schema + coherence constraints
├── corpus/
│   ├── corpus.json              # 84 traditions encoded
│   ├── corpus-review.html       # visual review dashboard
│   ├── anchors.json             # the 20 calibrating anchors
│   └── build_corpus.py          # builds corpus.json
├── prompts/
│   ├── system.md                # ethnomusicologist voice + output structure
│   ├── expedition_template.md   # per-expedition template
│   ├── audio_spec_schema.json   # JSON schema for section 9
│   └── example_expedition.md    # worked example
├── expeditions/
│   └── example/
│       ├── field_notes.md       # the ethnographic document
│       ├── audio_spec.json      # machine-readable spec
│       ├── audio.wav            # rendered demonstration (75 s)
│       └── index.html           # expedition detail page
├── synthesis/
│   └── engine.py                # audio_spec.json → WAV (numpy additive synth)
├── loop/
│   ├── distance.py              # morphospace distance metric
│   ├── sampler.py               # rejection sampler biased toward empty regions
│   ├── backends.py              # LLM backends (offline / Claude / Ollama)
│   ├── expedition.py            # orchestrator — one expedition end-to-end
│   └── finalize.py              # for offline-mode completion
├── viewer/
│   ├── project.py               # classical MDS → projection.json (pure numpy)
│   ├── projection.json          # 2D coordinates for corpus + expeditions
│   └── index.html               # canvas-based interactive scatter
└── coherence.py                 # hard + soft constraint checker
```

## Running the code

```bash
# Validate the corpus
python3 coherence.py

# Rebuild corpus.json from source
python3 corpus/build_corpus.py

# Render audio from a spec file (JSON or markdown-embedded)
python3 synthesis/engine.py <spec_path> <output.wav> [seed]

# Run one expedition (offline — writes prompt to disk for manual LLM)
python3 -m loop.expedition --backend offline

# Run one expedition (Claude API)
export ANTHROPIC_API_KEY=sk-ant-...
pip install --user --break-system-packages anthropic
python3 -m loop.expedition --backend claude

# Run one expedition (local Ollama)
ollama serve &
ollama pull mistral
python3 -m loop.expedition --backend ollama

# Finalize an offline expedition after pasting LLM response into field_notes.md
python3 -m loop.finalize <expedition_number>

# Regenerate the 2D projection after new expeditions are added
python3 viewer/project.py
```

Requires Python 3 + numpy. Optional: `anthropic` SDK for Claude backend, `requests` for Ollama.

## Synthesis engine capabilities

- **Pitch encodings**: ratio, cents-above-reference, absolute Hz
- **Rhythm systems**: metric, additive, pulse-free, breath-based, cyclical-nonmetric, ritual-cued, indeterminate-proportional
- **Timbres**: sine, vocal (low/high), overtone whistle, bowed string, struck metal, plucked string (Karplus-Strong), reed, breath noise, percussive
- **Voice roles**: sustained drone, ostinato, melodic lead, ornamental, hocket, percussive, ritual punctuation, breath phrase
- **Spatial**: stereo pan per voice
- **Inflection**: per-pitch microtonal wobble rules
- **Form**: multi-section pieces with per-voice active_sections

## Status

Built 2026-04-21. Complete end-to-end pipeline: schema, 84-tradition corpus, prompts, coherence checker, expedition loop (sample → coherence-check → LLM call → render → archive), synthesis engine, and 2D morphospace map all in place. Three LLM backends supported (offline, Claude API, Ollama). Ready to run expeditions.

## Architecture

```
01. sample coordinate     →  30-dim point (continuous + categorical)
02. coherence check       →  reject or pass
03. curiosity score       →  weighted distance from 84 corpus points
04. LLM as field ethnomusicologist  →  field notes + audio spec
05. render audio spec     →  WAV (additive synthesis, spatial voices)
06. archive specimen      →  markdown + json + wav
```

## Credits

Built by [Jon Toews](https://jontoews.com) with [Claude Code](https://claude.com/claude-code).
