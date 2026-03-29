# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Does

OOMLOUT OOMP (Open Optimized Manufacturing Platform) Version 2 is a part classification and data aggregation system. It:

- Pulls part data from configured GitHub source repositories
- Applies utility modules for custom data manipulation and code generation
- Outputs a comprehensive parts catalog (~1,500 parts, 200+ computed fields each) as CSV and Markdown reports to `/report/`

## Commands

**Build (primary):**
```bash
python action_build_oomp.py
python action_build_oomp.py -f warehouse   # build with filter
```

**Profile build performance:**
```bash
python action_build_oomp_time_analysis_wrapper.py
```

There are no test or lint commands — this is a data processing/generation tool.

## Architecture

### Data Flow

1. `action_build_oomp.py` clones/updates `https://github.com/oomlout/oomlout_oomp_builder` into `temporary/oomlout_oomp_builder/`
2. Reads YAML configuration from `configuration/`
3. Delegates to `run.py` in the cloned builder repo
4. Builder pulls part data from source repos, applies utilities, writes outputs to `report/`

### Configuration Layer (`configuration/`)

| File | Purpose |
|------|---------|
| `repos_source_default.yaml` | Source repositories containing part data |
| `utility_source_default.yaml` | Utility repos for processing (code gen, data manipulation, report gen) |
| `filter.yaml` | Which parts to include (`["*"]` = all) |
| `oomlout_oomp_utility_oomlout_generate_report_configuration.yaml` | Defines fields exported to CSV/Markdown |

### External Dependencies

All core build logic lives in the **externalized builder repo** (`oomlout_oomp_builder`), cloned at runtime into `temporary/`. Utility repos are also cloned at runtime. This means:
- The `temporary/` directory is generated — don't edit files there directly
- Changing build behavior means modifying configuration YAML or the external repos
- The builder repo is the authoritative place for aggregation/processing logic

### Output

Reports in `report/` contain computed fields per part including: MD5 hashes, BIP39 word mappings, emoji codes, various case-conversion formats, manufacturer data, and classification hierarchies.
