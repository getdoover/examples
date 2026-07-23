"""Tags published by the processor and consumed by its UI or peer apps."""

from pydoover.tags import Tag, Tags


class OnMessageProcessingTags(Tags):
    # `live=True` is useful for the primary rapidly changing value.
    measurement = Tag("number", default=None, live=True)
    status = Tag("string", default="unknown")
    source_time = Tag("string", default=None)
    last_processed_at = Tag("string", default=None)
