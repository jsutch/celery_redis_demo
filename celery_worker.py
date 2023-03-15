import os
from app import celery, create_app
 
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()

@celery.task(name='tasks.async_run_get_manifest')
def run_get_manifest():
    """ Run the entire get_manifest flow as a single function """
    build_path()
    manifest_version = request_manifest_version()
    if check_manifest(manifest_version) is True:
        getManifest()
        buildTable()
        manifest_type = "full"
        all_data = buildDict(DB_HASH)
        writeManifest(all_data, manifest_type)
        cleanUp()
    else:
        print("No change detected!")

    return


def async_run_get_manifest():
    """ Asynchronous task, called from API endpoint. """
    run_get_manifest.delay()
    return

@periodic_task(run_every=timedelta(seconds=300))
def periodic_run_get_manifest():
    """ Perodic task, run by Celery Beat process """
    run_get_manifest()
    return


