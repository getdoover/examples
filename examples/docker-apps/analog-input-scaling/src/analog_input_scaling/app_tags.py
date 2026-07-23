"""Tags produced by the device polling loop."""

from pydoover.tags import Tag, Tags


class AnalogInputScalingAppTags(Tags):
    raw_input = Tag("number", default=None)
    scaled_value = Tag("number", default=None, live=True)
    last_read_at = Tag("string", default=None)
