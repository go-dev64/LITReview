from crispy_forms.layout import Layout, Row, Column, Fieldset, Field


class TicketFormLayout(Layout):
    """Set layout form of create ticket"""

    def __init__(self):
        super().__init__(Fieldset())


class ReviewFormLayout(Layout):
    """Set layout form of create review"""

    def __init__(self):
        super().__init__()
