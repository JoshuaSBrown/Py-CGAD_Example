
import argparse
from py_cgad.githubapp import GitHubApp

class PostStatusApp(GitHubApp):

    def __init__(self, verbosity_in):
        if isinstance(verbosity_in,list):
            verbosity_in = verbosity_in[0]
        super().__init__(117711,'StatusApp','lanl','Py-CGAD',verbosity=verbosity_in)


def main(**kwargs):

    app = PostStatusApp(kwargs['verbose'])
    app.initialize(pem_file=kwargs['permissions'])
    app.postStatus(kwargs['status'],context="none",description="none",target_url="none")


if __name__ == '__main__':

    parser = argparse.ArgumentParser("Example implementation of Py-CGAD, will post generic message to provided commit hash")

    desc = ('What is the state of the status: success, failed, error, pending')

    parser.add_argument(
            '--status',
            '-s',
            type=str,
            nargs=1,
            required=True,
            help=desc)

    desc = ('Permissions file, allows us to interact with the github repository')

    parser.add_argument(
            '--permissions',
            '-p',
            type=str,
            nargs=1,
            required=True,
            help=desc)

    desc = ('Vebosity of output.')

    parser.add_argument(
            '--verbose',
            '-v',
            type=int,
            nargs=1,
            default=0,
            help=desc)

    args = parser.parse_args()

    main(**vars(args))
