# Sandbox setup

Dépôt de test du skill semver-repo-setup.

## Démarrage rapide

```bash
cp .env.example .env
uv sync
uv run pytest -m "not integration"
uv run uvicorn semver_repo_setup_sandbox.api.app:app --reload
docker build -t semver-repo-setup-sandbox . && docker run --rm -p 8000:8000 --env-file .env semver-repo-setup-sandbox
```

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md) (workflow par lots de version, gates de CI,
release) et le [board](https://github.com/users/WillIsback/projects/2).

## Licence

MIT — William Derue.
