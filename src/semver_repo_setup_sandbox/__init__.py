"""Sandbox setup — Dépôt de test du skill semver-repo-setup."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("semver-repo-setup-sandbox")
except PackageNotFoundError:  # pragma: no cover - paquet non installé
    __version__ = "0.0.0"
