import subprocess
from pathlib import Path

from indexer.config import settings
from indexer.logger import logger


def ensure_repo() -> tuple[Path, str]:
    repo_dir = Path(settings.git_sources_dir)
    repo_dir.mkdir(parents=True, exist_ok=True)

    git_dir = repo_dir / ".git"

    if not settings.git_repo_url:
        logger.info("No git repo URL configured, using local sources at %s", repo_dir)
        if git_dir.exists():
            result = subprocess.run(
                ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            )
            commit_hash = result.stdout.strip()
        else:
            commit_hash = "local"
        logger.info("Current commit: %s", commit_hash)
        return repo_dir, commit_hash

    if git_dir.exists():
        logger.info("Repository exists at %s, pulling latest changes...", repo_dir)
        subprocess.run(
            ["git", "-C", str(repo_dir), "fetch", "origin"],
            check=True,
        )
        subprocess.run(
            ["git", "-C", str(repo_dir), "reset", "--hard", f"origin/{settings.git_branch}"],
            check=True,
        )
    else:
        logger.info("Cloning %s into %s", settings.git_repo_url, repo_dir)
        subprocess.run(
            [
                "git",
                "clone",
                "--branch",
                settings.git_branch,
                "--single-branch",
                settings.git_repo_url,
                str(repo_dir),
            ],
            check=True,
        )

    result = subprocess.run(
        ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    commit_hash = result.stdout.strip()
    logger.info("Current commit: %s", commit_hash)
    return repo_dir, commit_hash
