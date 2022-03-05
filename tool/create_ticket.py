import os

from github import Github
import yaml


def main():
    pac = os.environ.get("GITHUB_PAC")
    g = Github(pac)
    repo = g.get_repo("kjmatu/monitor-cam-pi")

    with open("./tickets.yml") as tickets:
        ticket_yaml = yaml.safe_load(tickets)

        for label, tickets in ticket_yaml.items():
            github_label = repo.get_label(label)
            open_issues = repo.get_issues(labels=[github_label], state="open")
            open_issus_titles = [issue.title for issue in open_issues]
            for ticket in tickets:
                if ticket["title"] not in open_issus_titles:
                    repo.create_issue(**ticket, labels=[github_label], assignees=["kjmatu"])


if __name__ == "__main__":
    main()