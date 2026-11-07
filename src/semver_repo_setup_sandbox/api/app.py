"""Application FastAPI."""

from fastapi import FastAPI

from semver_repo_setup_sandbox import __version__

app = FastAPI(
    title="Sandbox setup",
    version=__version__,
    description="Dépôt de test du skill semver-repo-setup.",
)


@app.get("/health", tags=["ops"])
def health() -> dict[str, str]:
    """Sonde de vivacité : état et version déployée."""
    return {"status": "ok", "version": __version__}
