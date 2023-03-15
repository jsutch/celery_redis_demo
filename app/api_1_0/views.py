@api.route('/updateManifest')
@login_required
def updateManifest():
    async_run_get_manifest()
    return render_template('index.html',
                            site_details    = site_details,
                            ) 
