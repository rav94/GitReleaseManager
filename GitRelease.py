import os
import subprocess

class GitRelease(object):
    def __init__(self, repo_directory_path, release_version_number, new_version_number):
        self.repo_directory_path = repo_directory_path
        self.release_version_number = release_version_number
        self.new_version_number = new_version_number

    def _execute_shell_commands(self, cmd):
        pipe = subprocess.Popen(cmd, shell=True, cwd=self.repo_directory_path, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = pipe.communicate()
        out = out.strip()
        error = error.strip()
        return out, error

    def _set_git_environment(self):
        success, error = False, False
        git_current_branch_cmd = "git branch | grep \*" + " | cut -d ' ' -f2"
        branch_name, branch_check_error = self._execute_shell_commands(git_current_branch_cmd)

        if not branch_check_error:

            if branch_name == "master":
                git_pull_cmd = "git pull"
                git_pull_sucess, git_pull_error = self._execute_shell_commands(git_pull_cmd)

                if not git_pull_error:
                    print("Git Pull Master Success - {}".format(git_pull_sucess))
                    success = git_pull_sucess
                    return success, error

                else:
                    #Pulling lots of changes returns as an error, hence removing the Error=True as command is actually sucesfull
                    print("Git Pull Master Error - {}".format(git_pull_error))
                    success = git_pull_error
                    return success, error

            else:
                git_reset_hard_cmd = "git reset --hard origin/" + branch_name
                git_reset_success, git_reset_error = self._execute_shell_commands(git_reset_hard_cmd)
                
                if not git_reset_error:
                    print("Git Reset Success - {}".format(git_reset_success))
                    git_checkout_cmd = "git checkout master"
                    git_checkout_sucess, git_checkout_error = self._execute_shell_commands(git_checkout_cmd)

                    #Switching to master branch in git checkout gets returned as an error
                    print("Git Checkout Error - {}".format(git_checkout_error))
                    print("Git Checkout Success - {}".format(git_checkout_sucess))

                    git_pull_cmd = "git pull"
                    git_pull_sucess, git_pull_error = self._execute_shell_commands(git_pull_cmd)

                    if not git_pull_error:
                        print("Git Pull Master Success - {}".format(git_pull_sucess))
                        success = git_pull_sucess
                        return success, error

                    else:
                        print("Git Pull Master Error - {}".format(git_pull_error))
                        error = git_pull_error
                        return success, error

                else:
                    print("Git Reset Error - {}".format(git_reset_error))
                    error = git_reset_error
                    return success, error
        
        else:
            print("Git Branch Name Check - {}".format(branch_check_error))
            error = branch_check_error
            return success, error

    def git_release_invoke(self):
        success, error = self._set_git_environment()
        return success, error
        