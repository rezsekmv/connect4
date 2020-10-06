from restapi import *

def main():

    app, api = init_api()
    add_resources(api)
    run_api(app)

main()
