# vOid Community repOsitory
Currently in TESTING mode  
Don't depend on it yet. PRs welcome 🤗
- Void User Repository
- VUR
- testing repo
- waiting list
- void unstable
- by community
- for community

Provides:
- templates
- binaries

## DISCLAIMER

This project is **not affiliated with or endorsed by the Void Linux project** or its maintainers.  
It is an **unofficial community repository** designed to simplify managing and building user-contributed packages using the void-packages build system.  
Use at your own discretion.

## Overview
A collection of template files for building packages on Void Linux.  
If you dont wish to build the packages locally, https://repo.osowoso.org repository provides prebuilt binaries.  
Pick your architecture there and you will see README.

## Structure
- Main repository with templates on Codeberg https://codeberg.org/oSoWoSo/oco
- mirror Github repository + CI https://github.com/oSoWoSo/Void_Community_Repository (Here we build binary packages)
- Binary repository https://repo.osowoso.org/

## How to use
in https://repo.osowoso.org/`(architecture)`  
are easy to understand READMEs  
Just pick your architecture

## How to contribute
Clone Codeberg repo  
`git clone https://codeberg.org/oSoWoSo/oco`  

Add your changes
- When you change any shlib from upstream void-packages, changes my be reflected in `shlibs_remove` and `shlibe_append`
- When you add new shlib add it to `shlibe_append`

After adding template, run `./update-readme` to regenerate templates list and table

Create PR

