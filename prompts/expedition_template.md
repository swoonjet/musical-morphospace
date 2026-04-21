# Expedition Template

This template is filled at runtime by the expedition loop. Placeholders in `{{double_curly}}` are substituted with values from the sampled coordinate and the corpus.

---

EXPEDITION #{{expedition_number}}
Date: {{iso_date}}
Morphospace coordinates:
  continuous: {{continuous_vector_json}}
  categorical: {{categorical_vector_json}}
Curiosity score: {{curiosity_score}} (distance from nearest known tradition, weighted)
Coherence check: passed ({{hard_constraints_checked}} hard constraints, {{soft_warnings_triggered}} soft warnings)

## Nearest known traditions

### 1. {{neighbor_1_name}} — distance {{neighbor_1_distance}}
Region: {{neighbor_1_region}}
Summary: {{neighbor_1_notes}}
Key shared parameters with the sampled point: {{neighbor_1_shared}}
Key divergent parameters: {{neighbor_1_divergent}}

### 2. {{neighbor_2_name}} — distance {{neighbor_2_distance}}
Region: {{neighbor_2_region}}
Summary: {{neighbor_2_notes}}
Key shared parameters with the sampled point: {{neighbor_2_shared}}
Key divergent parameters: {{neighbor_2_divergent}}

### 3. {{neighbor_3_name}} — distance {{neighbor_3_distance}}
Region: {{neighbor_3_region}}
Summary: {{neighbor_3_notes}}
Key shared parameters with the sampled point: {{neighbor_3_shared}}
Key divergent parameters: {{neighbor_3_divergent}}

## Parameter hints from coordinates

Continuous (all 0.0–1.0):
{{continuous_dim_table}}

Categorical:
{{categorical_dim_table}}

## Soft warnings (advisory, not constraints)
{{soft_warnings_list}}

## Your task

Document the system that sits at these coordinates — between the listed neighbors but coinciding with none. Follow the section structure defined in your system prompt. The combination of parameters is unusual in the world's musical traditions; your job is to describe the grammar that would make these parameters work together coherently.

Ensure section 9 (AUDIO SPECIFICATION) is fully parameterized per `audio_spec_schema.json` and that every field it declares matches the prose in sections 2–6.

Length target: 500–1,000 words for sections 1–8 and 10 combined. Section 9 is as long as the audio spec requires.
