FROM spaneng/doover_device_base AS base_image

LABEL com.doover.app="true"
LABEL com.doover.managed="true"

# The base image exposes HEALTHCHECK_PORT and runs the app as the `app` user.
HEALTHCHECK --interval=30s --timeout=2s --start-period=5s \
    CMD curl -f "127.0.0.1:$HEALTHCHECK_PORT" || exit 1


# Build dependencies in an isolated environment. Cache mounts keep repeat
# builds quick without copying package-manager caches into the final image.
FROM base_image AS builder

COPY --from=ghcr.io/astral-sh/uv:0.7.3 /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# Reuse libraries provided by doover_device_base and install only the packages
# that are absent. This avoids duplicating large runtime dependencies.
RUN uv venv --system-site-packages
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    SKIP=$(uv pip freeze --system | sed -E 's/[[:space:]@=].*//; s/^/--no-install-package /' | tr '\n' ' ') && \
    uv sync --locked --no-install-project --no-dev $SKIP

COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    SKIP=$(uv pip freeze --system | sed -E 's/[[:space:]@=].*//; s/^/--no-install-package /' | tr '\n' ' ') && \
    uv sync --locked --no-dev $SKIP


# Copy only the ready application environment onto the clean runtime image.
FROM base_image AS final_image

COPY --from=builder --chown=app:app /app /app
ENV PATH="/app/.venv/bin:$PATH"
CMD ["doover-app-run"]
