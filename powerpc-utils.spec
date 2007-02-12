Summary:	Various utilities for Linux/PowerPC
Summary(pl.UTF-8):   Różne narzędzia dla Linuksa na PowerPC
Name:		powerpc-utils
Version:	1.1.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/p/powerpc-utils/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d879b109bb8f0d726304b60b147bff13
Patch0:		%{name}_%{version}-12.diff.gz
BuildRequires:	sgml-tools
Provides:	pmac-utils = %{version}-%{release}
Obsoletes:	pmac-utils
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for Linux on PowerPC hardware:
- mousemode - tell an ADB mouse to use a given device handler ID.
- nvsetenv - change/view Open Firmware environment variables.
- nvsetvol - set Open Firmware stored volume setting.
- trackpad - modify PowerBook trackpad behavior (tap/drag mode).
- fblevel - control LCD/TFT display backlight brightness.
- fnset - set PowerBook keyboard function keys mode.

%description -l pl.UTF-8
Narzędzia dla Linuksa na sprzęcie PowerPC:
- mousemode - ustawianie myszy ADB do używania podanego ID urządzenia
- nvsetenv - zmiana/oglądanie zmiennych środowiskowych OpenFirmware
- nvsetvol - ustawianie głośności zapisanej w OpenFirmware
- trackpad - zmiana zachowania trackpada w PowerBooku (tryb tap/drag)
- fblevel - sterowanie jasnością podświetlenia wyświetlacza LCD/TFT
- fnset - ustawianie trybu klawiszy funkcyjnych klawiatury PowerBooka

%prep
%setup -q -n pmac-utils
%patch0 -p1

%build
%{__make} all-man all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8}

install mousemode.8 nvsetenv.8 nvsetvol.8 trackpad.8 fblevel.8 \
	$RPM_BUILD_ROOT%{_mandir}/man8

install mousemode nvsetenv nvsetvol backlight trackpad fblevel fnset \
	$RPM_BUILD_ROOT%{_sbindir}

install lsprop $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.lsm
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
