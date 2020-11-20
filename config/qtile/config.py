from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.config import EzKey
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keymap = {
    'M-h': lazy.layout.left(),
    'M-j': lazy.layout.down(),
    'M-k': lazy.layout.up(),
    'M-l': lazy.layout.right(),
    'M-S-h': lazy.layout.move_left(),
    'M-S-j': lazy.layout.move_down(),
    'M-S-k': lazy.layout.move_up(),
    'M-S-l': lazy.layout.move_right(),
    'M-A-h': lazy.layout.integrate_left(),
    'M-A-j': lazy.layout.integrate_down(),
    'M-A-k': lazy.layout.integrate_up(),
    'M-A-l': lazy.layout.integrate_right(),
    'M-d': lazy.layout.mode_horizontal(),
    'M-v': lazy.layout.mode_vertical(),
    'M-S-d': lazy.layout.mode_horizontal_split(),
    'M-S-v': lazy.layout.mode_vertical_split(),
    'M-a': lazy.layout.grow_width(30),
    'M-x': lazy.layout.grow_width(-30),
    'M-S-a': lazy.layout.grow_height(30),
    'M-S-x': lazy.layout.grow_height(-30),
    'M-n': lazy.layout.reset_size(),

    'M-w': lazy.window.kill(),
    'M-<Tab>': lazy.next_layout(),
    'M-<Return>': lazy.spawn(terminal),
    'M-r': lazy.spawn("rofi -show run"),
    'M-C-r': lazy.restart(),
    'M-C-q': lazy.shutdown(),
}

keys = [EzKey(k, v) for k, v in keymap.items()]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

from plasma import Plasma

layouts = [
    Plasma(
        border_normal='#333333',
        border_focus='#00e891',
        border_normal_fixed='#006863',
        border_focus_fixed='#00e8dc',
        border_width=1,
        border_width_single=0,
        margin=5
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=13,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method = "line",
                    rounded = False,
                    ),
                widget.Prompt(),
                widget.Spacer(),
                widget.Systray(),
                widget.Battery(format = '{percent:2.0%}'),
                widget.Clock(format = '%d/%m/%Y %H:%M'),
            ],
            24,
            opacity=0.8,
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
