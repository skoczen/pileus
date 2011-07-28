from qi_toolkit.fabbase import *

setup_env_centos("pileus","root",
                initial_settings={
                    'staging_hosts':['digitalmycelium.com'],
                    'production_hosts':[
                                '50.16.217.71',
                                '50.16.206.163',
                                       ],
                    'production_db_hosts':['ext-mysql.agoodcloud.com'],
                    'staging_db_hosts':['ext-mysql.digitalmycelium.com'],
                    'admin_symlink' : '_admin',
                    'python_version': '2.7',
                }, 
                overrides={
                    'git_origin':"git@github.com:skoczen/pileus.git",
                    # 'dry_run':True,
                    'local_working_path':"~/workingCopy/goodcloud",
                    "staging_virtualenv_name": "pileus",
                },
                )



def dump_marketing_fixture():
    magic_run("%(work_on)s cd %(project_name)s; %(python)s manage.py dumpdata --natural --indent 4 --exclude=contenttypes marketing_site cms mptt menus text  > %(git_path)s/%(project_name)s/apps/marketing_site/fixtures/marketing_site.json")


def repopulate_search_caches():
    magic_run("%(work_on)s cd %(project_name)s; %(python)s manage.py repopulate_search_caches")

def backup_db():
    magic_run("backup perform --trigger %(project_name)s")