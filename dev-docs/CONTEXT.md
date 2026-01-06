# Project Context

Persistent context that survives conversation resets.

## Project Overview

**OCI AI Architect** - Specialized toolkit for Oracle Cloud Infrastructure AI solutions including GenAI Services, Dedicated AI Clusters, and Oracle ADK.

## Key Components

### Skills (6 OCI-focused)
- **oci-services-expert**: All OCI AI services (Vision, Speech, Language, Document Understanding)
- **genai-dac-specialist**: DAC deployment and operations
- **oracle-adk**: Agent Development Kit patterns
- **oracle-agent-spec**: Open Agent Specification
- **rag-expert**: RAG patterns for OCI GenAI Agents
- **mcp-architecture**: MCP integration with Oracle servers

### Knowledge Base
- OCI GenAI documentation
- Dedicated AI Clusters guides
- OCI-Azure Interconnect patterns

### Templates
- D2 architecture diagrams (OCI-specific)
- Terraform modules for OCI GenAI

## Repository Structure

```
oci-ai-architect/
├── CLAUDE.md           # Main instructions
├── skills/             # 6 OCI-focused skills
├── knowledge-base/     # OCI reference documentation
├── templates/          # D2, Terraform (OCI)
├── dev-docs/           # Persistent dev context
└── .claude/            # Hooks, commands, settings
```

## Recent Changes

| Date | Change | Impact |
|------|--------|--------|
| 2026-01-06 | Updated all 6 skills to v1.1.0 | Added last_updated, external_version |
| 2026-01-06 | Created VERSION-TRACKING.md | Centralized OCI version management |
| 2026-01-06 | Added /update-knowledge command | Automated knowledge refresh |

## Related Repositories

- **ai-architect**: Vendor-neutral, best-of-breed multi-cloud
- GitHub: frankxai/ai-architect

## OCI Regions with GenAI

| Region | Availability |
|--------|--------------|
| US Midwest (Chicago) | DAC, On-Demand |
| UK South (London) | DAC, On-Demand |
| Germany Central (Frankfurt) | DAC, On-Demand |

---
*Update this file when major context changes occur*
