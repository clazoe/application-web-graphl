#!/bin/bash
orator migrate -c db.py -f && (cd /graphql-api && uvicorn app.main:app --host 0.0.0.0)