from py_cgad.githubapp import GitHubApp
import os


class StatusApp(GitHubApp):
    def __init__(self, verbosity_in=0):
        """Status app uploads, status for a commit, can also retrieve"""
        if isinstance(verbosity_in, list):
            verbosity_in = verbosity_in[0]
        super().__init__(
            117711,
            "StatusApp",
            "JoshuaSBrown",
            "PyCGADExample",
            os.path.abspath(__file__),
            verbosity=verbosity_in,
        )
