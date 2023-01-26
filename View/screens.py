# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
}