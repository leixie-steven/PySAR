# grab version / date of the latest commit
import os
import subprocess


def get_release_info(version='v1.1.0-dev', date='2019-04-26'):
    """Grab version and date of the latest commit from a git repository"""
    # go to the repository directory
    dir_orig = os.getcwd()
    os.chdir(os.path.dirname(os.path.dirname(__file__)))

    # grab git info into string
    try:
        version_str = subprocess.check_output(["git", "describe", "--tags"])
        version, num_commit = version_str.decode('utf-8').split('-')[:2]
        version += '-{}'.format(num_commit)

        date_str = subprocess.check_output(["git", "log", "-1", "--date=short", "--format=%cd"])
        date = date_str.decode('utf-8').strip()
    except:
        pass

    # go back to the original directory
    os.chdir(dir_orig)
    return version, date

release_version, release_date = get_release_info()

# generate_from: http://patorjk.com/software/taag/
logo = """
_________________________________________________
       ____             __     __     ____  
       /    )         /    )   / |    /    )
------/____/----------\-------/__|---/___ /------
     /        /   /    \     /   |  /    |  
____/________(___/_(____/___/____|_/_____|_______
                /                           
            (_ /                            

 A Python package for InSAR time series analysis.
           PySAR {v}, {d}
_________________________________________________
""".format(v=release_version, d=release_date)

website = 'https://github.com/insarlab/PySAR'

description = """PySAR release version {v}, release date {d}""".format(v=release_version,
                                                                       d=release_date)
