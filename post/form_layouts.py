from crispy_forms.layout import Layout, Row, Column, Fieldset
from crispy_forms import bootstrap


class TicketFormLayout(Layout):
    """Set layout form of create ticket"""

    def __init__(self):
        super().__init__(Fieldset("Demande de critique sur un Livre / Article", "title", "description"))


class ReviewFormLayout(Layout):
    """Set layout form of create review"""

    def __init__(self):
        super().__init__(
            Fieldset(
                "Publier une  critique sur un Livre / Article",
                Row(
                    Column("headline"),
                    Column(bootstrap.InlineRadios("rating"), css_class="ms-2 p-2 text-center"),
                ),
                Row(Column("body")),
                css_class="border rounded-2 p-3",
            )
        )
