#!/usr/bin/env python3
"""tier_classify.py — shared office-tier classifier + rubric helpers for v5.0.

Single source of truth for federal/state/local classification and the
per-tier rubric (which categories count, and their pillar). Imported by
generate-profiles.py and build-search-index.py so card scores and profile
scores never diverge.
"""
import re


def classify_office_tier(c):
    """Return 'federal' | 'state' | 'local' for a candidate based on office.
    (Extracted from generate-profiles.py 2026-05-21 for v5.0 — keep behavior
    identical to the profile generator.)"""
    office = c.get('office') or ''
    if not office:
        jur = (c.get('jurisdiction') or '').lower()
        if 'executive branch' in jur or 'judicial branch' in jur:
            return 'federal'
        return 'state'
    o = office.lower()
    if re.search(r'\b(president|vice president|u\.?s\.?\s+sen|u\.?s\.?\s+hous|u\.?s\.?\s+rep|'
                 r'united states sen|united states hous|united states rep|secretary of|'
                 r'acting attorney general|attorney general of the united states|'
                 r'director of|administrator of|ambassador|chief of staff|deputy chief of staff|'
                 r'homeland security advisor|chief justice|associate justice.+supreme court|'
                 r'special envoy)', o):
        if re.search(r'^attorney general$|state attorney general', o) and 'united states' not in o:
            return 'state'
        return 'federal'
    if re.search(r'\bgovernor\b|^lt\.?\s+governor|lieutenant governor|'
                 r'state senator|state senate|state representative|state hous|'
                 r'state assembl|^delegate$|delegate \(|house of delegates', o):
        return 'state'
    if re.search(r'^attorney general$|secretary of state$|state treasurer|state auditor|'
                 r'state comptroller', o):
        return 'state'
    if 'state supreme court' in o or re.search(r'(chief justice|justice).+state', o):
        return 'state'
    if re.search(r'\bmayor\b|city council|town council|borough council|'
                 r'county (commissioner|supervisor|judge|board)|'
                 r'school board|board of education|'
                 r'district attorney|sheriff|city clerk|city attorney|'
                 r'commonwealth\'?s attorney', o):
        return 'local'
    return 'state'


def category_in_tier(cat, tier):
    """True if this category belongs to the given tier's rubric.
    Categories carry a `pillars` map ({tier: pillar_key}); absence of `pillars`
    (legacy) defaults to 'in every tier' for back-compat."""
    pillars = cat.get('pillars')
    if pillars is None:
        return True
    return tier in pillars


def category_pillar(cat, tier):
    """Return the pillar key ('god_first' | 'america_first' | 'state_first' |
    'local_first') for this category at the given tier, or None if not in the
    tier's rubric. Falls back to the legacy `tier` field for federal."""
    pillars = cat.get('pillars') or {}
    pill = pillars.get(tier)
    if pill is None and tier == 'federal':
        return cat.get('tier')
    return pill
