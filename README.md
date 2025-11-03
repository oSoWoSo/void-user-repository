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
| aquamarine | 0.9.5 | https://hyprland.org/hyprlang/index.html | Encoded14 |  |
| glaze | 6.0.1 | https://github.com/stephenberry/glaze | Encoded14 |  |
| hyprcursor | 0.1.13 | https://github.com/hyprwm/hyprcursor | Encoded14 |  |
| hyprgraphics | 0.2.0 | https://github.com/hyprwm/hyprgraphics | Encoded14 |  |
| hypridle | 0.1.7 | https://github.com/hyprwm/hypridle | Encoded14 |  |
| hyprland | 0.51.1 | https://hyprland.org/ | Encoded14 |  |
| hyprland-protocols | 0.7.0 | https://github.com/hyprwm/hyprland-protocols | Encoded14 |  |
| hyprland-qt-support | 0.1.0 | https://github.com/hyprwm/hyprland-qt-support | Encoded14 |  |
| hyprland-qtutils | 0.1.5 | https://github.com/hyprwm/hyprland-qtutils | Encoded14 |  |
| hyprlang | 0.6.4 | https://hyprland.org/hyprlang/index.html | Encoded14 |  |
| hyprlock | 0.9.2 | https://github.com/hyprwm/hyprlock | Encoded14 |  |
| hyprpaper | 0.7.5 | https://github.com/hyprwm/hyprpaper | Encoded14 |  |
| hyprpicker | 0.4.5 | https://github.com/hyprwm/hyprpicker | Encoded14 |  |
| hyprpolkitagent | 0.1.3 | https://github.com/hyprwm/hyprpolkitagent | Encoded14 |  |
| hyprsunset | 0.3.3 | https://github.com/hyprwm/hyprsunset | Encoded14 |  |
| hyprsysteminfo | 0.1.3 | https://github.com/hyprwm/hyprsysteminfo | Encoded14 |  |
| hyprutils | 0.10.0 | https://github.com/hyprwm/hyprutils | Encoded14 |  |
| hyprwayland-scanner | 0.4.5 | https://github.com/hyprwm/hyprwayland-scanner | Encoded14 |  |
| libspng | 0.7.4 | https://libspng.org/ | Encoded14 |  |
| ly | "1.0.3" | https://github.com/fairyglade/ly | Encoded14 | i686 x86_64 |
| sdbus-cpp | 2.1.0 | https://github.com/Kistler-Group/sdbus-cpp | Encoded14 |  |
| tomlplusplus | 3.4.0 | https://marzer.github.io/tomlplusplus/ | Encoded14 |  |
| xdg-desktop-portal-hyprland | 1.3.11 | https://github.com/hyprwm/xdg-desktop-portal-hyprland | Encoded14 |  |
| zen-browser | "1.17.4b" | https://www.zen-browser.app/ | Encoded14 | x86_64 aarch64 |
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
echo repository=https://raw.githubusercontent.com/oSoWoSo/void-user-repository/repository-x86_64-glibc | sudo tee /etc/xbps.d/20-void-user-repository.conf
```
- x86_64-musl
```
echo repository=https://raw.githubusercontent.com/oSoWoSo/void-user-repository/repository-x86_64-musl | sudo tee /etc/xbps.d/20-void-user-repository.conf
```
- aarch64-glibc
```
echo repository=https://raw.githubusercontent.com/oSoWoSo/void-user-repository/repository-aarch64-glibc | sudo tee /etc/xbps.d/20-void-user-repository.conf
```
- aarch64-musl
```
echo repository=https://raw.githubusercontent.com/oSoWoSo/void-user-repository/repository-aarch64-musl | sudo tee /etc/xbps.d/20-void-user-repository.conf
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
