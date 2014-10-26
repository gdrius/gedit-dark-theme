from gi.repository import GObject, Gedit, Gtk


class DarkThemePlugin(GObject.Object, Gedit.AppActivatable):

    __gtype_name__ = 'DarkThemePlugin'
    app = GObject.property(type=Gedit.App)

    def __init__(self):
        GObject.Object.__init__(self)
        self._dark_theme_default = None

    def do_activate(self):
        settings = Gtk.Settings.get_default()
        self._dark_theme_default = settings.get_property(
                                        'gtk-application-prefer-dark-theme')
        settings.set_property('gtk-application-prefer-dark-theme', True)

    def do_deactivate(self):
        settings = Gtk.Settings.get_default()
        if self._dark_theme_default is None:
            self._dark_theme_default = False
        settings.set_property('gtk-application-prefer-dark-theme',
                              self._dark_theme_default)
