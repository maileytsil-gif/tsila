#!/usr/bin/env python3
"""Create an evidence-based retrospective from one production session JSON.
Never edits a Live project, bridge, or approval state.
"""
import argparse
import json
import pathlib
import sys

FIELDS = {'session_id', 'project_copy', 'bridge_version', 'bridge_commands', 'renders', 'listening', 'user_feedback', 'errors'}


def review(record):
    if not isinstance(record, dict) or not record.get('session_id'):
        raise ValueError('session_id is required')
    errors = record.get('errors', [])
    if not isinstance(errors, list): raise ValueError('errors must be a list')
    for key in ('bridge_commands', 'renders', 'listening'):
        if key in record and not isinstance(record[key], list):raise ValueError(key+' must be a list')
    evidence = bool(record.get('renders')) and bool(record.get('listening'))
    completed = evidence and not errors
    suggestions = []
    if errors:
        suggestions.append({'priority':'high','action':'Classify each bridge error; reproduce on a copy with a regression test before editing code.'})
    if not record.get('renders'):
        suggestions.append({'priority':'high','action':'Create a render and reimport it before assessing the produced music.'})
    if not record.get('listening'):
        suggestions.append({'priority':'high','action':'Record actual listening conditions (headphones/mono/speakers) and observations.'})
    if completed and record.get('user_feedback') == 'approved':
        suggestions.append({'priority':'normal','action':'Extract one reusable successful procedure into the Codex skill and test it against a second song; avoid changing the Live bridge without a reason.'})
    return {'session_id':record['session_id'],'quality_gate':'evidence_present' if completed else 'incomplete',
            'artist_approved':record.get('user_feedback')=='approved',
            'automatic_code_change':False,'suggestions':suggestions,
            'verification':'The session log alone does not prove audio quality; listen to renders and compare Live state.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('session_json');p.add_argument('--output');a=p.parse_args()
    record=json.loads(pathlib.Path(a.session_json).read_text())
    if not isinstance(record,dict):raise ValueError('root must be object')
    report=review(record)
    result=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
    if a.output:pathlib.Path(a.output).write_text(result)
    else:sys.stdout.write(result)

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,json.JSONDecodeError) as exc:
        print(json.dumps({'ok':False,'error':str(exc)}),file=sys.stderr);raise SystemExit(1)
