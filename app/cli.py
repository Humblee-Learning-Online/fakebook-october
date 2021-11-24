import click, os

def register(app):
    @app.cli.group()
    def blueprint():
        """Blueprint creation commands."""
        pass

    @blueprint.command()
    @click.argument('name')
    def create(name):
        """Create new Flask Blueprint"""
        basepath = os.path.abspath(os.path.dirname(__name__)) + f'/app/blueprints/{name}'

        try:
            # check if the basepath + the blueprint folder name exists
            if not os.path.exists(basepath):
                os.makedirs(basepath)
                init_file = open(f'{basepath}/__init__.py', 'w')
                init_file.close()
                routes_file = open(f'{basepath}/routes.py', 'w')
                routes_file.close()
                models_file = open(f'{basepath}/models.py', 'w')
                models_file.close()
            print('Blueprint created successfully')
        except Exception as error:
            print(f"Something went wrong with creating your blueprint called {name}.")
            print(error)