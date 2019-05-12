import os
import subprocess

class GitRelease(object):
    def __init__(self, path, release_version_number):
        self.path = path
        self.release_version_number = release_version_number

    def test(self):
        my_quote = self.path
        my_release = self.release_version_number
        return my_quote, my_release

    '''
    def set_git_environment(self):
        # cd to the git repo path -> Handle error if the path is not found
        # Check the git branch
        # If not master, run git reset --hard origin/current_branch
        # Git checkout master
    '''

    def git_checkout_master(self):
        subprocess.run(["git", "checkout", "master"])

    '''
    def git_release(self):
        # Run the release process
    '''