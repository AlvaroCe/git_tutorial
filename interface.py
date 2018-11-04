"""
Application that opens an UI where two values can be added or substracted.
"""

import Tkinter as tk
import maths


class Application(object):
    """
    User interface
    """
    def __init__(self, root):
        self._master = root
        self._create_widgets()

    def _create_widgets(self):
        """
        """
        tk.Label(master=self._master, text='Argument 1').grid(row=0,
                                                              sticky=tk.W)
        tk.Label(master=self._master, text='Argument 2').grid(row=1,
                                                              sticky=tk.W)

        self.input1 = tk.Entry(master=self._master)
        self.input2 = tk.Entry(master=self._master)

        self.input1.grid(row=0, column=1)
        self.input2.grid(row=1, column=1)

        sum_button = tk.Button(master=self._master, text="SUM",
                               command=self._sum)
        substract_button = tk.Button(master=self._master, text="SUBSTRACT",
                                     command=self._substract)

        sum_button.grid(row=2, column=2)
        substract_button.grid(row=2, column=3)

        self.result_output = tk.Entry(master=self._master)
        self.result_output.grid(row=2, columnspan=2)

    def _sum(self):
        var_1 = float(self.input1.get())
        var_2 = float(self.input2.get())

        result = maths.sum_example(var_1, var_2)
        self.result_output.delete(0, tk.END)
        self.result_output.insert(0, str(result))

    def _substract(self):
        var_1 = float(self.input1.get())
        var_2 = float(self.input2.get())

        result = maths.substract_example(var_1, var_2)
        self.result_output.delete(0, tk.END)
        self.result_output.insert(1, str(result))


def main():
    """
    Start application
    """
    root = tk.Tk()
    root.title('Application example')
    Application(root)
    root.mainloop()

# Create an application instance and run it
if __name__ == "__main__":
    main()
