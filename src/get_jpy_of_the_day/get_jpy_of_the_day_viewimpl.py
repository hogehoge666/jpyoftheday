import click

class GetJpyOfTheDayViewImpl:
    def generate_view(self, view_model:dict):
        style_requested_date = click.style(
            f"{view_model['requested_date']} {view_model['requested_day_of_the_week']}",
            fg="blue"
        )
        click.secho(f"Requested Date:\t{style_requested_date}", fg="blue")
        if view_model["retrieved_date"] != view_model["requested_date"]:
            click.secho("  Market might have been closed at the requested date.", fg="red")
            click.secho("  Here is the data from the nearest open day.", fg="red")
            style_retrieved_date = click.style(
                f"{view_model['retrieved_date']} {view_model['retrieved_day_of_the_week']}",
                fg="blue"
            )
            click.secho(f"Retrieved Date:\t{style_retrieved_date}", fg="blue")
        click.secho(f"Closing Price:\t{view_model['price']}", fg="green")
