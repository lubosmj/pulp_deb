from pulpcore.plugin import PulpPluginAppConfig


class PulpDebPluginAppConfig(PulpPluginAppConfig):
    """Entry point for the deb plugin."""

    name = "pulp_deb.app"
    label = "deb"
    version = "2.17.0.dev"
