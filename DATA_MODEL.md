# Public data model

The public corpus is designed around three distinct objects.

## Source record

A record returned or described by an external source.

```text
SOURCE
 -> SOURCE_RECORD
```

## Canonical work

A project-level bibliographic object constructed only after source comparison.

```text
SOURCE_RECORD_1
SOURCE_RECORD_2
SOURCE_RECORD_3
      ↓
QUALIFIED MATCH
      ↓
CANONICAL_WORK
```

## Relation

A versioned relation between works, records, concepts, people or events.

Examples:

```text
HAS_RECORD
VERSION_OF
REPRINT_OF
TRANSCRIPT_OF
POSTHUMOUS_EDITION_OF
INTRODUCES
USES
EXTENDS
REVISES
POSSIBLE_MATCH
NO_RELATION
```

Public exports must never hide unresolved conflicts by silently collapsing records.
