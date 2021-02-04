from src.github import Github


def run_action(
        github_repo: str,
        ignore_branches: list,
        last_commit_age_days: int,
        github_token: str,
        dry_run: bool = True
) -> list:
    print({
        'github_repo': github_repo,
        'ignore_branches': ignore_branches,
        'last_commit_age_days': last_commit_age_days,
        'dry_run': dry_run,
    })

    print(github_token)

    github = Github(github_repo=github_repo, github_token=github_token)

    deleted_branches: list = ['foo']
    branches = github.get_deletable_branches()

    print(branches)

    return deleted_branches
