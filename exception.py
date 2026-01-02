import sys

def error_message_detail(error, detail:sys):
    _, _, exc_tb = detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    err_msg = f"Error occurred in file: {file_name}, line number: {line_number}, error message: {str(error)}"
    
    return err_msg
    
    
class CustomError(Exception):
    """A custom exception class for specific error handling."""
    def __init__(self, err_message, detail:sys):
        super().__init__(err_message)
        self.err_message = error_message_detail(err_message, detail)

    def __str__(self):
        return f"CustomError: {self.err_message}"