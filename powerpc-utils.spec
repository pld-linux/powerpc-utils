Summary:	Various utilities for Linux/PowerPC
Name:		powerpc-utils
Version:	1.1.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/p/powerpc-utils/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d879b109bb8f0d726304b60b147bff13
Patch0:		%{name}_%{version}-12.diff.gz
BuildRequires:	sgml-tools
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for Linux on PowerPC hardware. mousemode - tell an ADB mouse
to use a given device handler ID. nvsetenv - change/view Open Firmware
environment variables. nvsetvol - set Open Firmware stored volume
setting. clock - Hardware clock program for Power Macs. trackpad -
modify PowerBook trackpad behavior (tap/drag mode). fblevel - control
LCD/TFT display backlight brightness. fnset - set PowerBook keyboard
function keys mode.

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

install clock.8 mousemode.8 nvsetenv.8 nvsetvol.8 trackpad.8 fblevel.8 \
	$RPM_BUILD_ROOT%{_mandir}/man8

install clock mousemode nvsetenv nvsetvol backlight trackpad fblevel fnset \
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
