from crispy_forms.layout import Div, Layout, Row, Column, Fieldset
from crispy_forms import bootstrap


class TicketFormLayout(Layout):
    """Set layout form of create ticket"""

    def __init__(self):
        super().__init__(
            Fieldset(
                "Demande de critique sur un Livre / Article",
                "title",
                "description",
            ),
        )


class ReviewFormLayout(Layout):
    """Set layout form of create reviewwith a new and review ticket"""

    def __init__(self):
        super().__init__(
            Fieldset(
                "Publier une  critique sur un Livre / Article",
                "headline",
                Div(bootstrap.InlineRadios("rating"), css_class="ms-2 p-2 text-center"),
                "body",
            )
        )