## Void official documentation
- [Manual](https://github.com/void-linux/void-packages/blob/master/Manual.md)
- [Contributing](https://github.com/void-linux/void-packages/blob/master/CONTRIBUTING.md)
- [Readme](https://github.com/void-linux/void-packages/blob/master/README.md)

## Available templates (packages when built successfully)
| package | version | homepage | maintainer | notes |
|:--------|:--------|:---------|:-----------|:------|
| aquamarine | 0.9.5 | https://github.com/hyprwm/aquamarine | zenobit |  |
| brow6el | 0.3.4 | https://codeberg.org/janantos/brow6el | zenobit |  |
| btrfs-progs | 6.17.1 | https://btrfs.wiki.kernel.org/index.php/Main_Page | Enno Boland |  |
| corekeyboard | 5.0.1 | https://gitlab.com/cubocore/coreapps/corekeyboard | zenobit |  |
| cosmic-applets | 1.0.12 | https://github.com/pop-os/cosmic-applets | Bella Wagner | x86_64* i686 |
| cosmic-applibrary | 1.0.12 | https://github.com/pop-os/cosmic-applibrary | Bella Wagner | x86_64* i686 |
| cosmic-bg | 1.0.12 | https://github.com/pop-os/cosmic-bg | Bella Wagner | x86_64* i686 |
| cosmic-comp | 1.0.12 | https://github.com/pop-os/cosmic-comp | Bella Wagner | x86_64* i686 |
| cosmic-desktop-full | 1.0.12 | https://github.com/pop-os/cosmic-epoch | Bella Viola Wagner | x86_64* |
| cosmic-desktop-minimal | 1.0.12 | https://github.com/pop-os/cosmic-epoch | Bella Wagner | x86_64* |
| cosmic-edit | 1.0.12 | https://github.com/pop-os/cosmic-edit | Bella Wagner | x86_64* |
| cosmic-files | 1.0.12 | https://github.com/pop-os/cosmic-files | Bella Wagner | x86_64* |
| cosmic-greeter | 1.0.12 | https://github.com/pop-os/cosmic-greeter | Bella Wagner | x86_64* i686 |
| cosmic-icons | 1.0.12 | https://github.com/pop-os/cosmic-icons | Bella Wagner |  |
| cosmic-idle | 1.0.12 | https://github.com/pop-os/cosmic-idle | Bella Wagner | x86_64* i686 |
| cosmic-initial-setup | 1.0.12 | https://github.com/pop-os/cosmic-initial-setup | Bella Wagner | x86_64* i686 |
| cosmic-launcher | 1.0.12 | https://github.com/pop-os/cosmic-launcher | Bella Wagner | x86_64* i686 |
| cosmic-notifications | 1.0.12 | https://github.com/pop-os/cosmic-notifications | Bella Wagner | x86_64* i686 |
| cosmic-osd | 1.0.12 | https://github.com/pop-os/cosmic-osd | Bella Wagner | x86_64* i686 |
| cosmic-panel | 1.0.12 | https://github.com/pop-os/cosmic-panel | Bella Wagner | x86_64* i686 |
| cosmic-player | 1.0.12 | https://github.com/pop-os/cosmic-player | Bella Wagner | x86_64* i686 |
| cosmic-randr | 1.0.12 | https://github.com/pop-os/cosmic-randr | Bella Wagner | x86_64* i686 |
| cosmic-screenshot | 1.0.12 | https://github.com/pop-os/cosmic-screenshot | Bella Wagner | x86_64* i686 |
| cosmic-session | 1.0.12 | https://github.com/pop-os/cosmic-session | Bella Wagner | x86_64* i686 |
| cosmic-settings | 1.0.12 | https://github.com/pop-os/cosmic-settings | Bella Wagner | x86_64* i686 |
| cosmic-settings-daemon | 1.0.12 | https://github.com/pop-os/cosmic-settings-daemon | Bella Wagner | x86_64* i686 |
| cosmic-term | 1.0.12 | https://github.com/pop-os/cosmic-term | Bella Wagner | x86_64* |
| cosmic-theme-editor | 0.0.0 | https://github.com/pop-os/cosmic-theme-editor | Bella Wagner | x86_64* i686 |
| cosmic-tweaks | 0.2.2 | https://github.com/cosmic-utils/cosmic-tweaks | Bella Viola Wagner | x86_64 |
| cosmic-wallpapers | 1.0.12 | https://github.com/pop-os/cosmic-wallpapers | Bella Wagner |  |
| cosmic-workspaces-epoch | 1.0.12 | https://github.com/pop-os/cosmic-workspaces-epoch | Bella Wagner | x86_64* i686 |
| desktop-tui | 0.3.2 | https://github.com/Julien-cpsn/desktop-tui | zenobit |  |
| drako | 0.2.10 | https://github.com/lucky7xz/drako | zenobit |  |
| forgejo-runner | 12.10.1 | https://code.forgejo.org/forgejo/runner | zenobit |  |
| gh-lazy | 0.6.4 | https://github.com/gizmo385/gh-lazy | zenobit |  |
| glaze | 6.0.3 | https://github.com/stephenberry/glaze | zenobit |  |
| gofer | 0.2.0 | https://codeberg.org/JakeAtLinux/Gofer | zenobit |  |
| hyprcursor | 0.1.13 | https://github.com/hyprwm/hyprcursor | zenobit |  |
| hyprdynamicmonitors | 1.3.5 | https://github.com/fiffeek/hyprdynamicmonitors | zenobit |  |
| hyprgraphics | 0.3.0 | https://github.com/hyprwm/hyprgraphics | zenobit |  |
| hypridle | 0.1.7 | https://github.com/hyprwm/hypridle | zenobit |  |
| hyprland | 0.52.1 | https://hyprland.org/ | zenobit |  |
| hyprland-devel | 0.52.1 | https://hyprland.org/ | zenobit |  |
| hyprland-guiutils | 0.1.0 | https://github.com/hyprwm/hyprland-guiutils | zenobit |  |
| hyprland-protocols | 0.7.0 | https://github.com/hyprwm/hyprland-protocols | zenobit |  |
| hyprland-qt-support | 0.1.0 | https://github.com/hyprwm/hyprland-qt-support | zenobit |  |
| hyprlang | 0.6.4 | https://github.com/hyprwm/hyprlang | zenobit |  |
| hyprlock | 0.9.2 | https://github.com/hyprwm/hyprlock | zenobit |  |
| hyprpaper | 0.7.6 | https://github.com/hyprwm/hyprpaper | zenobit |  |
| hyprpicker | 0.4.5 | https://github.com/hyprwm/hyprpicker | RAR27 |  |
| hyprpolkitagent | 0.1.3 | https://github.com/hyprwm/hyprpolkitagent | zenobit |  |
| hyprsunset | 0.3.3 | https://github.com/hyprwm/hyprsunset | zenobit |  |
| hyprsysteminfo | 0.1.3 | https://github.com/hyprwm/hyprsysteminfo | zenobit |  |
| hyprtoolkit | 0.3.0 | https://github.com/hyprwm/hyprtoolkit | zenobit |  |
| hyprutils | 0.10.2 | https://github.com/hyprwm/hyprutils | zenobit |  |
| hyprwayland-scanner | 0.4.5 | https://github.com/hyprwm/hyprwayland-scanner | zenobit |  |
| kando | 2.3.0 | https://kando.menu | zenobit | x86_64 aarch64 |
| libcprime | 5.0.1 | https://gitlab.com/cubocore/libcprime | zenobit |  |
| libspng | 0.7.4 | https://libspng.org/ | zenobit |  |
| linuxcommandlibrary | 3.3.1 | http://linuxcommandlibrary.com/ | zenobit |  |
| lunasvg | 3.5.0 | https://github.com/sammycage/lunasvg | zenobit |  |
| ly | 1.1.2 | https://codeberg.org/fairyglade/ly | zenobit | i686 x86_64 |
| menu-themes | 0.8.0 | https://github.com/kando-menu/menu-themes | zenobit |  |
| mesa-amber | 21.3.9 | https://gitlab.freedesktop.org/mesa/mesa/-/blob/amber/docs/relnotes/21.3.9.rst | Bella Viola Wagner |  |
| nebula-gtk | 1.3.7 | https://github.com/Letdown2491/nebula-gtk | zenobit |  |
| pop-fonts | 0.0.0 | https://github.com/pop-os/fonts | Bella Wagner |  |
| pop-icons | 3.5.1 | https://github.com/pop-os/icon-theme | Bella Wagner |  |
| pop-launcher | 1.2.7 | https://github.com/pop-os/launcher | Bella Wagner | x86_64* i686 |
| pop-sounds-theme | 5.5.1 | https://github.com/pop-os/gtk-theme | Bella Wagner |  |
| python3-anysqlite | 0.0.5 | https://github.com/karpetrosyan/anysqlite | zenobit |  |
| python3-hishel | 1.1.9 | https://github.com/karpetrosyan/hishel | zenobit |  |
| python3-inline-snapshot | 0.32.6 | https://15r10nk.github.io/inline-snapshot/latest | zenobit |  |
| python3-linkify-it-py | 2.1.0 | https://github.com/tsutsu3/linkify-it-py | Orphaned |  |
| python3-PyGithub | 2.8.1 | https://pygithub.readthedocs.io/ | Orphan |  |
| python3-textual | 5.3.0 | https://textual.textualize.io | icp |  |
| python3-uc-micro-py | 2.0.0 | https://github.com/tsutsu3/uc.micro-py | Orphaned |  |
| quickemu | 4.9.9 | https://github.com/quickemu-project/quickemu | zenobit |  |
| rgc | 1.1.0 | https://github.com/flameshikari/rgc | zenobit |  |
| runkit | 1.4.0 | https://github.com/Letdown2491/runkit | zenobit |  |
| sdbus-cpp | 2.1.0 | https://github.com/Kistler-Group/sdbus-cpp | zenobit |  |
| shattered-pixel-dungeon | 3.3.8 | https://github.com/00-Evan/shattered-pixel-dungeon | zenobit |  |
| tdf | 0.5.0 | https://github.com/itsjunetime/tdf | zenobit |  |
| tomlplusplus | 3.4.0 | https://marzer.github.io/tomlplusplus/ | zenobit |  |
| vbm | 1.0.1 | https://codeberg.org/oSoWoSo/vbm | zenobit |  |
| Vish | 1.1.2 | https://github.com/Lluciocc/Vish | zenobit |  |
| vtm | 2026.05.01 | https://github.com/directvt/vtm | zenobit |  |
| xdg-desktop-portal-cosmic | 1.0.12 | https://github.com/pop-os/xdg-desktop-portal-cosmic | Bella Wagner | x86_64* |
| xdg-desktop-portal-hyprland | 1.3.11 | https://github.com/hyprwm/xdg-desktop-portal-hyprland | zenobit |  |
| xut | 0.4.2 | https://codeberg.org/mobinmob/xut | mobinmob |  |
| zen-browser-aarch64-bin | 1.19.11b | https://github.com/zen-browser/desktop | Bella Wagner | aarch64 |
| zen-browser-bin | 1.19.11b | https://github.com/zen-browser/desktop | Bella Wagner | x86_64 |
| zig | 0.16.0 | https://ziglang.org | Bella Viola Wagner | x86_64* aarch64* |

Binary repository hosted thanks to [OScloud](https://OScloud.cz)
