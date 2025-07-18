from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.default.items = [["Yes",0],["No",1]]
    self.homeownership.items = [["Rent",2],["Own",1]["Mortgage",0]]
    # Any code you write here will run before the form opens.

  def submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    loan_status = anvil.server.call('classify_loan',
                                   int(self.loan_amount.text),
                                   int(self.income.text),
                                   int(self.default.text),
                                   int(self.homeownership.text)
                                   )
    if loan_status:
      self.loan_status.visible = True
      self.loan_status.text = "Applicant is " + loan_status.capitalize()
    
