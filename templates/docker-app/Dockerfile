FROM spaneng/doover_device_base

LABEL com.doover.app="true"
LABEL com.doover.managed="true"
HEALTHCHECK --interval=30s --timeout=2s --start-period=5s \
    CMD curl -f "127.0.0.1:$HEALTHCHECK_PORT" || exit 1

COPY --from=ghcr.io/astral-sh/uv:0.7.3 /uv /bin/uv
WORKDIR /app
COPY . .
RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"
CMD ["doover-app-run"]
