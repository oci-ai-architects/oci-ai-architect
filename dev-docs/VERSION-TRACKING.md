# OCI AI Architect - Version Tracking

**Last Updated**: 2026-01-06
**Philosophy**: OCI-first, Oracle ecosystem optimized

---

## OCI GenAI Models

| Model | Family | Context | Best For |
|-------|--------|---------|----------|
| **Command R+** | Cohere | 128K | Complex reasoning, RAG, enterprise |
| **Command R** | Cohere | 128K | General purpose chat |
| **Command Light** | Cohere | 4K | High volume, simple tasks |
| **Llama 3.1 70B** | Meta | 128K | Open source, fine-tunable |
| **Llama 3.1 8B** | Meta | 128K | Fast, cost-effective |
| **Llama 3.2** | Meta | 128K | Latest Llama, multimodal |

## OCI Services

| Service | Status | Key Features |
|---------|--------|--------------|
| **OCI GenAI** | GA | Hosted inference, fine-tuning |
| **Dedicated AI Clusters** | GA | Private GPUs, 50 endpoints/cluster |
| **GenAI Agents** | GA | RAG, tools, multi-turn |
| **OCI Search** | GA | Vector search for agents |
| **Oracle ADK** | 1.0 GA | Code-first agent development |
| **Agent Spec** | 1.0 | Framework-agnostic definitions |

## DAC Pricing (January 2026)

| Unit Type | $/Hour | Monthly (730h) |
|-----------|--------|----------------|
| Hosting Unit | ~$2.05 | ~$1,500 |
| Fine-Tuning Unit | ~$5.47 | ~$4,000 |

### Sizing Guide
| Workload | Units | Monthly |
|----------|-------|---------|
| Dev/Test | 2-5 | $3-7.5K |
| Production | 5-15 | $7.5-22K |
| High Volume | 15-30 | $22.5-45K |
| Enterprise | 30-50 | $45-75K |

## OCI-Azure Interconnect

| Feature | Specification |
|---------|---------------|
| Latency | <2ms |
| Bandwidth | Up to 100 Gbps |
| Regions | 12+ paired locations |
| Use Case | GPT access via Azure + OCI backend |

## Oracle MCP Servers

| Server | Purpose |
|--------|---------|
| **Oracle Database MCP** | SQL, PL/SQL, schema tools |
| **Oracle Cloud MCP** | OCI infrastructure tools |

## Embedding Models

| Model | Dimensions | Provider |
|-------|------------|----------|
| **Cohere Embed v3** | 1024 | OCI GenAI |
| **Cohere Embed Multilingual** | 1024 | OCI GenAI |

## SDK Versions

| SDK | Version | Language |
|-----|---------|----------|
| OCI SDK | Latest | Python/Java/Go/TS |
| Oracle ADK | 1.0 | Python |
| OCI CLI | Latest | Bash |

---

## Update Checklist

When OCI releases updates:
- [ ] Check OCI Console for new models
- [ ] Update this file
- [ ] Update skill `external_version` fields
- [ ] Update CLAUDE.md quick reference
- [ ] Check Oracle blogs for announcements

## Sources

- [OCI GenAI Documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/overview.htm)
- [Dedicated AI Clusters](https://docs.oracle.com/en-us/iaas/Content/generative-ai/ai-cluster.htm)
- [OCI GenAI Agents](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Oracle ADK](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/adk/)
- [Oracle MCP Servers](https://github.com/oracle/mcp-servers)

---
*Review monthly or after Oracle announcements*
