# Void-User-Repository

## DISCLAIMER

This project is **not affiliated with or endorsed by the Void Linux project** or its maintainers.
It is an **unofficial community tool** designed to simplify managing and building user-contributed packages using the void-packages build system.
Use at your own discretion.

## Overview
A collection of template files for building packages on Void Linux.
Includes a helper script, vay, which simplifies local package building and installation.
If you dont wish to build the packages locally, this repository also provides prebuilt binaries in the releases. Information on how to easily download and install them go to [Prebuilt binaries](#prebuilt-binaries).

## Available packages
| package | version | homepage | maintainer | notes |
|:--------|:--------|:---------|:-----------|:------|
| Converseen | 0.15.1.0 | https://github.com/Faster3ck/Converseen | Orphaned |  |
| aquamarine | 0.9.5 | https://github.com/hyprwm/aquamarine | zenobit |  |
| blocky | 0.27.0 | https://0xerr0r.github.io/blocky/latest | krum |  |
| desktop-tui | 0.3.1 | https://github.com/Julien-cpsn/desktop-tui | zenobit |  |
| dotbot | 1.23.1 | https://github.com/anishathalye/dotbot | zenobit |  |
| dtrx | 8.7.0 | https://github.com/dtrx-py/dtrx/ | travankor |  |
| easybashgui | 15.0.1 | https://github.com/BashGui/easybashgui | zenobit |  |
| efl | 1.28.1 | https://enlightenment.org | Orphaned |  |
| enlightenment | 0.27.1 | http://enlightenment.org | Orphaned |  |
| ftxui | 6.1.9 | https://github.com/ArthurSonzogni/FTXUI | zenobit |  |
| gcompris-qt | 25.1.1 | https://gcompris.net/index-en.html | zenobit |  |
| glaze | 6.0.2 | https://github.com/stephenberry/glaze | zenobit |  |
| gpu-screen-recorder | 5.6.8 | https://git.dec05eba.com/gpu-screen-recorder/ | zenobit | x86_64 i686 |
| gpu-screen-recorder-gtk | 5.7.8 | https://git.dec05eba.com/gpu-screen-recorder-gtk/ | zenobit | x86_64 i686 |
| hyprcursor | 0.1.13 | https://github.com/hyprwm/hyprcursor | zenobit |  |
| hyprdynamicmonitors | 1.3.5 | https://github.com/fiffeek/hyprdynamicmonitors | zenobit |  |
| hyprgraphics | 0.3.0 | https://github.com/hyprwm/hyprgraphics | zenobit |  |
| hypridle | 0.1.7 | https://github.com/hyprwm/hypridle | zenobit |  |
| hyprland | 0.52.0 | https://hyprland.org/ | zenobit |  |
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
| hyprtoolkit | 0.2.4 | https://github.com/hyprwm/hyprtoolkit | zenobit |  |
| hyprutils | 0.10.1 | https://github.com/hyprwm/hyprutils | zenobit |  |
| hyprwayland-scanner | 0.4.5 | https://github.com/hyprwm/hyprwayland-scanner | zenobit |  |
| input-remapper | 2.1.1 | https://github.com/sezanzeb/input-remapper | zenobit |  |
| kando | 2.1.0 | https://kando.menu | zenobit | x86_64 aarch64 |
| kde-material-you-colors | 1.10.1 | https://github.com/luisbocanegra/kde-material-you-colors | zenobit |  |
| libspng | 0.7.4 | https://libspng.org/ | zenobit |  |
| linuxcommandlibrary | 3.3.1 | http://linuxcommandlibrary.com/ | zenobit |  |
| ly | 1.1.2 | https://codeberg.org/fairyglade/ly | zenobit | i686 x86_64 |
| musl-locales | 0.1.1 | https://git.adelielinux.org/adelie/musl-locales | zenobit | *-musl |
| nebula-gtk | 1.1.3 | https://github.com/Letdown2491/nebula-gtk | Letdown2491 |  |
| nwg-bar | 0.1.6 | https://github.com/nwg-piotr/nwg-bar | zenobit |  |
| nwg-clipman | 0.2.7 | https://github.com/nwg-piotr/nwg-clipman | zenobit |  |
| nwg-displays | 0.3.26 | https://nwg-piotr.github.io/nwg-shell/nwg-displays | zenobit |  |
| nwg-dock | 0.4.3 | https://nwg-piotr.github.io/nwg-shell/nwg-dock | zenobit |  |
| nwg-dock-hyprland | 0.4.8 | https://nwg-piotr.github.io/nwg-shell/nwg-dock-hyprland | zenobit |  |
| nwg-drawer | 0.7.4 | https://nwg-piotr.github.io/nwg-shell/nwg-drawer | zenobit |  |
| nwg-icon-picker | 0.1.1 | https://github.com/nwg-piotr/nwg-icon-picker | zenobit |  |
| nwg-launchers | 0.7.1.1 | https://github.com/nwg-piotr/nwg-launchers | Érico |  |
| nwg-look | 1.0.6 | https://github.com/nwg-piotr/nwg-look | cinerea0 |  |
| nwg-menu | 0.1.9 | https://nwg-piotr.github.io/nwg-shell/nwg-menu | zenobit |  |
| nwg-panel | 0.10.6 | https://nwg-piotr.github.io/nwg-shell/nwg-panel | zenobit |  |
| nwg-readme-browser | 0.1.7 | https://nwg-piotr.github.io/nwg-shell/nwg-readme-browser | zenobit |  |
| nwg-shell | 0.5.49 | https://nwg-piotr.github.io/nwg-shell | zenobit |  |
| nwg-shell-config | 0.5.62 | https://nwg-piotr.github.io/nwg-shell/nwg-shell-config | zenobit |  |
| opentyrian2000 | 2000.20250408 | https://github.com/KScl/opentyrian2000 | zenobit |  |
| pkgconf | 2.5.1 | http://pkgconf.org/ | Enno |  |
| python3-dasbus | 1.7 | https://github.com/dasbus-project/dasbus | zenobit |  |
| python3-geographiclib | 2.0 | https://geographiclib.sourceforge.io/ | zenobit |  |
| python3-geopy | 2.4.1 | https://github.com/geopy/geopy | zenobit |  |
| python3-imagehash | 4.3.2 | https://github.com/JohannesBuchner/imagehash | zenobit |  |
| python3-materialcolor | 2.0.10 | https://github.com/T-Dynamos/materialyoucolor-python | zenobit |  |
| python3-pyexiv2 | 2.15.5 | https://github.com/LeoHsiao1/pyexiv2 | zenobit |  |
| qca-qt6 | 2.3.10 | https://userbase.kde.org/QCA | John |  |
| qdiskinfo | 0.4 | https://github.com/edisionnano/QDiskInfo | zenobit |  |
| quickemu-rs | 2.0.1 | https://github.com/lj3954/quickemu-rs | zenobit |  |
| quickosdl | 0.3.2 | https://github.com/lj3954/quickosdl | zenobit |  |
| quickshell | 0.2.1 | https://quickshell.org | classabbyamp |  |
| regex-tui | 0.1.0 | https://github.com/vitor-mariano/regex-tui | zenobit |  |
| runkit-git | 999 | https://github.com/Letdown2491/runkit | zenobit |  |
| sdbus-cpp | 2.1.0 | https://github.com/Kistler-Group/sdbus-cpp | zenobit |  |
| sdkmanager | 0.6.11 | https://gitlab.com/fdroid/sdkmanager | zenobit |  |
| shattered-pixel-dungeon | 3.2.5 | https://github.com/00-Evan/shattered-pixel-dungeon | Mihail |  |
| spdlog | 1.16.0 | https://github.com/gabime/spdlog | skmpz |  |
| tomlplusplus | 3.4.0 | https://marzer.github.io/tomlplusplus/ | zenobit |  |
| tuisic | 1.7.2 | https://github.com/Dark-Kernel/tuisic | zenobit |  |
| vbm | 1.0.1 | https://codeberg.org/oSoWoSo/vbm | zenobit |  |
| wayscriber | 0.6.3 | https://github.com/devmobasa/wayscriber | zenobit |  |
| xdg-desktop-portal-hyprland | 1.3.11 | https://github.com/hyprwm/xdg-desktop-portal-hyprland | zenobit |  |
| zen-browser | 1.17.4b | https://www.zen-browser.app/ | Encoded14 | x86_64 aarch64 |
| zig | 0.14.1 | https://ziglang.org | Orphaned | x86_64* aarch64* |
## The `vay` script

`vay` works similarly to AUR helpers on Arch Linux.
Automatically performs the actions needed to build the packages locally on your system.
If you prefer to do this manually go to [Manually building](#manually-building).
Note: this script not only works for the extra template files provided in this repository but also for packages not distrubted in the Voidlinux mirrors such as nonfree packages (discord, spotify, etc.)

## Installation

1. Start by cloning this repository.
```
git clone https://github.com/oSoWoSo/void-user-repository
```

2. Change into the cloned directory:
```
cd void-user-repository
```

3. Create `~/.local/bin` if it doesn’t already exist:
```
mkdir -p ~/.local/bin
```

4. Symlink the helper script:
```
ln -sf "$(realpath vay.sh)" "$HOME/.local/bin/vay"
```

5. Run the helper by typing vay followed by one or more package names:
```
vay <package1> <package2> ...
```

## Prebuilt binaries

Currently prebuilt binary packages are provided for the following architectures:
- x86_64-glibc
- x86_64-musl
- aarch64-glibc
- aarch64-musl

1. Create an entry in /etc/xbps.d/ and add this repository. This can be done with the following commands:
- x86_64-glibc
```
echo repository=https://github.com/oSoWoSo/VUR-x86_64/raw/refs/heads/bin | sudo tee /etc/xbps.d/00-VUR.conf
```
- x86_64-musl
```
echo repository=https://github.com/oSoWoSo/VUR-x86_64-musl/raw/refs/heads/bin | sudo tee /etc/xbps.d/00-VUR.conf
```
- aarch64-glibc
```
echo repository=https://github.com/oSoWoSo/VUR-aarch64/raw/refs/heads/bin | sudo tee /etc/xbps.d/00-VUR.conf
```
- aarch64-musl
```
echo repository=https://github.com/oSoWoSo/VUR-aarch64-musl/raw/refs/heads/bin | sudo tee /etc/xbps.d/00-VUR.conf
```
2. Refresh your repositories and accept the fingerprint:
```
sudo xbps-install -S
```
3. You are now able to search through all of the packages in this repository, and install them as usual:
```
xbps-query -Rs hypr
sudo xbps-install -S hyprland
```

## Manually building
1. Clone both this repository as well as [void-packages](https://github.com/void-linux/void-packages):
```
git clone https://github.com/oSoWoSo/void-user-repository.git
git clone https://github.com/void-linux/void-packages.git
```

2. Copy the templates files from this repository into void-packages:
```
cp -r void-user-repository/srcpkgs/* void-packages/srcpkgs/
```

3. Edit shlibs by removing the lines found in shlibs_remove and appending the lines from shlibs_append.

4. Bootstrap the build system:
```
cd void-packages
./xbps-src binary-bootstrap
```

5. Build the packages you want:
```
./xbps-src pkg <package1> <package2> ...
```

6. Install the built packages:
```
sudo xbps-install --repository /hostdir/binpkgs/ <package1> <package2> ...
```

### Running Hyprland

In order to run Hyprland you will need to install some additional packages which will depend on your setup, for example a [session and seat manager](https://docs.voidlinux.org/config/session-management.html) and [graphics drivers](https://docs.voidlinux.org/config/graphical-session/graphics-drivers/index.html). You may also have to add the user to the `_seatd` group. If you use an Nvidia GPU refer to the [Hyprland Wiki](https://wiki.hyprland.org/Nvidia), but keep in mind that Hyprland does not officially support Nvidia.

### Contributing
Contributions are greatly appreciated. Overall, this repository adheres to the same rules and guidelines as the [official void-packages repository](https://github.com/void-linux/void-packages/blob/master/CONTRIBUTING.md). The main difference is that here, you’re welcome to add template files for Chromium or Firefox forks if they provide additional value beyond changing certain settings or configuration files.

### Credits
[Makrennel: hyprland-void](https://github.com/Makrennel/hyprland-void): Hyprland template files

[Encoded14: void-user-repository](https://github.com/Encoded14/void-user-repository): Better workflow file and some templates

[grvn: void-packages](https://github.com/grvn/void-packages): various template files
