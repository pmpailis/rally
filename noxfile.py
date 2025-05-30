import nox


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def test(session: nox.Session) -> None:
    session.install(".[develop]")
    session.run("pytest")


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def it(session: nox.Session) -> None:
    session.install(".[develop]")
    session.run("pytest", "-s", "it")


@nox.session(python="3.12")
def it_serverless(session: nox.Session) -> None:
    session.install(".[develop]")
    session.install("pytest-rally @ git+https://github.com/elastic/pytest-rally.git")
    session.run(
        "pytest",
        "-s",
        "it/track_repo_compatibility",
        "--log-cli-level=INFO",
        "--track-repository-test-directory=it_serverless",
        *session.posargs,
    )


@nox.session(python="3")
def rally_tracks_compat(session: nox.Session) -> None:
    session.install(".[develop]")
    session.install("pytest-rally @ git+https://github.com/elastic/pytest-rally.git")
    session.run("pytest", "it/track_repo_compatibility", "--log-cli-level=INFO")
