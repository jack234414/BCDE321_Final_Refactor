import unittest
from unittest.mock import patch
from main import CommandLineInterface


class TestMyPlot(unittest.TestCase):

    @patch('builtins.print')
    def test_load_data(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.do_load_data("JSTest1.js")
        expected = mock_print.assert_called_with("The current directory is: \nYour selected js file is: JSTest1.js")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_load_data(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_load_data()
        expected = mock_print.assert_called_with('Loads data from a provided Javascript file \nSyntax: load_data '
                                                 '[file path]')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_load_data_typing_wrong(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.do_load_data("JSTest1")
        expected = mock_print.assert_called_with('You did not input any path'
                                                 ' or your input file is not existed')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_load_data_wrong_filetype(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.do_load_data("jsNotExist.js")
        expected = mock_print.assert_called_with('You did not input any path or your input file is not existed')
        self.assertEqual(expected, actual)

    def test_exit(self):
        cmd = CommandLineInterface()
        actual = cmd.do_exit(None)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_exit(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_exit()
        expected = mock_print.assert_called_with('Exits the program \nSyntax: exit')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_db_table_select(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_db_table_select()
        expected = mock_print.assert_called_with("To select a table you want to see with stored data \nSyntax: table_select [-options] \nOptions: \n -a: Select attributes table \n -m: Select methods table \n -c: Select all extracted class table")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_validate_data_class_table(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        actual = cmd.do_validate_data("-c")
        expected = mock_print.assert_called_with([[1, 'CycleLog'], [2, 'Ride']])
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_validate_data_method_table(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        actual = cmd.do_validate_data("-m")
        expected = mock_print.assert_called_with([[1, 1, 'constructor'], [2, 1, 'addRide'], [3, 1, 'sortRides'], [4, 1, 'getShortRides'], [5, 1, 'getLongRides'], [6, 1, 'getRideBetweenDate'], [7, 1, 'removeRide'], [8, 1, 'save'], [9, 1, 'load'], [10, 1, 'startEdit'], [11, 1, 'doneEdit'], [12, 1, 'cancelEdit'], [13, 1, 'calculateTotalDistance'], [14, 1, 'calculateAverageKPH'], [15, 1, 'findRideTitle'], [16, 1, 'getAllRides'], [17, 2, 'constructor'], [18, 2, 'finishedRide'], [19, 2, 'calculateDuration'], [20, 2, 'calculateKPH']])
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_validate_data_attr_table(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        actual = cmd.do_validate_data("-a")
        expected = mock_print.assert_called_with([[1, 1, 'this.allMyRides=[]'], [2, 1, 'this.editedRide=null'], [3, 1, 'this.editedRideIndex=null'], [4, 1, 'this.beforeEditTitleCache=""'], [5, 1, 'this.beforeEditDistanceCache=""'], [6, 1, 'this.beforeEditDurationCache=""'], [7, 2, 'this.title=newTitle'], [8, 2, 'this.id=newId'], [9, 2, 'this.date=newDate'], [10, 2, 'this.duration=newDuration'], [11, 2, 'this.distance=newDistance'], [12, 2, 'this.kph=newKPH'], [13, 2, 'this.completed=false']])
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_extract_data(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_extract_data()
        expected = mock_print.assert_called_with('Extracts data from loaded'
                                                 ' JavaScript file '
                                                 '\nSyntax: extract_data')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_convert_to_uml(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_convert_to_uml()
        expected = mock_print.assert_called_with('Converts extracted data '
                                                 'and displays image '
                                                 '\nSyntax: convert_to_uml')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_convert_to_uml(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        cmd.do_extract_data(None)
        actual = cmd.do_convert_to_uml(None)
        expected = mock_print.assert_called_with("Data has been extracted")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_draw_diagram_wrong_arg(self, mock_print):
        arg = ""
        cmd = CommandLineInterface()
        actual = cmd.do_draw_chart(arg)
        expected = mock_print.assert_called_with('Please at the least entre 1 argument as an option. Try again !')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_draw_diagram(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        actual = cmd.do_draw_chart("-b")
        expected = mock_print.assert_called_with('Query "SELECT * from uml_resource.all_class;" processed!')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()