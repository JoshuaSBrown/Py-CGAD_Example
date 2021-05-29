
import argparse
from py_cgad.githubapp import GitHubApp

class PostStatusApp(GitHubApp):

    def __init__(self):
        super().__init__(117711,'StatusApp','lanl','Py-CGAD')


def main(**kwargs):

    app = PostStatusApp()
    app.initialize(pem_file=kwargs['permissions'])
    app.postStatus(kwargs['status'])


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

    args = parser.parse_args()

    main(**vars(args))
