import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)


@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore


class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    def get_prof_picture(self, path=None):
        """Returns the path of an optional profile picture that users can set

        Args:
            path (str, optional): The path to the profile picture. Defaults to None.

        Returns:
            (str): The profile picture path.
        """
        # setting a profile picture is optional
        if not path:
            pass

        self.__check_safe_path(path)

        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))

        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    def get_tax_form_attachment(self, path=None):
        """Returns the path of an attached tax form that every user should submit

        Args:
            path (str, optional): The path to the tax form. Defaults to None.

        Returns:
            (bytearray): The tax form path.
        """
        if not path:
            raise Exception("Error: Tax form is required for all users")

        self.__check_safe_path(path)

        tax_data = None
        with open(path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that taxa data is returned on screen after this
        return path

    def __check_safe_path(self, path):
        """Defends against path traversal attacks"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.normpath(os.path.join(base_dir, path))

        # If the normalized base dir path is longer than the base_dir,
        # then some sort of traversal happened.
        if base_dir != os.path.commonpath([base_dir, filepath]):
            raise Exception(f"Error: The path {path} is not a safe path.")
