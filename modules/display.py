from rich.table import Table
from rich.console import Console

console = Console()


def show_results(data: dict):

    table = Table(
        title="Instagram Intelligence Report"
    )

    table.add_column(
        "Field",
        style="cyan",
        no_wrap=True
    )

    table.add_column(
        "Value",
        style="green"
    )

    profile = data.get(
        "profile",
        {}
    )

    stats = data.get(
        "profile_stats",
        {}
    )

    metadata = data.get(
        "metadata",
        {}
    )

    score = data.get(
        "intelligence_score",
        {}
    )

    table.add_row(
        "Username",
        str(
            profile.get(
                "username",
                "N/A"
            )
        )
    )

    table.add_row(
        "Reachable",
        str(
            profile.get(
                "reachable",
                False
            )
        )
    )

    table.add_row(
        "Followers",
        str(
            stats.get(
                "followers",
                "N/A"
            )
        )
    )

    table.add_row(
        "Following",
        str(
            stats.get(
                "following",
                "N/A"
            )
        )
    )

    table.add_row(
        "Posts",
        str(
            stats.get(
                "posts",
                "N/A"
            )
        )
    )

    table.add_row(
        "Bio",
        str(
            metadata.get(
                "bio",
                "Not Found"
            )
        )
    )

    table.add_row(
        "Intel Score",
        str(
            score.get(
                "score",
                0
            )
        )
    )

    console.print(
        table
    )
