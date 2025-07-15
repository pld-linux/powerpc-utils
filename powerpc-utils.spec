Summary:	Various utilities for Linux on Apple PowerPC hardware
Summary(pl.UTF-8):	Różne narzędzia dla Linuksa na platformie PowerPC firmy Apple
Name:		powerpc-utils
Version:	1.1.3
Release:	3
License:	GPL v2+
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/p/powerpc-utils/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d879b109bb8f0d726304b60b147bff13
Patch0:		http://ftp.debian.org/debian/pool/main/p/powerpc-utils/%{name}_%{version}-24.diff.gz
# Patch0-md5:	7766bd30b8f97bf584addca797a50327
BuildRequires:	sgml-tools
Provides:	pmac-utils = %{version}-%{release}
Obsoletes:	pmac-utils
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for Linux on Apple PowerPC (PMac) hardware:
- fblevel - control LCD/TFT display backlight brightness.
- fdeject - eject floppy.
- lsprop - list OF device tree in human readable format.
- autoboot - set autoboot (server mode) flag on CUDA PowerMacs.
- bootsched - set automatic power up time on CUDA PowerMacs.
- backlight - set backlight level on PowerBooks.
- fnset - set PowerBook keyboard function keys mode.
- macos - reboot into MacOS.
- mousemode - tell an ADB mouse to use a given device handler ID.
- nvsetenv - change/view Open Firmware environment variables.
- nvsetvol - set Open Firmware stored volume setting.
- nvvideo - PowerMac video/color mode selector.
- sndvolmix - sound volume setup.
- trackpad - modify PowerBook trackpad behavior (tap/drag mode).

%description -l pl.UTF-8
Narzędzia dla Linuksa na sprzęcie PowerPC firmy Apple (PMac):
- fblevel - sterowanie jasnością podświetlenia wyświetlacza LCD/TFT
- fdeject - wysuwanie dyskietki z napędu
- lsprop - listowanie drzew urządzeń OF w czytelnej postaci
- autoboot - zmiana flagi autoboot (trybu serwera) w PowerMacach CUDA
- bootsched - zmiana czasu automatycznego włączenia w PowerMacach CUDA
- backlight - zmiana poziomu podświetlenia ekranu w PowerBookach
- fnset - ustawianie trybu klawiszy funkcyjnych klawiatury PowerBooka
- macos - reboot i uruchomienie systemu MacOS.
- mousemode - ustawianie myszy ADB do używania podanego ID urządzenia
- nvsetenv - zmiana/oglądanie zmiennych środowiskowych OpenFirmware
- nvsetvol - ustawianie głośności zapisanej w OpenFirmware
- nvvideo - wybór trybu graficznego i liczby kolorów w PowerMacach
- sndvolmix - ustawianie głośności dźwięku.
- trackpad - zmiana zachowania trackpada w PowerBooku (tryb tap/drag)

%prep
%setup -q -n pmac-utils
%patch -P0 -p1

%build
%{__make} all-man all fdeject nvvideo sndvolmix \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8}

install autoboot.8 bootsched.8 fblevel.8 fdeject.8 macos.8 mousemode.8 \
	nvsetenv.8 nvsetvol.8 nvvideo.8 sndvolmix.8 \
	trackpad.8 \
	$RPM_BUILD_ROOT%{_mandir}/man8

install autoboot backlight bootsched fnset macos \
	mousemode nvsetenv nvsetvol nvvideo sndvolmix trackpad \
	$RPM_BUILD_ROOT%{_sbindir}

install fblevel fdeject lsprop $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README pmac-utils-%{version}.lsm
%attr(755,root,root) %{_bindir}/fblevel
%attr(755,root,root) %{_bindir}/fdeject
%attr(755,root,root) %{_bindir}/lsprop
%attr(755,root,root) %{_sbindir}/autoboot
%attr(755,root,root) %{_sbindir}/backlight
%attr(755,root,root) %{_sbindir}/bootsched
%attr(755,root,root) %{_sbindir}/fnset
%attr(755,root,root) %{_sbindir}/macos
%attr(755,root,root) %{_sbindir}/mousemode
%attr(755,root,root) %{_sbindir}/nvsetenv
%attr(755,root,root) %{_sbindir}/nvsetvol
%attr(755,root,root) %{_sbindir}/nvvideo
%attr(755,root,root) %{_sbindir}/trackpad
%{_mandir}/man8/autoboot.8*
%{_mandir}/man8/bootsched.8*
%{_mandir}/man8/fblevel.8*
%{_mandir}/man8/fdeject.8*
%{_mandir}/man8/macos.8*
%{_mandir}/man8/mousemode.8*
%{_mandir}/man8/nvsetenv.8*
%{_mandir}/man8/nvsetvol.8*
%{_mandir}/man8/nvvideo.8*
%{_mandir}/man8/sndvolmix.8*
%{_mandir}/man8/trackpad.8*
