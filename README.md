# Doover Examples

Minimal starting points and focused working examples for custom Doover
applications. Every project is self-contained and can be copied into its own
repository.

## Starting templates

| App type | When to use it | Template |
| --- | --- | --- |
| Processor | Empty config/tags/UI classes and stubbed processor event hooks. | [Processor template](templates/processor/) |
| Integration | Empty tags/UI, ingestion configuration, and stubbed integration hooks. | [Integration template](templates/integration/) |
| Docker app | Empty config/tags/UI classes and stubbed loop/event/shutdown hooks. | [Docker app template](templates/docker-app/) |
| Report generator | Produce downloadable JSON reports from Doover data. | [Report generator template](templates/report-generator/) |
| Widget | Build a custom JavaScript/TypeScript user interface. | Planned |
| Multi-format app | Ship more than one cooperating app type from a repository. | Planned |

## Quick start

Copy the closest minimal template, then add only the pieces your app needs:

```bash
cp -R templates/processor ../my-processor
cd ../my-processor
uv sync
uv run pytest
```

Every Python template follows the same broad layout:

```text
template/
├── README.md
├── doover_config.json
├── pyproject.toml
├── src/<package>/
└── tests/
```

The processor, integration, and report generator templates include `build.sh`
for Lambda packaging. The Docker template includes the smallest usable
`Dockerfile`.

## Custom examples

Examples add one complete behaviour at a time and are intentionally more
opinionated than the templates.

| App type | Example | What it demonstrates |
| --- | --- | --- |
| Processor | [On message processing](examples/processors/on-message-processing/) | Subscription config, validation, tags, UI, calibration, and connection status |
| Integration | [Webhook routing](examples/integrations/webhook-routing/) | Ingestion decoding, validation, auditing, permissions, and agent routing |
| Docker app | [Analog input scaling](examples/docker-apps/analog-input-scaling/) | Hardware polling, linear scaling, tags, dynamic UI, and safe shutdown |
| Device widget | [Tag values](examples/device-widget-tag-values/) | Processor-backed interpreter UI, device-local channel access, tag flattening, and filtering |

## Template lineage

The first custom examples are small, vendor-neutral adaptations of working
Doover applications:

- The processor and integration patterns come from
  [getdoover/digital_matter](https://github.com/getdoover/digital_matter).
- The Docker/device pattern comes from
  [getdoover/analog-level-sensor](https://github.com/getdoover/analog-level-sensor).
- The report generator pattern comes from Doover's JSON report generator.

The original projects contain their full production business logic. The custom
examples retain one useful vertical slice; the templates deliberately omit that
logic.

## Adding another template

Keep template classes and handlers empty, but retain the conventional file
structure so users can immediately see where configuration, tags, UI, and
lifecycle logic belong. Put actual protocols and business logic into focused
custom examples instead. Each project should stay independently installable and
testable and be added to the CI matrix below.
