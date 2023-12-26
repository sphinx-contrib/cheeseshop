import re

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.utils import unescape

from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import split_explicit_title

__version__ = "0.3"
version_info = (0, 3)

# language=HTML
RELEASE_INFO = """\
<div class="release_info {class_}">{prefix}:
<a href="https://pypi.org/pypi/{dist}">latest</a>
</div>
"""

# language=HTML
RELEASE_SCRIPT = """\
<script type="text/javascript">
  $(function() {
    $('.release_info').each(function() {
      var self = this, anchor = $('a', this);
      $.getJSON(anchor.attr('href') + '/json?callback=?', function(data) {
          anchor.remove();
        var ul = $('<ul>').appendTo(self);
        $.each(data.urls, function(url_id) {
          var url=data.urls[url_id];
          var li=$('<li>');
          li.appendTo(ul);
          var a=$('<a>').attr('href', url.url).text(url.filename);
          a.appendTo(li);
        });
      });
    });
  });
</script>
"""


class CheeseShop(SphinxDirective):
    """Directive for embedding "latest release" info in the form of a list of
    release file links.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'prefix': directives.unchanged,
        'class': directives.unchanged,
    }

    def run(self):
        ret = []
        if not self.env.temp_data.get('cheeseshop_script_written'):
            self.env.temp_data['cheeseshop_script_written'] = True
            ret.append(nodes.raw(RELEASE_SCRIPT, RELEASE_SCRIPT, format='html'))
        dist = self.arguments[0]
        prefix = self.options.get('prefix') or 'Download'
        class_ = self.options.get('class') or ''
        html = RELEASE_INFO.format(dist=dist, prefix=prefix, class_=class_)
        ret.append(nodes.raw(html, html, format='html'))
        return ret


def pypi_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for linking to PyPI packages."""

    cheeseshop_url = inliner.document.settings.env.config.cheeseshop_url
    has_explicit, title, target = split_explicit_title(unescape(text))

    # See if an explicit version has been specified with
    # "package-name (version)"
    m = re.match(r'(.*)\s+\((.*?)\)', target)
    if m:
        dist, version = m.groups()
        url = f'{cheeseshop_url}/{dist}/{version}'
        if not has_explicit_title:
            title = f'{dist} {version}'
    else:
        dist = target
        url = f'{cheeseshop_url}/{dist}'

    ref = nodes.reference(rawtext, title, refuri=url)
    return [ref], []


def setup(app):
    app.require_sphinx('4.0')
    app.add_directive('pypi-release', CheeseShop)
    app.add_role('pypi', pypi_role)
    app.add_config_value('cheeseshop_url', 'https://pypi.org/pypi', 'html')
