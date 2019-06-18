import csv

import rope.base.project
from rope.base import libutils
from rope.refactor.move import MoveModule
from rope.refactor.rename import Rename
from rope.refactor.topackage import ModuleToPackage

sdk_generated_path = '../../sdk_generated/'
sdk_path = 'opsgenie_sdk/'


# move each domain api resource into separate package
def move_all_api_modules_to_package():
    print('API modules are moving their own packages.')
    for api_resource in api_resources.get_files():
        if api_resource.name != '__init__.py':
            print('\tfileName: ' + api_resource.name)

            moduleToPackage = ModuleToPackage(project, api_resource)
            changes = moduleToPackage.get_changes()
            project.do(changes)


# rename api module (drop redundant '_api' suffix)
def rename_all_api_modules():
    print('API modules are renaming (drop redundant "_api" suffix).')
    for api_resource in api_resources.get_folders():
        if api_resource.name.endswith('_api'):
            rename = Rename(project, api_resource)
            new_name = rename.get_old_name().split('_api')[0]

            print('\told: ' + api_resource.name + ' new: ' + new_name)

            changes = rename.get_changes(new_name)
            project.do(changes)


# move domain specific models from common model package to related api module
def move_domain_models():
    print('Domain specific models are moving to related api packages.')
    with open(sdk_generated_path + 'opsgenieCodegenModels.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['opsgenieDomain'] != 'common':
                model_resource = libutils.path_to_resource(project,
                                                           sdk_generated_path + sdk_path + 'models/' + row['classFilename'] + '.py',
                                                           'file')
                model_dest_resource = libutils.path_to_resource(project,
                                                                sdk_generated_path + sdk_path + 'api/' + row['opsgenieDomain'],
                                                                'folder')

                if model_resource.exists() and model_dest_resource.exists():
                    print('\tclassname: ' + row["classname"] + ' classFilename: ' + row["classFilename"] + ' opsgenieDomain: ' + row["opsgenieDomain"])

                    moveModule = MoveModule(project, model_resource)
                    changes = moveModule.get_changes(model_dest_resource)
                    project.do(changes)


project = rope.base.project.Project(sdk_generated_path)

api_resources = libutils.path_to_resource(project, sdk_generated_path + sdk_path + 'api', 'folder')

move_all_api_modules_to_package()
rename_all_api_modules()
move_domain_models()

project.close()
