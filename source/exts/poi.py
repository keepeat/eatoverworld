# -*- encoding:utf-8 -*-
# Author: Taoge

from __future__ import unicode_literals
import os
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from common import get_template
from gaode import Gaode, GDError


class poi_node(nodes.General, nodes.Element):
    pass


class POIDirective(Directive):
    has_content = True
    option_spec = {
        'name': directives.unchanged_required,
        'address': directives.unchanged_required,
        'link': directives.unchanged_required,
        'scene': directives.unchanged_required,
        'recommend': directives.unchanged_required,
    }

    def run(self):
        name = self.options["name"]
        address = self.options["address"]
        link = self.options["link"]
        scene = self.options["scene"]
        recommend = self.options['recommend']
        content = self.content.data
        scenes = scene.split(",")
        recommends = recommend.split(',')

        poi_card = poi_node()

        poi_card.title = name
        poi_card.link = link
        poi_card.scenes = scenes
        poi_card.recommends = recommends
        poi_card.address = address
        poi_card.comment = " ".join(content)
        poi_card.gd_dest_name = name
        poi_card.gd_dest = ''
        gd_key = os.getenv('GD_KEY')
        if gd_key is None:
            raise RuntimeError("GD_KEY required")
        poi_card.gd_key = gd_key
        try:
            poi_card.gd_dest = Gaode.address2dest(address)
        except GDError:
            pass
        return [poi_card]


def visit_poi(self, node):
    template = get_template('poi/poi.html')
    html = template.format(
        title=node.title,
        address=node.address,
        link=node.link,
        scene_list="".join(["<li>{}</li>".format(s) for s in node.scenes]),
        comment=node.comment,
        recommend_list="".join(["<li>{}</li>".format(s) for s in node.recommends]),
        gd_dest_name=node.address,
        gd_key=node.gd_key,
        gd_dest=node.gd_dest,
    )
    self.body.append(html)
    raise nodes.SkipNode


def depart_poi(self, node):
    pass


def setup(app):
    app.add_directive("poi", POIDirective)
    app.add_node(poi_node, html=(visit_poi, None))

    # app.add_node(poi_node, html=(visit_poi, depart_poi))
