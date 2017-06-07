# -*- encoding:utf-8 -*-
# Author: Taoge


from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import Directive, directives


class poi_node(nodes.General, nodes.Element):
    pass


class POIDirective(Directive):
    has_content = True
    option_spec = {
        'name': directives.unchanged_required,
        'address': directives.unchanged_required,
        'link': directives.unchanged_required,
        'scene': directives.unchanged_required,
        'recommend': directives.unchanged_required
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

        return [poi_card]


def visit_poi(self, node):
    html = POI_CARD_TEMPLATE.format(
        title=node.title,
        address=node.address,
        link=node.link,
        scene_list="".join(["<li>{}</li>".format(s) for s in node.scenes]),
        comment=node.comment,
        recommend_list="".join(["<li>{}</li>".format(s) for s in node.recommends])
    )
    self.body.append(html)
    raise nodes.SkipNode


def depart_poi(self, node):
    pass


def setup(app):
    app.add_directive("poi", POIDirective)
    app.add_node(poi_node, html=(visit_poi, None))

    # app.add_node(poi_node, html=(visit_poi, depart_poi))


POI_CARD_TEMPLATE = """


      <div class="row">
        <div class="col s12 m6">
          <div class="card white">
            <div class="card-content black-text">
              <span class="card-title">{title}</span>
              <p>{comment}</p>
              <div>
              <span>场景: </span>
                {scene_list}
              </div>
              <div>
              <span>推荐菜: </span>
                {recommend_list}
              </div>
              <p>地址: <i> {address}</i> </p>

            </div>
            <div class="card-action">
              <a href="{link}">Details</a>
            </div>
          </div>
        </div>
      </div>

"""
