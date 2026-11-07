# AGENTS.md — Sandbox setup

Dépôt de test du skill semver-repo-setup.

<!-- Contexte projet (cahier des charges, fournisseurs, contraintes) : à compléter. -->

## Workflow (obligatoire)

Skills `semver-batch-workflow` et `semver-repo-setup`
(https://github.com/WillIsback/agent-skills). Résumé :

- Une issue typée par changement (`.github/ISSUE_TEMPLATE`) ; epics = issues parentes
  `type:epic`, user stories = sous-issues.
- Lots de version (milestones datés) traités dans l'ordre **patch → minor → major**.
- Branche de lot `<type>/<version>` ; une sous-branche par issue `<type>/<version>-<tâche>`,
  fusionnée dans la branche de lot par `<type>: merge <type>/<version>-<tâche> (#N)`.
- **Jamais de commit ni de merge direct sur `main`** : une PR par lot, avec `Closes #N`
  pour chaque issue.
- Board : https://github.com/users/WillIsback/projects/2 — tenir à jour la
  colonne Status (En cours, Intégré au lot) avec `gh project item-edit`.
- Conventional Commits ; `feat` → minor, `fix`/`perf` → patch, `!` → major.
- Preflight uniquement si la CI de PR ne couvre pas un job de la release.
- Toujours minimiser le temps de CI/CD : ne rien construire deux fois, cacher, filtrer
  par chemins, garder le lourd hors PR.

## Commandes

```bash
uv sync
uv run pytest -m "not integration"
uv run uvicorn semver_repo_setup_sandbox.api.app:app --reload
docker build -t semver-repo-setup-sandbox . && docker run --rm -p 8000:8000 --env-file .env semver-repo-setup-sandbox
```

## Conventions

- Les tests unitaires n'appellent jamais de réseau : simuler. Les tests réels sont
  marqués `integration`.
- Explorer le code avec CodeGraph (`codegraph_explore`) avant grep/lecture.
- Textes, docs, commits et PR en français.
