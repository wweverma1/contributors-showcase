# Related third party imports
import pygal
import json


class Chart:

    def generate_chart(response):
        response["contributors"].reverse()
        chart = pygal.HorizontalBar(show_legend=False)
        chart.title = "Contributors' Showcase 🏆"
        chart.x_title = "Commits"
        contributors_list = [contributor["contributions"] for contributor in response["contributors"]]
        chart.add("Contributor", contributors_list)
        chart.x_labels = [contributor["login"] for contributor in response["contributors"]]
        chart.render_to_file('static/images/bar_chart.svg')

