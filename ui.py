import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton
class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1,self).__init__('Simple example 1')

        #Definition of the forms fields
        self._firstname     = ControlText('Senetence', 'Default value')

        self._button        = ControlButton('Press this button')


#Execute the application
if __name__ == "__main__":
    pyforms.start_app( SimpleExample1 )